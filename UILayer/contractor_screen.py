import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Contractor

class ContractorScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        print("Main menu > Contractors")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a contractor		[E] Edit a contractor			[B] Go back")
        print("|	[R] Remove a contractor		[S] Search for")
        print("|	[V] View contact info")
        print("|")
        print(ui_consts.SEPERATOR)

        contractors = self.ui.logic_api.contractor_get_all()

        contractor_table = PrettyTable()
        contractor_table.field_names = ["id", "name","type","destination","contact","rating"]

        for contractor in contractors:
            contractor_destination = self.ui.logic_api.destination_get_by_ID(contractor.destinationID)
            if contractor_destination is not None:
                contractor_destination_country = contractor_destination.country
            else:
                contractor_destination_country = "Not assigned"

            contractor_table.add_row([contractor.contractorID, contractor.name, contractor.contractor_type, contractor_destination_country, contractor.contact, contractor.rating])

        contractor_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(contractors) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Contractor list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")
        print(contractor_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        destinations = self.ui.logic_api.destination_get_all()

        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID", "Country"]

        for destination in destinations:
            destination_table.add_row([destination.destinationID, destination.country])

        if cmd == "n":
            self.current_page += 1

        if cmd == "p":
            self.current_page -= 1

        # Add a contractor
        if cmd == "a":
            print(destination_table)

            new_destination = input("Enter destination ID for new contractor: ").upper()
                # ID Auto generate variable = int(n + 1) then make str("C"+(variable))
            #print(f"New contractor destination ID: ") # Ekki implementað
                # If ID does not exist in destination list, raise error "No destination found with that ID!"
	            # Cancel command if destination ID is not found
            add_contractor = input("New contractor name: ")
            add_type = input("New contractor type: ")
            #add_destinationID = input("New destinationID: ")
            add_contact = input("New contractor contact (optional): ")
            add_rating = float(input("Enter rating: "))
            add_phone = input("New contractor phone: ")
            add_address = input("New contractor address: ")
            add_opening_hours = (input("Add opening hours for contractor: "))

            new_contractor = Contractor(None, new_destination, add_rating, add_contractor, add_contact, add_phone, add_address, add_opening_hours, add_type)

            self.ui.logic_api.contractor_add(new_contractor)

        # Remove a contractor
        if cmd == "r":
            print(contractor_table)
            remove_id = input("Remove employee with the ID: ").upper()
            self.ui.logic_api.contractor_remove(remove_id)

        # View contact info
        if cmd == "v":
            view_contact_from_id = input("View the contact information of contractor with the ID: ")
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
            try:
                search = input("Search for: ") # Sama search allstaðar á eftir að implementa
            except LookupError:
                return "No contractor found with that ID!"

        if cmd == "b":
            return ui_consts.CMD_BACK
