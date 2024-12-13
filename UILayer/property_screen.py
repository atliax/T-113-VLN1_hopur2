# standard library imports
import math
from textwrap import fill

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Property

class PropertyScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self) -> str | None:
        self.clear_screen()

        print("Main Menu > Properties")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
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
                property_list = self.logic_api.property_search(self.active_search_filter)
            else:
                property_list = self.logic_api.property_get_all()
        except Exception as e:
            print(f"Error loading properties:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        total_pages = math.ceil(len(property_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        property_table = PrettyTable()
        property_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]
        property_table._min_table_width = ui_consts.TABLE_WIDTH

        for property in property_list:
            try:
                property_destination = self.logic_api.destination_get_by_ID(property.destinationID)
            except Exception as e:
                print(f"Error loading destination '{property.destinationID}' for property '{property.ID}':")
                print(f"{type(e).__name__}: {e}")
                input(ui_consts.MSG_ENTER_BACK)
                return ui_consts.CMD_BACK

            if property_destination is not None:
                property_destination_country = property_destination.country
            else:
                property_destination_country = "Not assigned"

            property_table.add_row([property.ID, fill(property.name, width=18), fill(property_destination_country, width=18), fill(property.address, width=32), property.square_meters, property.rooms, fill(property.type, width=12)])

        print(f"|  Property list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(property_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("")
            print("No properties found.")

        print("")
        cmd = input("Command: ").lower()

        # construct a table of destinations for use with the "add" and "edit" commands
        try:
            destinations = self.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destinations:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK
        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID","Country","Airport"]
        for destination in destinations:
            destination_table.add_row([destination.ID, destination.country, destination.airport])

        match cmd:

            # Next page
            case "n":
                self.current_page += 1

            # Previous page
            case "p":
                self.current_page -= 1

            # Add a property
            case "a":
                if self.logic_api.is_manager_logged_in():
                    # First present the available destinations
                    print(destination_table)

                    # Get new property details from user
                    new_destination_ID_prompt = "Enter a destination ID for new property (B to go cancel): "

                    try:
                        while not self.logic_api.destination_get_by_ID(new_destination_ID := input(new_destination_ID_prompt).upper()):
                            if new_destination_ID == "B":
                                return None
                            print(f"No destination found with the ID: {new_destination_ID}")
                    except Exception as e:
                        print(f"Error loading destination '{new_destination_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    while (new_property_name := input("New property name: ")) == "":
                        print("Property name can't be empty.")

                    while (new_property_address := input("New property address: ")) == "":
                        print("Property address can't be empty.")

                    valid_integer = False
                    while not valid_integer:
                        try:
                            new_property_square_meters = int(input("New property square meters: "))
                            if new_property_square_meters >= 0:
                                valid_integer = True
                            else:
                                raise ValueError
                        except ValueError:
                            print("Please enter a valid integer.")

                    valid_integer = False
                    while not valid_integer:
                        try:
                            new_property_room_count = int(input("New property number of rooms: "))
                            if new_property_room_count >= 0:
                                valid_integer = True
                            else:
                                raise ValueError
                        except ValueError:
                            print("Please enter a valid integer.")

                    while (new_property_type := input("New property type: ")) == "":
                        print("Property type can't be empty.")

                    # construct property instance
                    new_property = Property(None, new_destination_ID, new_property_name, new_property_address, new_property_square_meters, new_property_room_count, new_property_type)

                    # Send the freshly constructed property down to logic api
                    try:
                        self.logic_api.property_add(new_property)
                    except Exception as e:
                        print(f"Error adding new property '{new_property.name}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # [R] Remove a property
            case "r":
                if self.logic_api.is_manager_logged_in():
                    remove_id = input("Remove a property that has the ID: ").upper()

                    if input(f"Are you sure you want to remove property '{remove_id}' (Y to confirm)? ").upper() != "Y":
                        return None

                    try:
                        self.logic_api.property_remove(remove_id)
                    except Exception as e:
                        print(f"Error removing property '{remove_id}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # [V] View facilities
            case "v":
                property_ID = input("View the facilities in property with ID: ").upper()

                try:
                    check = self.logic_api.property_get_by_ID(property_ID)
                except Exception as e:
                    print(f"Error loading data for property '{property_ID}':")
                    print(f"{type(e).__name__}: {e}")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

                if check is None:
                    print(f"No property with ID '{property_ID}' exists.")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None
                else:
                    self.logic_api.facility_set_selected_property(property_ID)
                    return ui_consts.FACILITY_SCREEN

            # [E] Edit a property 
            case "e":
                if self.logic_api.is_manager_logged_in():
                    property_edit = None

                    while property_edit is None:
                        property_edit_ID = input("Edit property with the ID (B to cancel): ").upper()

                        if property_edit_ID == "B":
                            return None

                        try:
                            property_edit = self.logic_api.property_get_by_ID(property_edit_ID)
                        except Exception as e:
                            print(f"Error loading data for property '{property_edit_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            continue

                        if property_edit is None:
                            print(f"No property found with the ID: '{property_edit_ID}'.")

                    # First present the available destinations
                    print(destination_table)

                    # Then ask the user to enter a new destination
                    new_destinationID_prompt = "Enter new destination ID for the property (B to cancel): "
                    try:
                        while not self.logic_api.destination_get_by_ID(new_destinationID := input(new_destinationID_prompt).upper()):
                            if new_destinationID == "B":
                                return None
                            print(f"No destination found with the ID: '{new_destinationID}'.")
                    except Exception as e:
                        print(f"Error loading destination '{new_destinationID}' while editing property '{property_edit_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    setattr(property_edit, "destinationID", new_destinationID)

                    print("Enter new data for the property, leave the field empty to keep the previous data.")

                    editable_attributes = ["name","address","square_meters","rooms", "type"]
                    for attribute in editable_attributes:
                        current_value = getattr(property_edit, attribute)
                        new_value = input(f"New {attribute.capitalize()}( Current {current_value}): ").strip()

                        if new_value:
                            if attribute == "square_meters" or attribute == "rooms":
                                valid_integer = False
                                while not valid_integer:
                                    try:
                                        new_value = int(new_value)
                                        if new_value >= 0:
                                            valid_integer = True
                                        else:
                                            raise ValueError
                                    except ValueError:
                                        print("Please enter a valid integer.")
                                        new_value = input(f"New {attribute.capitalize()}( Current {current_value}): ").strip()

                            setattr(property_edit, attribute, new_value)

                    try:
                        self.logic_api.property_edit(property_edit)
                    except Exception as e:
                        print(f"Error editing property '{property_edit_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # [S] Search for
            case "s":
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)
                return None

            # [B] Go Back
            case "b":
                return ui_consts.CMD_BACK

        return None
