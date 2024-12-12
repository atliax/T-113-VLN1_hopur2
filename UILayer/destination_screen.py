import math

from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

from Model import Destination

class DestinationScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        print("Main Menu > Destinations")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        else:
            print_formatted_text(HTML("|	<s>[A] Add a destination</s>		<s>[E] Edit a destination</s>			[B] Go back"))

        print("|")
        print(ui_consts.SEPERATOR)

        try:
            all_destinations = self.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destinations:")
            print(f"{type(e).__name__}: {e}")
            input("Press enter to go back.")
            return ui_consts.CMD_BACK

        total_pages = math.ceil(len(all_destinations) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        destination_table = PrettyTable()
        destination_table.field_names = ["ID", "Destination","Airport", "Opening hours", "Phone", "Manager"]
        destination_table._min_table_width = ui_consts.TABLE_WIDTH

        for destination in all_destinations:
            try:
                destinanation_manager = self.logic_api.staff_get_by_ID(destination.managerID)
            except Exception as e:
                print(f"Error loading info for manager '{destination.managerID}' in destination '{destination.ID}':")
                print(f"{type(e).__name__}: {e}")
                input("Press enter to go back.")
                return ui_consts.CMD_BACK

            if destinanation_manager is None:
                manager_name = "Needs manager"
            else:
                manager_name = destinanation_manager.name

            destination_table.add_row([destination.ID, destination.country, destination.airport, destination.opening_hours, destination.phone, manager_name])

        print(f"|  Destination list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if total_pages != 0:
            print(destination_table.get_string(start=self.current_page * 10, end=(self.current_page + 1) * 10))

        print("")
        cmd = input("Command: ").lower()

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
                    destination_attributes = ["country", "airport", "phone", "opening_hours"]

                    new_destination = []
                    for attribute in destination_attributes:
                        new_value = input(f"New {attribute}: ")

                        if attribute == "phone":
                            check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")
                            while not check_phone.isdigit():
                                print("Phone number must contain only '+', '-', ' ' and numbers.")
                                new_value = input(f"New {attribute}: ")
                                check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")

                        new_destination.append(new_value)

                    tmp = Destination(None, new_destination[0], new_destination[1], new_destination[2], new_destination[3], None)

                    try:
                        self.logic_api.destination_add(tmp)
                    except Exception as e:
                        print(f"Error adding new destination:")
                        print(f"{type(e).__name__}: {e}")
                        input("Press enter to continue.")
                        return self

                    print("New destination added successfully.")
                    print("Please navigate to the staff menu and add a manager for this location.")
                    input("Press enter to continue.")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")

            # Edit destination
            case "e":
                if self.logic_api.is_manager_logged_in():
                    destination_edit = None
                    destination_attributes = ["managerID", "country", "airport", "phone", "opening_hours"]

                    while destination_edit is None:
                        pick_destination = input("Type in the ID of the destination you want to edit (B to return): ").upper()

                        if pick_destination == "B":
                            return self

                        try:
                            destination_edit = self.logic_api.destination_get_by_ID(pick_destination)
                        except Exception as e:
                            print(f"Error loading destination '{pick_destination}':")
                            print(f"{type(e).__name__}: {e}")
                            input("Press enter to continue.")
                            return self

                        if destination_edit is None:
                            print(f"Destination '{pick_destination}' not found, try again.")
                            input("Press enter to continue.")

                    print("Leave empty if you wish to not change.")
                    for attribute in destination_attributes:
                        current_value = getattr(destination_edit, attribute)
                        new_value = input(f"New {attribute} (current: {current_value}): ").upper().strip()

                        if attribute == "managerID" and new_value:
                            manager_ids = [manager.ID for manager in self.logic_api.staff_list_managers()]
                            while new_value not in manager_ids:
                                print(f"Invalid manager ID: {new_value}. Please provide a valid manager ID. (B to cancel) ")
                                new_value = input(f"New {attribute} (current: {current_value}): ").strip().upper()
                                if new_value == "B":
                                    return self
                        elif attribute == "phone" and new_value:
                            check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")
                            while not check_phone.isdigit():
                                print("Phone number must contain only '+', '-', ' ' and numbers.")
                                new_value = input(f"New {attribute} (current: {current_value}): ").strip()
                                check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")

                        if new_value:
                            setattr(destination_edit, attribute, new_value)

                    try:
                        self.logic_api.destination_edit(destination_edit)
                        print("Destination updated successfully.")
                        input("Press enter to continue.")
                    except Exception as e:
                        print(f"Error editing destination '{pick_destination}':")
                        print(f"{type(e).__name__}: {e}")
                        input("Press enter to continue.")
                        return self
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return self
