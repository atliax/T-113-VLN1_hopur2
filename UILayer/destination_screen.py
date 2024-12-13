# standard library imports
import math
from textwrap import fill

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Destination

class DestinationScreen(BaseScreen):
    """
    Screen class to manage destination related options, like adding
    viewing and editing destinations
    """
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1

    def run(self) -> str | None:
        """
        Main method to display destination screen 
        and handle user commands
        """
        self.clear_screen()

        print("Main Menu > Destinations")

        print(ui_consts.SEPERATOR)
        print("|")

        # Display options based on user permissions
        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        else:
            print_formatted_text(HTML("|	<s>[A] Add a destination</s>		<s>[E] Edit a destination</s>			[B] Go back"))

        print("|")
        print(ui_consts.SEPERATOR)

        # Fetch a list of all available destinations, handling errors
        try:
            all_destinations = self.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destinations:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        # Calculate total pages and make sure current page is within valid bounds
        total_pages = math.ceil(len(all_destinations) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        # Set up destination table
        destination_table = PrettyTable()
        destination_table.field_names = ["ID", "Destination","Airport", "Opening hours", "Phone", "Manager"]
        destination_table._min_table_width = ui_consts.TABLE_WIDTH

        for destination in all_destinations:
            try:
                # Fetch manager information for the destination
                destinanation_manager = self.logic_api.staff_get_by_ID(destination.managerID)
            except Exception as e:
                print(f"Error loading info for manager '{destination.managerID}' in destination '{destination.ID}':")
                print(f"{type(e).__name__}: {e}")
                input(ui_consts.MSG_ENTER_BACK)
                return ui_consts.CMD_BACK

            # Assign "Needs Manager" if no manager is assigned
            if destinanation_manager is None:
                manager_name = "Needs manager"
            else:
                manager_name = destinanation_manager.name

            # Add destination data to the table
            destination_table.add_row([destination.ID, destination.country, destination.airport, destination.opening_hours, destination.phone, manager_name])


        # Display destination data with nagivation for paging
        print(f"|  Destination list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if total_pages != 0:
            print(destination_table.get_string(start=self.current_page * 10, end=(self.current_page + 1) * 10))
        else:
            print("")
            print("No destinations found.")

        print("")
        cmd = input("Command: ").lower()

        # Handle user commands
        match cmd:
            # Next page
            case "n":
                self.current_page += 1

            # Previous page
            case "p":
                self.current_page -= 1

            # Add a destination
            case "a": 
                if self.logic_api.is_manager_logged_in():
                    # Collect input for the new destination attributes
                    new_destination_attributes = ["country", "airport", "phone", "opening_hours"]

                    new_destination_data = []
                    for attribute in new_destination_attributes:
                        # Required fields can not be left empty
                        while (new_value := input(f"New {attribute}: ")) == "":
                            print(f"Field '{attribute}' can't be empty.")

                        # Validate phone number input
                        if attribute == "phone":
                            check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")
                            while not check_phone.isdigit():
                                print(ui_consts.MSG_INVALID_PHONE)
                                new_value = input(f"New {attribute}: ")
                                check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")

                        new_destination_data.append(new_value)

                    # Create a new destination object
                    new_destination = Destination(None, None, new_destination_data[0], new_destination_data[1], new_destination_data[2], new_destination_data[3])

                    # Add destination to database
                    try:
                        self.logic_api.destination_add(new_destination)
                    except Exception as e:
                        print(f"Error adding new destination:")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    print("New destination added successfully.")
                    print("Please navigate to the staff menu and add a manager for this location.")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Edit destination
            case "e":
            
                if self.logic_api.is_manager_logged_in():
                    destination_edit = None
                    edit_destination_attributes = ["country", "airport", "phone", "opening_hours"]

                    while destination_edit is None:
                        edit_destination_ID = input("Enter the ID of the destination you want to edit (B to return): ").upper()

                        if edit_destination_ID == "B":
                            return None

                        try:
                            # Get destination details
                            destination_edit = self.logic_api.destination_get_by_ID(edit_destination_ID)
                        except Exception as e:
                            print(f"Error loading destination '{edit_destination_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None

                        if destination_edit is None:
                            print(f"Destination '{edit_destination_ID}' not found, try again.")
                            input(ui_consts.MSG_ENTER_CONTINUE)

                    print("Enter new data for the destination, leave the field empty to keep the previous data.")

                    # Display available managers
                    print("\nAvailable Managers:")
                    managers = self.logic_api.staff_list_managers()

                    table = PrettyTable()
                    table.field_names = ["Manager ID", "Name"]
                    for manager in managers:
                        table.add_row([manager.ID, manager.name])
                    print(table)

                    new_manager_id = input("Enter new Manager ID (B to cancel): ").upper().strip()
                    if new_manager_id == "B":
                        return None

                    # Prompt for manager ID and make sure it is valid
                    manager_ids = [manager.ID for manager in managers]
                    while new_manager_id not in manager_ids:
                        print(f"Invalid manager ID: {new_manager_id}. Please provide a valid manager ID. (B to cancel)")
                        new_manager_id = input("Enter new Manager ID: ").strip().upper()
                        if new_manager_id == "B":
                            return None

                    setattr(destination_edit, "managerID", new_manager_id)

                    # Collect and validate new data for editable attributes
                    for attribute in edit_destination_attributes:
                        current_value = getattr(destination_edit, attribute)
                        new_value = input(f"New {attribute} (current: {current_value}): ").strip()

                        if attribute == "phone" and new_value:
                            check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")
                            while not check_phone.isdigit():
                                print(ui_consts.MSG_INVALID_PHONE)
                                new_value = input(f"New {attribute} (current: {current_value}): ").strip()
                                check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")

                        if new_value:
                            setattr(destination_edit, attribute, new_value)

                    # Save the updated destination
                    try:
                        self.logic_api.destination_edit(destination_edit)
                    except Exception as e:
                        print(f"Error editing destination '{edit_destination_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                    print("Destination updated successfully.")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return None
