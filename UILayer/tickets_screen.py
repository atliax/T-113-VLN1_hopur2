from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class TicketsScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Tickets")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a ticket		[E] Edit a ticket			[B] Go back")
        print("|	[R] Remove a ticket		[S] Search for")
        print("|	[V] View closed tickets		[RV] Review a ticket report")
        print("|	[D] Ticket details")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ")

        # Add a ticket
        if cmd == "a":
            return ui_consts.TICKETMAKER
        

        # Remove a ticket
        if cmd == "r":
            remove_ticket = input("Remove ticket with ID: ")

        # Edit ticket
        if cmd == "e":
            edit_ticket = input("Edit ticket with the ID: ")
            # Go to "Main menu > Tickets > Ticket editor"

        # search
        if cmd == "s":
            search = input("Search for: ")

        # View closed tickets
        if cmd == "v":
            # go to submenu "Main menu > Tickets > Closed tickets"
            pass

        # Review
        if cmd == "rv":
            review = input("Review ticket with ID: ")
        # go to submenu "Main menu > Tickets > Review report ticket: (TICKET ID)"

        if cmd == "d":
            details = input("View ticket with ID: ")
        # Go to "Main menu > Tickets > Ticket details"

        if cmd == "b":
            return ui_consts.BACK

        return self
