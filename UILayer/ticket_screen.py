import math
import datetime
from textwrap import fill

from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Ticket

class TicketScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self):
        self.clear_screen()

        print("Main Menu > Tickets")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add a ticket		[E] Edit/Process			[B] Go back")
            print("|	[R] Remove a ticket		[S] Search for")
            print("|	[V] View closed tickets		[D] Ticket details")
        else:
            print_formatted_text(HTML("|	[A] Add a ticket		[E] Edit/Process			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove a ticket</s>		[S] Search for"))
            print_formatted_text(HTML("|	[V] View closed tickets		[D] Ticket details"))

        print("|")
        print(ui_consts.SEPERATOR)

        # Geyma nöfn til að þurfa ekki að fletta upp í hvert skipti
        facility_names = {}
        property_names = {}
        staff_names = {}

        #all_tickets = self.logic_api.ticket_get_all() # fyrir edit og view og svona, mögulega ekki sniðugt

        if self.active_search_filter:
            ticket_list = self.logic_api.ticket_search(self.active_search_filter)
        else:
            ticket_list = self.logic_api.ticket_get_all()

        all_tickets_table = PrettyTable()
        all_tickets_table.field_names = ["ID", "Property", "Facility", "Title", "Priority", "Status"]

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

        all_tickets_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(ticket_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Ticket list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(all_tickets_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        properties = self.logic_api.property_get_all()
        property_table = PrettyTable()
        property_table.field_names = ["Property ID","Name","Destination","Type"]
        for property in properties:
            property_table.add_row([property.ID, property.name,property.destinationID,property.type])

        match cmd:

            case "n":   # Next page:
                self.current_page += 1

            case "p":   # Previous page:
                self.current_page -= 1

            case "a":   # Add a ticket

                print(property_table)
                new_ticket_title = ""
                new_date = ""
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
                        return self
                    validated = self.logic_api.property_validate(new_property_id)
                tmp = self.logic_api.facility_get_by_propertyID(new_property_id)

                #Choose facility with verification
                if len(tmp) == 0:
                    print ("No Facalities to choose, using propertyID only")
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
                            return self
                        verified = self.logic_api.facility_validate(new_ticket_facility_id, tmp)

                while not new_ticket_title:
                    new_ticket_title = input("New ticket title: ").strip()

                new_description = input("New ticket description: ")

                while new_priority not in priority_list:
                    new_priority = input("New ticket priority(high, medium, low): ").lower().capitalize()

                date_validated = False
                while not date_validated:
                    print ("Use DD-MM-YYYY format")
                    new_date = input("Date to open(leave empty if open now): ")
                    if new_date == "":
                        new_date = datetime.datetime.now().strftime("%d-%m-%Y")
                    try:
                        date = new_date
                        date_validated = datetime.datetime.strptime(date, "%d-%m-%Y")
                    except ValueError:
                        print ("Sorry wrong format, try again!")

                while new_recurring < 0:
                    try:
                        new_recurring = int(input("Recur every N days (0 = never): "))
                    except ValueError:
                        print("Invalid input, Please enter a valid number.")
                        new_recurring = -1

                new_ticket = Ticket(None, new_ticket_facility_id, new_property_id, new_priority, new_ticket_title, new_description,None, None, None, new_recurring , new_date, None, None, None, None, None, None, None, None)
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
                # Gefur lista á closed tickets (virkar eins og search með fixed keyword)
                pass

            case "d":   # Ticket details
                ticket_by_id = None
                while ticket_by_id is None:
                    view_ticket = input("Type in ID of ticket for details: ").upper()

                    ticket_by_id = self.logic_api.ticket_get_by_ID(view_ticket)
                    
                    if ticket_by_id is None:
                        print(f"No ticket with the ID: '{view_ticket}', try again (B to cancel).")
                    if view_ticket == "B":
                        return self

                print(ticket_by_id.staffID)

                ticket_table = PrettyTable()
                #total_cost = ticket_by_id.cost + ticket_by_id.contractor_fee
                ticket_table.field_names = ["ID", ticket_by_id.ID]
                ticket_table.add_row(["Facility", facility_names[ticket_by_id.facilityID]], divider=True)
                ticket_table.add_row(["Property", property_names[ticket_by_id.propertyID]], divider=True)
                ticket_table.add_row(["Priority", ticket_by_id.priority], divider=True)
                ticket_table.add_row(["Title", ticket_by_id.title], divider=True)
                ticket_table.add_row(["Description", fill(ticket_by_id.description, width=50)], divider=True)
                ticket_table.add_row(["Open?", ticket_by_id.open], divider=True)
                ticket_table.add_row(["Status", ticket_by_id.status], divider=True)
                ticket_table.add_row(["Recurring?", ticket_by_id.recurring], divider=True)
                ticket_table.add_row(["Recurring days", ticket_by_id.recurring_days], divider=True)
                ticket_table.add_row(["Open date", ticket_by_id.open_date], divider=True)
                ticket_table.add_row(["Staff", staff_names[ticket.staffID]], divider=True)
                if ticket_by_id.report:
                    ticket_table.add_row(["Report", fill(ticket_by_id.report)], divider=True)
                ticket_table.add_row(["Cost", ticket_by_id.cost], divider=True)
                ticket_table.add_row(["Contractor", ticket_by_id.contractorID], divider=True)
                ticket_table.add_row(["Contr. review", ticket_by_id.contractor_review], divider=True)
                ticket_table.add_row(["Contr. rating", ticket_by_id.contractor_rating], divider=True)
                ticket_table.add_row(["Contractor fee", ticket_by_id.contractor_fee], divider=True)
                #ticket_table.add_row(["Total cost", total_cost], divider=True)

                print(ticket_table)
                input("Press enter to continue.")

            case "e":# Edit ticket
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
                        return self

                    edit_ticket = self.logic_api.ticket_get_by_ID(pick_ticket)

                    if edit_ticket is not None:

                        # Edit property with verification
                        print(property_table)
                        print ("Leave empty if you don't want to change propertyID")
                        edit_property_id = input(f"New propertyID (Current: {edit_ticket.propertyID}) associated with ticket {edit_ticket.ID}: ").upper()
                        if edit_property_id.strip() == "":
                            edit_property_id = edit_ticket.propertyID
                        validated = self.logic_api.validate_property(edit_property_id)
                        while not validated:
                            if edit_property_id == "B":
                                return self
                            print ("No such property, type B to back or try again")
                            edit_property_id = input(f"New propertyID (Current: {edit_ticket.propertyID}) associated with ticket {edit_ticket.ID}: ").upper()
                            if edit_property_id == "":
                                edit_property_id = edit_ticket.propertyID
                            validated = self.logic_api.validate_property(edit_property_id)
                        tmp = self.logic_api.facility_get_by_propertyID(edit_property_id)

                        #Edit facility with verification
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
                                edit_ticket_facility_id = edit_ticket.facilityID
                            verified = self.logic_api.facility_validate(edit_ticket_facility_id, tmp)
                            while not verified:
                                if new_ticket_facility_id == "B":
                                    return self
                                print ("No such facility at this property, B to cancel or try again")
                                new_ticket_facility_id = input(f"New propertyID (Current: {edit_ticket.facilityID}) associated with ticket {edit_ticket.ID}: ").upper()
                                if edit_ticket_facility_id.strip() == "":
                                    edit_ticket_facility_id = edit_ticket.facilityID
                                verified = self.logic_api.facility_validate(new_ticket_facility_id, tmp)

                        while edit_priority not in priority_list: # edit priority 
                            print ("leave empty if you don't wish to change priority")
                            edit_priority = input(f"edit ticket priority(high, medium, low), current ({edit_ticket.priority}): ").lower().capitalize()
                            if edit_priority.strip() == "":
                                edit_priority = edit_ticket.priority
                        edit_ticket.priority = edit_priority.lower().capitalize()

                        while not edit_ticket_title:
                            print ("leave empty if you don't wish to change ticket title")
                            edit_ticket_title = input("New ticket title: ").strip()
                            if edit_ticket_title == "":
                                edit_ticket_title = edit_ticket.title
                        edit_ticket.title = edit_ticket_title



                        self.logic_api.ticket_edit(edit_ticket)

                    else:
                        print(f"No ticket with the ID: '{pick_ticket}', try again (B to cancel).")


            case "p":
                #rest af edit
                edit_recurring = -1
                process_ticket = None
                process_cost = -1
                while process_ticket is None:
                    pick_ticket = input("Type in ID of ticket to edit or b to back: ").upper()
                    if pick_ticket == "B":
                        return self
                    
                    process_ticket = self.logic_api.ticket_get_by_ID(pick_ticket)

                    if process_ticket is not None:

                        while edit_recurring < 0:
                            print (f"Current recur rate in days {process_ticket.recurring_days}")
                            print ("leave empty if you want it to remain as is")
                            try:
                                edit_recurring = input(" New recur rate every X days (0 = never): ")
                                if edit_recurring.strip() == "":
                                    break
                                edit_recurring = int(edit_recurring)
                            except ValueError:
                                print("Invalid input, Please enter a number")
                                edit_recurring = -1
                        process_ticket.recurring_days = edit_recurring
                    
                        while process_cost < 0:
                            print (f"If there was material cost, type in how much: ")
                            try:
                                process_cost = input(f"leave empty if none or type 0")
                                if  process_cost.strip() == "" or int(process_cost) == 0:
                                    process_ticket.cost = 0
                                else:
                                    process_ticket.cost = int(process_cost) 
                            except ValueError:
                                print ("please enter a valid number or leave empty.")
                                process_cost = -1

                        contractor = input("Was a contractred involved in the ticket? (\"yes\" if so): ").lower()
                        if contractor == "yes":
                            pass


                                


                        
                    
                        


            case "s":    # Search for
                self.active_search_filter = input("Search for: ")
                # "Main menu > Tickets > Filtered" window and commands are identical to "Main menu > Tickets"

            case "b":
                return ui_consts.CMD_BACK

        return self
