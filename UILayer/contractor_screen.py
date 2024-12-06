from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class ContractorScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Contractors")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a contractor		[E] Edit a contractor			[B] Go back")
        print("|	[R] Remove a contractor		[S] Search for")
        print("|	[V] View contact info")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add a contractor
        if cmd == "a":
                # ID Auto generate variable = int(n + 1) then make str("C"+(variable))
            print(f"New contractor destination ID: ")
                # If ID does not exist in destination list, raise error "No destination found with that ID!"
	            # Cancel command if destination ID is not found
            add_contractor = input("New contractor name: ")
            add_type = input("New contractor type: ")
            add_contact = input("New contractor contact (optional): ")
            add_phone = int(input("New contractor phone: "))
            add_address = input("New contractor address: ")

        # Remove a contractor
        if cmd == "r":
            rm_contractor = input("Remove contractor with ID: ")
        
        # Edit contractor
        if cmd == "e":
            #If nothing is input, the name/loc will be unchanged
            change_contractor = input("Change contractor name to: ")
            change_phone = input("Change contractor phone number: ")
            change_email = input("Change contractor email to: ")
            change_title = input("Change contractor type to: ")
            change_location = input("Change contractor location to: ")

        # Search for contractor
        if cmd == "s":
            search = input("Search for: ")
        
        if cmd == "rv":
            contractor_id = input("Rate contractor with ID: ")
            rating = input("Rating: (0.00 - 10.00): ")

        if cmd == "b":
            return ui_consts.BACK
            

