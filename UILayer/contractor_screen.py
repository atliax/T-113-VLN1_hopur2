from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Contractor
from Model import Destination
from prettytable import PrettyTable

class ContractorScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Contractors")

        contractor : list[Contractor] = self.ui.logic_api.get_all_contractors()

        contractor_table = PrettyTable()
        contractor_table.field_names = ["id", "name","type","destination","contact","rating"]

        for contractor in contractor:
            contractor_destination : Destination = self.ui.logic_api.get_destination_by_ID(contractor.destinationID)
            if contractor_destination is not None:
                contractor_destination_country = contractor_destination.country
            else:
                contractor_destination_country = "Not assigned"

            contractor_table.add_row([contractor.contractorID, contractor.name, contractor.contractor_type, contractor_destination_country, contractor.contact, contractor.rating])

        contractor_table._min_table_width = ui_consts.TABLE_WIDTH
        print(contractor_table)

        destinations : list[Destination] = self.ui.logic_api.get_all_destinations()

        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID", "Country"]

        for destination in destinations:
            destination_table.add_row([destination.destinationID, destination.country])

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
            print(destination_table)

            new_destination = input("Enter destination ID for new contractor: ")
                # ID Auto generate variable = int(n + 1) then make str("C"+(variable))
            #print(f"New contractor destination ID: ") # Ekki implementað
                # If ID does not exist in destination list, raise error "No destination found with that ID!"
	            # Cancel command if destination ID is not found
            add_contractor = input("New contractor name: ")
            add_type = input("New contractor type: ")
            #add_destinationID = input("New destinationID: ")
            add_contact = input("New contractor contact (optional): ")
            add_rating = float(input("Enter rating: "))
            add_phone = int(input("New contractor phone: "))
            add_address = input("New contractor address: ")
            add_opening_hours = int(input("Add opening hours for contractor: "))
            new_contractor = Contractor(new_destination ,None ,add_rating ,add_contractor ,add_contact ,add_phone, add_address ,add_opening_hours, add_type)
            self.ui.logic_api.add_new_contractor(new_contractor)

        # Remove a contractor
        if cmd == "r":
            try:
                remove_contractor = input("Remove contractor with ID: ")
            except LookupError:
                return "No contractor found with that ID!"

        # View contact info
        if cmd == "v":
            try:
                view = input("View the contact information of contractor with the ID: ")
            except LookupError:
                return "No contractor found with that ID!"
                # If ID does not exist in the contractor list, raise error "No contractor found with that ID!"    
	            # If ID does not exist, cancel command
            print(f"Name: {add_contractor}")
            print(f"Phone: {add_phone}")
            print(f"Address: {add_address}")
        
        # Edit contractor
        if cmd == "e":
            try:
            #If nothing is input, the name/loc will be unchanged
                edit_id = input("Edit contractor with the ID: ") # Óklárað!
            except LookupError:
                return "No contractor found with that ID!"
                # If ID does not exist in the contractor list, raise error "No contractor found with that ID!"    
                # If ID does not exist, cancel command
            change_contractor = input("Change contractor name to: ")
            change_type = input("Change contractor type to: ")
            change_contact = input("Change contractor contact to: ")
            change_phone = input("Change contractor phone number: ")
            change_location = input("Change contractor address to: ")

        # Search for contractor
        if cmd == "s":
            try:
                search = input("Search for: ") # Sama search allstaðar á eftir að implementa
            except LookupError:
                return "No contractor found with that ID!"
            
        if cmd == "b":
            return ui_consts.BACK
            

