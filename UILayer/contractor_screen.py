from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class ContractorScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Contractors")


        cmd = input("Command: ")

        # Add a contractor
        if cmd == "a":
            add_contractor = input("New contractor name: ")
            add_phone = input("New contractor phone: ")
            add_ssn = input("New contractor personal or company SSN: ")
            add_type = input("New contractor type: ")
            add_location = input("New contractor location: ")

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
            

