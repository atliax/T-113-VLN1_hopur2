import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Property

from prompt_toolkit import print_formatted_text, HTML

class PropertyScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self):
        self.clear_screen()

        print("Main Menu > Properties")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.ui.logic_api.is_manager_logged_in():
            print("|	[A] Add a property		[E] Edit a property			[B] Go back")
            print("|	[R] Remove a property		[S] Search for")
            print("|	[V] View facilities")
        else:
            print_formatted_text(HTML("|	<s>[A] Add a property</s>		<s>[E] Edit a property</s>			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove a property</s>		[S] Search for"))
            print_formatted_text("|	[V] View facilities")

        print("|")
        print(ui_consts.SEPERATOR)

        try:
            if self.active_search_filter:
                property_list = self.ui.logic_api.property_search(self.active_search_filter)
            else:
                property_list = self.ui.logic_api.property_get_all()
        except Exception as e:
            print(f"Error loading properties:")
            print(f"{type(e).__name__}: {e}")
            input("Press enter to go back.")
            return ui_consts.CMD_BACK

        property_table = PrettyTable()
        property_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]

        for property in property_list:
            try:
                property_destination = self.ui.logic_api.destination_get_by_ID(property.destinationID)
            except Exception as e:
                print(f"Error loading destination '{property.destinationID}' for property '{property.ID}':")
                print(f"{type(e).__name__}: {e}")
                input("Press enter to go back.")
                return ui_consts.CMD_BACK

            if property_destination is not None:
                property_destination_country = property_destination.country
            else:
                property_destination_country = "Not assigned"

            property_table.add_row([property.ID, property.name, property_destination_country, property.address, property.square_meters, property.rooms, property.type])

        property_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(property_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Property list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(property_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

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
                if self.ui.logic_api.is_manager_logged_in():
                    # First present the available destinations
                    print(destination_table)

                    # Get new property details from user
                    p_new_name = input("New property name: ")

                    input_prompt = "Enter a destination ID for new property (B to go cancel): "
                    try:
                        while not self.ui.logic_api.destination_get_by_ID(p_new_destination := input(input_prompt).upper()):
                            if p_new_destination == "B":
                                return self
                            print(f"No destination found with the ID: {p_new_destination}")
                    except Exception as e:
                        print(f"Error loading destination '{p_new_destination}' for new property '{p_new_name}':")
                        print(f"{type(e).__name__}: {e}")
                        input("Press enter to continue.")
                        return self

                    p_new_address = input("New property address: ")
                    p_new_square_mtrs = (input("New property square meters: "))
                    p_new_roomnum = (input("New property number of rooms: "))
                    p_new_type = input("New property type: ")

                    # construct property
                    new_property = Property(None, p_new_destination, p_new_name, p_new_address, p_new_square_mtrs, p_new_roomnum, p_new_type)

                    # Send property to logic api
                    try:
                        self.ui.logic_api.property_add(new_property)
                    except Exception as e:
                        print(f"Error adding new property '{new_property.name}':")
                        print(f"{type(e).__name__}: {e}")
                        input("Press enter to continue.")
                        return self
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # [R] Remove a property
            case "r":
                if self.ui.logic_api.is_manager_logged_in():
                    remove_id = input("Remove a property that has the ID: ").upper()
                    try:
                        self.ui.logic_api.property_remove(remove_id)
                    except Exception as e:
                        print(f"Error removing property '{remove_id}':")
                        print(f"{type(e).__name__}: {e}")
                        input("Press enter to continue: ")
                        return self
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
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
                if self.ui.logic_api.is_manager_logged_in():
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
                    
                    while True:
                        try:
                            new_destinationID = input("Enter destination ID for employee (B to go back): ").upper()
                            
                            if new_destinationID == "B":
                                return ui_consts.CMD_BACK  

                            
                            if not self.ui.logic_api.destination_get_by_ID(new_destinationID):
                                raise ValueError(f"No destination found with the ID: '{new_destinationID}'")
                            break  

                        except ValueError as e:
                            print(e)
                            print("Please try again (B to cancel).")

                    # Then get the new data from the user
                    # if nothing is input, the field will be left unchanged
                    for attribute in property_attributes:
                        current_value = getattr(property_edit, attribute)
                        new_value = input(f"New {attribute.capitalize()}( Current {current_value}): ").strip()
                        
                        if new_value:
                            setattr(property_edit,attribute,new_value)

                    self.ui.logic_api.property_edit(property_edit)
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # [S] Search for
            case "s":
                self.active_search_filter = input("Search for: ") 
            # [B] Go Back
            case "b":
                return ui_consts.CMD_BACK

        return self
