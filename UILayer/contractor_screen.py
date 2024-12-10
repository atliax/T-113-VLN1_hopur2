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

        print("Main Menu > Staff > Contractors")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a contractor		[E] Edit a contractor			[B] Go back")
        print("|	[R] Remove a contractor		[S] Search for")
        print("|	[V] View contact info")
        print("|")
        print(ui_consts.SEPERATOR)

        contractors = self.ui.logic_api.contractor_get_all()

        contractor_table = PrettyTable()
        contractor_table.field_names = ["ID", "Name","Type","Destination","Contact","Rating"]

        for contractor in contractors:
            contractor_destination = self.ui.logic_api.destination_get_by_ID(contractor.destinationID)
            if contractor_destination is not None:
                contractor_destination_country = contractor_destination.country
            else:
                contractor_destination_country = "Not assigned"

            contractor_table.add_row([contractor.ID, contractor.name, contractor.contractor_type, contractor_destination_country, contractor.contact, contractor.rating])

        contractor_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(contractors) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Contractor list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")
        if total_pages != 0:
            print(contractor_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        destinations = self.ui.logic_api.destination_get_all()

        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID", "Country"]

        for destination in destinations:
            destination_table.add_row([destination.ID, destination.country])

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
            remove_id = input("Remove contractor with the ID: ").upper()
            self.ui.logic_api.contractor_remove(remove_id)

        # View contact info
        if cmd == "v":
            contact_by_id = None
            
            while contact_by_id is None:
                view_contact = input("View the contact information of contractor with the ID: ").upper()
                
                for contractor in contractors:
                    if contractor.ID == view_contact:
                        contact_by_id = self.ui.logic_api.contractor_get_by_ID(view_contact)
                        break

                if contact_by_id is None:
                    print(f"No contractor with the ID: '{view_contact}'")

            contact_by_id_table = PrettyTable()
            contact_by_id_table.field_names = ["ID","Name","Type","Destination","Contact","rating"]
            contact_by_id_table.add_row([contact_by_id.ID,contact_by_id.name,contact_by_id.contractor_type,self.ui.logic_api.destination_get_by_ID(contact_by_id.destinationID).country,contact_by_id.contact,contact_by_id.rating])
            print(contact_by_id_table)        
                # print(contact_by_id.toJson())
            input("Command: ")

        # Edit contractor
        if cmd == "e":
            contractor_edit = None
            contractor_attributes = ["rating","name","contact","phone","opening_hours","contractor_type"]
           
            while contractor_edit is None:
                edit_with_id = input("Edit contractor with the ID: ").upper()
                #if nothing is input, the field will be left unchanged
                for contractor in contractors:
                    if contractor.ID == edit_with_id:
                        contractor_edit = contractor
                        break

                if contractor_edit is None:
                    print(f"No contractor with the ID: '{edit_with_id}' Try again (B to cancel).")

                if edit_with_id == "B":
                    return ui_consts.CMD_BACK

            print(destination_table)
            new_destinationID = input("New destination ID: ").upper()
            setattr(contractor_edit, "destinationID", new_destinationID)
            
            for attribute in contractor_attributes:
                current_value = getattr(contractor_edit, attribute)
                new_value = input(f"New {attribute.capitalize()} (Current {current_value}): ").strip()
                if new_value:
                    setattr(contractor_edit,attribute,new_value)


            self.ui.logic_api.contractor_edit(contractor_edit)
            # If ID does not exist in the employee list, raise error "No employee found with that ID!"
            # If ID does not exist, cancel command
            # If job title = "manager" or "boss" set isManager = True, otherwise False)

        # Search for contractor
        if cmd == "s":
            search = input("Search for: ") 

            search_contractor = self.ui.logic_api.contractor_search(search)
            
            search_contractor_table = PrettyTable()
            search_contractor_table.field_names = ["ID","Name","type","Country","Contact","Rating"]

            for unit in search_contractor:
                unit_destination = self.ui.logic_api.destination_get_by_ID(unit.destinationID.upper())
                if unit_destination is not None:
                    unit_destination.country = unit_destination.country
                else:
                    unit_destination.country = "Not assigned"
                search_contractor_table.add_row([unit.ID,unit.name,unit.contractor_type,unit_destination.country,unit.contact,unit.rating])
            print(search_contractor_table)
            input()


        if cmd == "b":
            return ui_consts.CMD_BACK
