import math
import datetime

from prettytable import PrettyTable
from textwrap import fill

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Ticket

class TicketScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self):
        self.clear_screen()

        print("Main Menu > Tickets")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a ticket		[EP] Process/Edit			[B] Go back")
        print("|	[R] Remove a ticket		[S] Search for")
        print("|	[V] View closed tickets		[D] Ticket details")
        print("|")
        print(ui_consts.SEPERATOR)

        all_tickets = self.ui.logic_api.ticket_get_all() # fyrir edit og view og svona, mögulega ekki sniðugt

        if self.active_search_filter:
            ticket_list = self.ui.logic_api.ticket_search(self.active_search_filter)
        else:
            ticket_list = self.ui.logic_api.ticket_get_all()

        all_tickets_table = PrettyTable()
        all_tickets_table.field_names = ["ID", "Property", "Facility", "Title", "Priority", "Status"]

        for ticket in ticket_list:
            ticket_property = self.ui.logic_api.property_get_by_ID(ticket.propertyID)
            if ticket.facilityID == None:
                facility_name = "None"
            else:
                ticket_facility = self.ui.logic_api.facility_get_by_ID(ticket.facilityID)
                facility_name = ticket_facility.name 
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

        properties = self.ui.logic_api.property_get_all()
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
                priority_list = ["high", "medium", "low"]

                # choose property with verification  
                new_property_id = input("Property ID of ticket: ").upper()  
                validated = self.ui.logic_api.validate_property(new_property_id)
                while not validated:
                    print ("No such property")
                    new_property_id = input("(B) to cancel or Property ID of ticket: ").upper()
                    if new_property_id == "B":
                        return self
                    validated = self.ui.logic_api.validate_property(new_property_id)
                tmp = self.ui.logic_api.facility_get_by_propertyID(new_property_id) 
 

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
                    verified = self.ui.logic_api.facility_validate(new_ticket_facility_id, tmp)
                    while not verified:
                        print ("No such facility at this property")
                        new_ticket_facility_id = input("(B) to cancel or ID of facility for ticket: ").upper()
                        if new_ticket_facility_id == "B":
                            return self
                        verified = self.ui.logic_api.facility_validate(new_ticket_facility_id, tmp)

                while not new_ticket_title: 
                    new_ticket_title = input("New ticket title: ")

                new_description = input("New ticket description: ")
                
                while new_priority not in priority_list:
                    new_priority = input("New ticket priority(high, medium, low): ").lower()

                date_validated = False
                while not date_validated:
                    print ("Use DD-MM-YYYY format")
                    new_date = input("Date to open(leave empty if open now): ")
                    if new_date == "":
                        new_date = datetime.datetime.now()
                    try:
                        date = new_date
                        date_validated = datetime.datetime.strptime(date, "%d-%m-%Y")
                    except ValueError:
                        print ("Sorry wrong format, try again!")

                while new_recurring >= 0:
                    new_recurring = int(input("Recur every N days (0 = never): "))
                
                new_ticket = Ticket(None, new_ticket_facility_id, new_property_id, new_priority, new_ticket_title, new_description,None, None, None, new_recurring , new_date, None, None, None, None, None, None, None, None)
                self.ui.logic_api.ticket_add(new_ticket)

            case "r":    # Remove a ticket
                remove_ticket = input("Remove ticket with ID: ")
                self.ui.logic_api.ticket_remove(remove_ticket)
                
            
            case "v":   # View closed tickets
                # Gefur lista á closed tickets (virkar eins og search með fixed keyword)
                pass

            case "d":   # Ticket details
                ticket_by_id = None
                while ticket_by_id is None:
                    view_ticket = input("Type in ID of ticket for details: ").upper()


                    ticket_by_id = self.ui.logic_api.ticket_get_by_ID(view_ticket)
                    
                    if ticket_by_id is None:
                        print(f"No ticket with the ID: '{view_ticket}', try again (B to cancel).")
                    if view_ticket == "B":
                        return self
                    

                ticket_table = PrettyTable()
                #total_cost = ticket_by_id.cost + ticket_by_id.contractor_fee
                ticket_table.field_names = ["ID", ticket_by_id.ID]
                ticket_table.add_row(["Facility", ticket_by_id.facilityID], divider=True)
                ticket_table.add_row(["Property", ticket_by_id.propertyID], divider=True)
                ticket_table.add_row(["Priority", ticket_by_id.priority], divider=True)
                ticket_table.add_row(["Title", ticket_by_id.title], divider=True)
                ticket_table.add_row(["Description", fill(ticket_by_id.description, width=50)], divider=True)
                ticket_table.add_row(["Open?", ticket_by_id.open], divider=True)
                ticket_table.add_row(["Status", ticket_by_id.status], divider=True)
                ticket_table.add_row(["Recurring?", ticket_by_id.recurring], divider=True)
                ticket_table.add_row(["Recurring days", ticket_by_id.recurring_days], divider=True)
                ticket_table.add_row(["Open date", ticket_by_id.open_date], divider=True)
                ticket_table.add_row(["Staff", ticket_by_id.staffID], divider=True)
                ticket_table.add_row(["Report", fill(ticket_by_id.report)], divider=True)
                ticket_table.add_row(["Cost", ticket_by_id.cost], divider=True)
                ticket_table.add_row(["Contractor", ticket_by_id.contractorID], divider=True)
                ticket_table.add_row(["Contr. review", ticket_by_id.contractor_review], divider=True)
                ticket_table.add_row(["Contr. rating", ticket_by_id.contractor_rating], divider=True)
                ticket_table.add_row(["Contractor fee", ticket_by_id.contractor_fee], divider=True)
                #ticket_table.add_row(["Total cost", total_cost], divider=True)

                print(ticket_table)
                input("Press enter to continue.")

            case "ep":    # Edit ticket
                # If ID does not exist in the ticket list, raise error "No ticket found with that ID!"
                # If ID does not exist, cancel command


                for ticket in all_tickets:
                    if ticket == ticket.ID:
                        edit_ticket = ticket
                        
                print("If you do not wish to change a specific field, you can leave the input empty")
                edit_ticket = None
                ticket_attributes = ["facilityID", "propertyID", "priority", "title", "description", "status", "recurring", "recurring_days", "open_date","close_date","staffID","report","cost","contractorID","contractor_review","contractor_rating","contractor_fee"]

                while edit_ticket is None:
                    pick_ticket = input("Type in ID of ticket to edit: ").upper()
                    if edit_ticket == "B":
                        return self
                    
                    edit_ticket = self.ui.logic_api.ticket_get_by_ID(pick_ticket)

                    if edit_ticket is not None:
                        for attribute in ticket_attributes:
                            current_value = getattr(edit_ticket, attribute)
                            new_value = input(f"New {attribute} (Current: {current_value}): ").strip()
                            if new_value:
                                setattr(edit_ticket, attribute, new_value)
                        self.ui.logic_api.ticket_edit(edit_ticket)

                    else:
                        print(f"No ticket with the ID: '{view_ticket}', try again (B to cancel).")
                    if pick_ticket == "B".upper():
                        return self

                # # if recur > 0 set recurring = True otherwise False

            case "s":    # Search for
                self.active_search_filter = input("Search for: ")
                # "Main menu > Tickets > Filtered" window and commands are identical to "Main menu > Tickets"
            

            case "b":
                return ui_consts.CMD_BACK

        return self
