# standard library imports
import math
import datetime
from textwrap import fill

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Ticket

class TicketScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self) -> str | None:
        self.clear_screen()

        print("Main Menu > Tickets")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add a ticket		[E] Edit			[B] Go back")
            print("|	[R] Remove a ticket		[S] Search for			[PR] Process")
            print("|	[V] View closed/open tickets	[D] Ticket details")
        else:
            print_formatted_text(HTML("|	[A] Add a ticket		<s>[E] Edit</s>			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove a ticket</s>		[S] Search for			[PR] Process"))
            print_formatted_text(HTML("|	[V] View closed/open tickets	[D] Ticket details"))

        print("|")
        print(ui_consts.SEPERATOR)

        # Geyma nöfn til að þurfa ekki að fletta upp í hvert skipti
        facility_names = {}
        property_names = {}
        staff_names = {}

        # Smíða töflu af destinations til að geta nýtt hana á fleiri en einum stað
        properties = self.logic_api.property_get_all()
        property_table = PrettyTable()
        property_table.field_names = ["Property ID","Name","Destination","Type"]
        for property in properties:
            property_table.add_row([property.ID, property.name,property.destinationID,property.type])

        logged_in_destinationID = self.logic_api.get_logged_in_staff().destinationID

        if self.active_search_filter:
            ticket_list = self.logic_api.ticket_search_only_destinationID(self.active_search_filter,logged_in_destinationID)
        else:
            ticket_list = self.logic_api.ticket_get_by_destinationID(logged_in_destinationID)

        total_pages = math.ceil(len(ticket_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        all_tickets_table = PrettyTable()
        all_tickets_table.field_names = ["ID", "Property", "Facility", "Title", "Priority", "Status"]
        all_tickets_table._min_table_width = ui_consts.TABLE_WIDTH

        for ticket in ticket_list:
            ticket_property = self.logic_api.property_get_by_ID(ticket.propertyID)

            if ticket.facilityID == None:
                facility_name = "None"
            else:
                ticket_facility = self.logic_api.facility_get_by_ID(ticket.facilityID)
                facility_name = ticket_facility.name

            ticket_staff = self.logic_api.staff_get_by_ID(ticket.staffID)
            if ticket_staff is None:
                staff_name = "No staff assigned"
            else:
                staff_name = ticket_staff.name

            facility_names[ticket.facilityID] = facility_name
            property_names[ticket.propertyID] = ticket_property.name
            staff_names[ticket.staffID] = staff_name

            all_tickets_table.add_row([ticket.ID, ticket_property.name, facility_name, fill(ticket.title, width=40), ticket.priority, ticket.status])

        print(f"|  Ticket list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page" + f" [{logged_in_destinationID}]") #TODO DEBUG REMOVE

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(all_tickets_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("")
            print("No tickets found.")

        print("")
        cmd = input("Command: ").lower()

        match cmd:

            # TODO DEBUG REMOVE
            case "sw":
                match self.logic_api.get_logged_in_staff().destinationID:
                    case "D1":
                        self.logic_api.get_logged_in_staff().destinationID = "D2"
                    case "D2":
                        self.logic_api.get_logged_in_staff().destinationID = "D3"
                    case "D3":
                        self.logic_api.get_logged_in_staff().destinationID = "D1"

            case "n":   # Next page:
                self.current_page += 1

            case "p":   # Previous page:
                self.current_page -= 1

            case "a":   # Add a ticket

                print(property_table)
                new_ticket_title = ""
                new_recurring = -1
                new_priority = ""
                priority_list = ["High", "Medium", "Low"]

                # choose property with verification
                new_property_id = input("Property ID of ticket: ").upper()
                validated = self.logic_api.property_validate(new_property_id)
                while not validated:
                    print ("No such property")
                    new_property_id = input("(B) to cancel or Property ID of ticket: ").upper()
                    if new_property_id == "B":
                        return None
                    validated = self.logic_api.property_validate(new_property_id)
                tmp = self.logic_api.facility_get_by_propertyID(new_property_id)

                #Choose facility with verification
                if len(tmp) == 0:
                    print ("No Facilities to choose, using propertyID only")
                    new_ticket_facility_id = None
                else:
                    facility_table = PrettyTable()
                    facility_table.field_names = ["ID","Name","Description"]
                    for facility in tmp:
                        facility_table.add_row([facility.ID,facility.name,facility.description])
                    print(facility_table) 

                    new_ticket_facility_id = input("ID of facility for ticket: ").upper()
                    verified = self.logic_api.facility_validate(new_ticket_facility_id, tmp)
                    while not verified:
                        print ("No such facility at this property")
                        new_ticket_facility_id = input("(B) to cancel or ID of facility for ticket: ").upper()
                        if new_ticket_facility_id == "B":
                            return None
                        verified = self.logic_api.facility_validate(new_ticket_facility_id, tmp)

                while not new_ticket_title:
                    new_ticket_title = input("New ticket title: ").strip()

                new_description = input("New ticket description: ")

                while new_priority not in priority_list:
                    new_priority = input("New ticket priority(high, medium, low): ").lower().capitalize()

                date_validated = False
                while not date_validated:
                    print ("Use DD-MM-YYYY format")
                    new_open_date = input("Date to open(leave empty if open now): ")
                    if new_open_date == "":
                        new_open_date = datetime.datetime.now().strftime("%d-%m-%Y")
                    try:
                        date = new_open_date
                        date_validated = datetime.datetime.strptime(date, "%d-%m-%Y")
                    except ValueError:
                        print ("Sorry wrong format, try again!")

                while new_recurring < 0:
                    try:
                        new_recurring = int(input("Recur every N days (0 = never): "))
                    except ValueError:
                        print("Invalid input, Please enter a valid number.")
                        new_recurring = -1
                ticket_recurring = True if new_recurring > 0 else False

                new_ticket = Ticket(ID = None, facilityID = new_ticket_facility_id, propertyID = new_property_id, 
                                    priority = new_priority, title = new_ticket_title, description = new_description, status = "Open", 
                                    recurring = ticket_recurring, recurring_days = new_recurring , open_date = new_open_date, 
                                    close_date = None, staffID = None, report = None, cost = 0, contractorID = None, 
                                    contractor_review = None, contractor_rating = None, contractor_fee = None)
                self.logic_api.ticket_add(new_ticket)

            case "r":    # Remove a ticket
                if self.logic_api.is_manager_logged_in():
                    remove_ticket = input("Remove ticket with ID: ").upper()
                    try:
                        self.logic_api.ticket_remove(remove_ticket)
                    except Exception as e:
                        print(f"Error removing ticket '{remove_ticket}':")
                        print(f"{type(e).__name__}: {e}")
                        input("Press any key to continue")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")

            case "v":   # View closed tickets
                if self.active_search_filter == "Closed":
                    self.active_search_filter = ""
                else:
                    self.active_search_filter = "Closed"

            case "d":   # Ticket details
                ticket_by_id = None
                while ticket_by_id is None:
                    view_ticket = input("Type in ID of ticket for details: ").upper()

                    ticket_by_id = self.logic_api.ticket_get_by_ID(view_ticket)
                    
                    if ticket_by_id is None:
                        print(f"No ticket with the ID: '{view_ticket}', try again (B to cancel).")
                    if view_ticket == "B":
                        return None

                self.print_ticket_detail_table(ticket_by_id)

                input("Press enter to continue.")

            case "e":# Edit ticket
                if self.logic_api.is_manager_logged_in():

                    ##### ÞARF LOCKED/OPEN FUNCTIONALITY, má ekki edita ef locked.
                    priority_list = ["High", "Medium", "Low"]
                    edit_priority = ""
                    edit_ticket_title = ""
                    #edit_description = ""
                    #"open_date","close_date","staffID","report","cost","contractorID","contractor_review","contractor_rating","contractor_fee"
                    
                    print("If you do not wish to change a specific field, you can leave the input empty")
                    
                    #ticket_attributes = ["priority", "title", "description", "status", "recurring_days"]

                    edit_ticket = None
                    while edit_ticket is None:
                        pick_ticket = input("Type in ID of ticket to edit or b to back: ").upper()
                        if pick_ticket == "B":
                            return None

                        edit_ticket = self.logic_api.ticket_get_by_ID(pick_ticket)

                        if (edit_ticket is not None) and (edit_ticket.status == "Closed"):
                            self.print_ticket_detail_table(edit_ticket)
                            print ("Tickets need to be open to edit or progress them")
                            answer = input(print ("Do you want to open the ticket? (yes/y to open, no/n to stay closed)")).lower()
                            if answer == "yes" or answer == "y":
                                edit_ticket.status = "Open"
                            elif answer == "no" or answer == "n":
                                return None
                            self.logic_api.ticket_edit(edit_ticket)                                
                            

                        if (edit_ticket is not None) and (edit_ticket.status != "Closed"):

                            # Edit property with verification
                            self.print_ticket_detail_table(edit_ticket)
                            print(property_table)
                            print ("Leave empty if you don't want to change propertyID")
                            edit_property_id = input(f"New propertyID (Current: {edit_ticket.propertyID}) associated with ticket {edit_ticket.ID}: ").upper()
                            if edit_property_id.strip() == "":
                                edit_property_id = edit_ticket.propertyID
                            validated = self.logic_api.property_validate(edit_property_id)
                            while not validated:
                                if edit_property_id == "B":
                                    return None
                                print ("No such property, type B to back or try again")
                                edit_property_id = input(f"New propertyID (Current: {edit_ticket.propertyID}) associated with ticket {edit_ticket.ID}: ").upper()
                                if edit_property_id == "":
                                    edit_property_id = edit_ticket.propertyID
                                validated = self.logic_api.property_validate(edit_property_id)
                            tmp = self.logic_api.facility_get_by_propertyID(edit_property_id)

                            #Edit facility with verification
                            self.print_ticket_detail_table(edit_ticket)
                            if len(tmp) == 0:
                                print ("No Facalities to choose, using propertyID only")
                                edit_ticket.facilityID = None
                            else:
                                facility_table = PrettyTable()
                                facility_table.field_names = ["ID","Name","Description"]
                                for facility in tmp:
                                    facility_table.add_row([facility.ID,facility.name,facility.description])
                                print(facility_table) 

                                print ("Leave empty if you don't want to change facilityID")
                                edit_ticket_facility_id = input(f"New propertyID (Current: {edit_ticket.facilityID}) associated with ticket {edit_ticket.ID}: ").upper()
                                if edit_ticket_facility_id.strip() == "":
                                    verified = True
                                    edit_ticket_facility_id = edit_ticket.facilityID
                                else:
                                    verified = self.logic_api.facility_validate(edit_ticket_facility_id, tmp)
                                while not verified:
                                    if new_ticket_facility_id == "B":
                                        return None
                                    print ("No such facility at this property, B to cancel or try again")
                                    new_ticket_facility_id = input(f"New propertyID (Current: {edit_ticket.facilityID}) associated with ticket {edit_ticket.ID}: ").upper()
                                    if edit_ticket_facility_id.strip() == "":
                                        edit_ticket_facility_id = edit_ticket.facilityID
                                    verified = self.logic_api.facility_validate(new_ticket_facility_id, tmp)

                            
                            self.print_ticket_detail_table(edit_ticket)
                            while edit_priority not in priority_list: # edit priority 
                                print ("leave empty if you don't wish to change priority")
                                edit_priority = input(f"edit ticket priority(high, medium, low), current ({edit_ticket.priority}): ").lower().capitalize()
                                if edit_priority.strip() == "":
                                    edit_priority = edit_ticket.priority
                            edit_ticket.priority = edit_priority.lower().capitalize()

                            self.print_ticket_detail_table(edit_ticket)
                            while not edit_ticket_title:
                                print ("leave empty if you don't wish to change ticket title")
                                edit_ticket_title = input("New ticket title: ").strip()
                                if edit_ticket_title == "":
                                    edit_ticket_title = edit_ticket.title
                            edit_ticket.title = edit_ticket_title



                            self.logic_api.ticket_edit(edit_ticket)

                        else:
                            print(f"No ticket with the ID: '{pick_ticket}', try again (B to cancel).")

            case "pr":
                #
                edit_recurring = -1
                process_ticket = None
                process_cost = -1
                chosen_contractor = ""
                contractor_rating = -1
                contractor_fee = -1 

                while process_ticket is None:
                    pick_ticket = input("Type in ID of ticket to edit or b to back: ").upper()
                    if pick_ticket == "B":
                        return None
                    
                    process_ticket = self.logic_api.ticket_get_by_ID(pick_ticket)

                    if process_ticket is not None and process_ticket.status == "Done" and self.logic_api.is_manager_logged_in():

                        self.print_ticket_detail_table(process_ticket)
                        print ("This ticket is ready for completion")
                        answer = input("type yes/y if you want to mark this as complete: ").lower()
                        if answer == "yes" or answer == "y":
                            print ("\nleave empty if you wish to add nothing")
                            report = input("Type in comment to add to report: ").strip()
                            if report != "":
                                userID = self.logic_api.get_logged_in_staff().name
                                process_ticket.report += f"\n{userID} {report}"
                            process_ticket.status = "Closed"
                            process_ticket.close_date = datetime.datetime.now().strftime("%d-%m-%Y")
                            self.logic_api.ticket_edit(process_ticket)


                    if process_ticket is not None and process_ticket.status != "Closed":
                        
                        self.print_ticket_detail_table(process_ticket)
                        while edit_recurring < 0:
                            print (f"\nCurrent recur rate in days {process_ticket.recurring_days}")
                            try:
                                edit_recurring = int(input("New recur rate every X days (0 = never): "))
                                #edit_recurring = process_ticket.recurring_days
                            except ValueError:
                                print("\nInvalid input, Please enter a number")
                                edit_recurring = -1
                        process_ticket.recurring_days = edit_recurring

                        self.print_ticket_detail_table(process_ticket)
                        while process_cost < 0:
                            print (f"\nIf there was material cost, type in how much: ")
                            try:
                                process_cost = int(input("Type 0 if none: "))
                                #process_cost = process_ticket.cost
                            except ValueError:
                                print ("please enter a valid number or leave empty.")
                                process_cost = -1
                        process_ticket.cost = process_cost

                        print ("\nWas a contractror involved in the ticket?")
                        contractor = input("(\"yes\" if so, anything else if not): ").lower()
                        if contractor == "yes" or contractor == "y":
                            
                            self.print_ticket_detail_table(process_ticket)
                            destination_id = self.logic_api.property_get_by_ID(process_ticket.propertyID).destinationID
                            contractor_in_destination = self.logic_api.contractor_get_by_destinationID(destination_id)
                            Contractor_table = PrettyTable()
                            Contractor_table.field_names = ["ID","Name","Rating", "phone", "opening hours", "type"]
                            for contractor_inst in contractor_in_destination:
                                Contractor_table.add_row([contractor_inst.ID,contractor_inst.name,contractor_inst.rating, contractor_inst.phone, contractor_inst.opening_hours, contractor_inst.contractor_type])
                            print(Contractor_table)

                            validated_contractor = False
                            while not validated_contractor:
                                chosen_contractor = input("Choose ID of contractor you want to register for this job: ").upper()
                                for con in contractor_in_destination:
                                    if chosen_contractor == con.ID:
                                        validated_contractor = True
                            process_ticket.contractorID = chosen_contractor

                            print ("\nleave empty if you do not wish to add a review")
                            contractor_review = input ("Review of the job done: ")
                            process_ticket.contractor_review = contractor_review

                            while contractor_rating < 0 or contractor_rating > 10:
                                contractor_rating = float(input("\ninput a rating for the contractor used from 0-10: "))
                                if contractor_rating < 0 or contractor_rating > 10:
                                    print("Try again")
                            process_ticket.contractor_rating = contractor_rating

                            while contractor_fee <= 0:
                                contractor_fee = int(input("How much was the fee for the contractor: "))
                                if contractor_fee <= 0:
                                    print ("Try again")
                            process_ticket.contractor_fee = contractor_fee

                        self.print_ticket_detail_table(process_ticket)
                        process_report = input ("\nWrite report here: ")
                        process_ticket.report = process_report
                        process_ticket.status = "Done"
                        process_ticket.staffID = self.logic_api.get_logged_in_staff().ID

                        
                        if contractor == "yes" or contractor == "y":
                            self.logic_api.contractor_update_rating(process_ticket.contractorID)
                        
                        print ("this is the final version of the ticket")
                        self.print_ticket_detail_table(process_ticket)
                        save_it = input("Is this acceptable(yes or y to agree, anything else to dismiss): ")
                        if save_it == "yes" or save_it == "y":
                            self.logic_api.ticket_edit(process_ticket)
                        else:
                            return self



            case "s":    # Search for
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)
                # "Main menu > Tickets > Filtered" window and commands are identical to "Main menu > Tickets"

            case "b":
                return ui_consts.CMD_BACK

        return None

    def print_ticket_detail_table(self, ticket_by_id : Ticket) -> None:
        ticket_table = PrettyTable()

        if ticket_by_id.facilityID is not None:
            facility_name = self.logic_api.facility_get_by_ID(ticket_by_id.facilityID).name
        else:
            facility_name = "No facility"

        property_name = self.logic_api.property_get_by_ID(ticket_by_id.propertyID).name

        if ticket_by_id.staffID is not None:
            staff_name = self.logic_api.staff_get_by_ID(ticket_by_id.staffID).name
        else:
            staff_name = "No staff"

        ticket_table.field_names = ["ID", ticket_by_id.ID]
        ticket_table.add_row(["Facility", facility_name], divider=True)
        ticket_table.add_row(["Property", property_name], divider=True)
        ticket_table.add_row(["Priority", ticket_by_id.priority], divider=True)
        ticket_table.add_row(["Title", ticket_by_id.title], divider=True)
        ticket_table.add_row(["Description", fill(ticket_by_id.description, width=50)], divider=True)
        ticket_table.add_row(["Status", ticket_by_id.status], divider=True)
        ticket_table.add_row(["Recurring?", ticket_by_id.recurring], divider=True)
        ticket_table.add_row(["Recurring days", ticket_by_id.recurring_days], divider=True)
        ticket_table.add_row(["Open date", ticket_by_id.open_date], divider=True)
        ticket_table.add_row(["Staff", staff_name], divider=True)
        if ticket_by_id.report:
            ticket_table.add_row(["Report", fill(ticket_by_id.report)], divider=True)
        ticket_table.add_row(["Cost", ticket_by_id.cost], divider=True)
        ticket_table.add_row(["Contractor", ticket_by_id.contractorID], divider=True)
        ticket_table.add_row(["Contr. review", ticket_by_id.contractor_review], divider=True)
        ticket_table.add_row(["Contr. rating", ticket_by_id.contractor_rating], divider=True)
        ticket_table.add_row(["Contractor fee", ticket_by_id.contractor_fee], divider=True)

        print(ticket_table.get_string())
