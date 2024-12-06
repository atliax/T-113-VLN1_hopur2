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

        # View contact info
        if cmd == "v":
            view = input("View the contact information of contractor with the ID: ")
                # If ID does not exist in the contractor list, raise error "No contractor found with that ID!"    
	            # If ID does not exist, cancel command
            print(f"Name: {add_contractor}")
            print(f"Phone: {add_phone}")
            print(f"Address: {add_address}")
        
        # Edit contractor
        if cmd == "e":
            #If nothing is input, the name/loc will be unchanged
            edit_id = input("Edit contractor with the ID: ") # Óklárað!
                # If ID does not exist in the contractor list, raise error "No contractor found with that ID!"    
                # If ID does not exist, cancel command
            change_contractor = input("Change contractor name to: ")
            change_type = input("Change contractor type to: ")
            change_contact = input("Change contractor contact to: ")
            change_phone = input("Change contractor phone number: ")
            change_location = input("Change contractor address to: ")

        # Search for contractor
        if cmd == "s":
            search = input("Search for: ") # Sama search allstaðar á eftir að implementa

        if cmd == "b":
            return ui_consts.BACK
            

