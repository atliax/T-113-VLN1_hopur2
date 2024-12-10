import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Ticket

class TicketScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        print("Main Menu > Tickets")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a ticket		[E] Edit a ticket			[B] Go back")
        print("|	[R] Remove a ticket		[S] Search for")
        print("|	[V] View closed tickets		[MR] Make a ticket report")
        print("|	[D] Ticket details		[VR] View a ticket report")
        print("|")
        print(ui_consts.SEPERATOR)

        all_tickets = self.ui.logic_api.ticket_get_all()

        all_tickets_table = PrettyTable()
        all_tickets_table.field_names = ["ID", "Property", "Facility", "Title", "Priority", "Status"]

        for ticket in all_tickets:
            ticket_property = self.ui.logic_api.property_get_by_ID(ticket.propertyID)
            ticket_facility = self.ui.logic_api.facility_get_by_ID(ticket.facilityID)
            all_tickets_table.add_row([ticket.ID, ticket_property.name, ticket_facility.name, ticket.title, ticket.priority, ticket.status])

        all_tickets_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(all_tickets) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Ticket list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if total_pages != 0:
            print(all_tickets_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()
        # ÞAÐ VANTAR AÐ HAFA OPTION TIL AÐ OPNA LOKAÐA VERKSKÝRSLU

        match cmd:
            # Next page:
            case "n":
                self.current_page += 1
            # Previous page:
            case "p":
                self.current_page -= 1
            # Add a ticket
            case "a":
                # Auto ID kerfi ekki implementað
                print(f"New ticket property ID: {"MISSING"}")
                print(f"New ticket facility ID: {"MISSING"}")
                new_ticket = input("New ticket title: ")
                new_description = input("New ticket description: ")
                new_priority = input("New ticket priority: ")
                new_status = input("New ticket status: ")
                new_date = input("New ticket date: ")
                new_recurring = int(input("Recur every N days (0 = never): "))
                # If recur > 0 set recurring = True otherwise False
            # Remove a ticket
            case "r":
                remove_ticket = input("Remove ticket with ID: ")
            # View closed tickets
            case "v":
                # Gefur lista á closed tickets (virkar eins og search með fixed keyword)
                pass
            # Ticket details
            case "d":
                view = input("View the details")
                print(f"Property: {"MISSING"}, Priority: {new_priority}")
                print(f"Facility: {"MISSING"}, Status: {new_status}")
                print(f"Title: {new_ticket}")
                print(f"Description: {new_description}")
                print(f"Date: {new_date}")
                # If a response is available from a manager
                print(f"Response: {"MISSING"}")
            # Edit ticket
            case "e":
                # If ID does not exist in the ticket list, raise error "No ticket found with that ID!"
                # If ID does not exist, cancel command
                print("If you do not wish to change a specific field, you can leave the input empty")
                change_title = input("Change ticket title to: ")
                change_description = input("Change ticket description to: ")
                change_priority = input("Change ticket priority to: ")
                change_status = input("Change ticket status: ")
                change_date = input("Change ticket date to: ")
                change_recurring = int(input("Change if ticket should recur every N days (0 = never): "))
                # if recur > 0 set recurring = True otherwise False
            # Search for
            case "s":
                print("You can search for a keyword and/or timeline, you can leave an input empty")
                print("What keyword would you like to search for?")
                print("You can combine keywords by following a word with ,")
                print("Example: (Grænland,Nuukstræti 4)")
                search = input("Search for: ")

                print("What timeline would ou like to search for?")
                print("Start                End")
                print("DD/MM/YYYY    DD/MM/YYYY")
                search_from = input("Search from: ")
                # print out a new filtered list based on keywords input
                #GoTo "Main menu > Tickets > Filtered"
                # "Main menu > Tickets > Filtered" window and commands are identical to "Main menu > Tickets"
                # Just replace the normal tickets list with the filtered one
            # Make a ticket report
            case "mr":
                create_report = input("Make a report for ticket with the ID: ")
                # If ID does not exist in the ticket list, raise error "No ticket found with that ID!"
                # If ID does not exist, cancel command
                employee = input("Employee writing report: ")
                report = input("Report: ")
                print("If applicable")
                print("If there are multiple contractors, type + to seperate them (C1 + C2 + C3)")
                id = input("ID of contractor/s hired")
                review = input("Conractor/s review: ")
                fee = float(input("Contractor/s fee: "))
                cost = float(input("Total cost: "))
            # View a ticket report
            case "vr":
                view = input("View a report for ticket with the ID: ")
                # If ID does not exist in the ticket list, raise error "No ticket found with that ID!"
                # If ID does not exist, cancel command
                # If the ticket doesnt have a report raise error "This ticket doesn't have a report!"
                # If the ticket doesn't have a report, cancel command      
                print (f"Employee: {"MISSING"}")
                print ("MISSING")
                print ("MISSING")
                print ("MISSING")
                print ("MISSING")
                print ("MISSING")
            	# print ("Employee: " + *Employee*)
                # print (*Report*)
                # print (*contractor/s hired*)
                # print (*contractor review*)
                # print (*contractor fee*)
                # print (*total coast*)
                rate = input("Rate contractor/s: ")
                respone = input("Write a response (optional): ")
                accept = input("Accept or decline (A/D): ")
                # If "A" then ticket status == "Closed"
                # If "D" then ticket status == "Needs work"
            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return self
