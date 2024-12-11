import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Property

class PropertyScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        print("Main Menu > Properties")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a property		[E] Edit a property			[B] Go back")
        print("|	[R] Remove a property		[S] Search for")
        print("|	[V] View facilities")
        print("|")
        print(ui_consts.SEPERATOR)

        all_properties = self.ui.logic_api.property_get_all()

        all_properties_table = PrettyTable()
        all_properties_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]

        for property in all_properties:
            property_destination = self.ui.logic_api.destination_get_by_ID(property.destinationID.upper())

            if property_destination is not None:
                property_destination_country = property_destination.country
            else:
                property_destination_country = "Not assigned"

            all_properties_table.add_row([property.ID, property.name, property_destination_country, property.address, property.square_meters, property.rooms, property.type])

        all_properties_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(all_properties) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Property list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if total_pages != 0:
            print(all_properties_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        # construct a table of destinations for use with the "add" and "edit" commands
        destinations = self.ui.logic_api.destination_get_all()
        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID","Country","Airport"]
        for destination in destinations:
            destination_table.add_row([destination.ID, destination.country, destination.airport])

        match cmd:
            case "n":
                self.current_page += 1
            case "p":
                self.current_page -= 1
            # [A] Add a property
            case "a":
                # First present the available destinations
                print(destination_table)

                # Get new property details from user
                p_new_name = input("New property name: ")
                p_new_destination = input("New property destionation ID: ")
                p_new_address = input("New property address: ")
                p_new_square_mtrs = (input("New property square meters: "))
                p_new_roomnum = (input("New property number of rooms: "))
                p_new_type = input("New property type: ")

                # construct property
                new_property = Property(None, p_new_destination, p_new_name, p_new_address, p_new_square_mtrs, p_new_roomnum, p_new_type)

                # Send property to logic api
                self.ui.logic_api.property_add(new_property)
            # [R] Remove a property
            case "r":
                remove_id = input("Remove a property that has the ID: ").upper()
                self.ui.logic_api.property_remove(remove_id)
            # [V] View facilities
            case "v":
                # If ID does not exist in property list, raise error "No property found with that ID!"
                # If ID does not exist, cancel command	
                property_ID = input("View the facilities in property with ID: ").upper()
                check = self.ui.logic_api.property_get_by_ID(property_ID)
                if check is not None:
                    self.ui.logic_api.facility_set_selected_property(property_ID)
                    return ui_consts.FACILITY_SCREEN
                else:
                    print(f"No property with ID '{property_ID}' exists.")
                    input("Press enter to continue.")
            # [E] Edit a property 
            case "e":
                property_edit = None
                property_attributes = ["destinationID","name","address","square_meters","rooms", "type"]

                while property_edit is None:
                    edit_with_id = input("Edit property with the ID: ").upper()

                    property_edit = self.ui.logic_api.property_get_by_ID(edit_with_id)

                    if property_edit is None:
                        print(f"No property with the ID: '{edit_with_id}' Try again (B to cancel).")

                    if edit_with_id == "B":
                        return ui_consts.CMD_BACK

                # First present the available destinations
                print(destination_table)

                # Then get the new data from the user
                # if nothing is input, the field will be left unchanged
                for attribute in property_attributes:
                    current_value = getattr(property_edit, attribute)
                    new_value = input(f"New {attribute.capitalize()} (Current {current_value}): ").strip()
                    if new_value:
                        setattr(property_edit,attribute,new_value)

                self.ui.logic_api.property_edit(property_edit)
            # [S] Search for
            case "s":
                search = input("Search for: ") 
            
                search_property = self.ui.logic_api.property_search(search)

                search_property_table = PrettyTable()
                search_property_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]

                for property in search_property:
                    unit_destination = self.ui.logic_api.destination_get_by_ID(property.destinationID.upper())

                    if unit_destination is not None:
                        unit_destination_country = unit_destination.country
                    else:
                        unit_destination_country = "Not assigned"

                    search_property_table.add_row([property.ID, property.name, unit_destination_country, property.address, property.square_meters, property.rooms, property.type])

                print(search_property_table) 
                input("Press enter to continue.")
            # [B] Go Back
            case "b":
                return ui_consts.CMD_BACK

        return self
