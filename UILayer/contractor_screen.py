import math

from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

from Model import Contractor

class ContractorScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self):
        self.clear_screen()

        print("Main Menu > Staff > Contractors")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.ui.logic_api.is_manager_logged_in():
            print("|	[A] Add a contractor		[E] Edit a contractor			[B] Go back")
            print("|	[R] Remove a contractor		[S] Search for")
            print("|	[V] View contact info")
        else:
            print_formatted_text(HTML("|	<s>[A] Add a contractor</s>		<s>[E] Edit a contractor</s>			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove a contractor</s>		[S] Search for"))
            print_formatted_text(HTML("|	[V] View contact info"))

        print("|")
        print(ui_consts.SEPERATOR)

        try:
            if self.active_search_filter:
                contractor_list = self.ui.logic_api.contractor_search(self.active_search_filter)
            else:
                contractor_list = self.ui.logic_api.contractor_get_all()
        except Exception as e:
            print(f"Error getting contractors: {type(e).__name__}: {e}")
            print("Could not load contractor list. Try again.")
            input("Press enter to go back.")
            return ui_consts.CMD_BACK
        
        contractor_table = PrettyTable()
        contractor_table.field_names = ["ID", "Name","Type","Destination","Contact","Rating","Opening hours"]

        for contractor in contractor_list:
            try:
                contractor_destination = self.ui.logic_api.destination_get_by_ID(contractor.destinationID)
            except Exception as e:
                print(f"Error loading destination data for contractor '{contractor.ID}': {type(e).__name__}: {e}")
                print("Error displaying contractor details.")
                input("Press enter to go back.")
                return ui_consts.CMD_BACK

            if contractor_destination is not None:
                contractor_destination_country = contractor_destination.country
            else:
                contractor_destination_country = "Not assigned"

            contractor_table.add_row([contractor.ID, contractor.name, contractor.contractor_type, contractor_destination_country, contractor.contact, contractor.rating, contractor.opening_hours])

        contractor_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(contractor_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Contractor list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(contractor_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("No contractors found.")

        print("")
        cmd = input("Command: ").lower()

        try:
            all_destinations = self.ui.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destination data: {type(e).__name__}: {e}")
            print("Could not load destinations. Try again.")
            input("Press enter to go back.")
            return ui_consts.CMD_BACK
        
        all_destinations_table = PrettyTable()
        all_destinations_table.field_names = ["Destination ID", "Country"]

        for destination in all_destinations:
            all_destinations_table.add_row([destination.ID, destination.country])

        match cmd:
            # Next page
            case "n":
                self.current_page += 1
            # Previous page
            case "p":
                self.current_page -= 1
            # Add a contractor
            case "a":
                if self.ui.logic_api.is_manager_logged_in():
                    print(all_destinations_table)

                    while True:
                        try:
                            new_destination = input("Enter destination ID for new employee (B to cancel): ").upper()
                            
                            if new_destination == "B":
                                return self 

                            
                            if not self.ui.logic_api.destination_get_by_ID(new_destination):
                                raise ValueError(f"No destination found with the ID: '{new_destination}'")
                            break  

                        except ValueError as e:
                            print(e)
                            print("Please try again or type 'B' to go back.")
                    # If ID does not exist in destination list, raise error "No destination found with that ID!"
                    # Cancel command if destination ID is not found
                    add_contractor = input("New contractor name: ")
                    add_type = input("New contractor type: ")
                    add_rating = 0.0
                    add_contact = input("New contractor contact (optional): ")
                    add_phone = input("New contractor phone number: ").replace(" ", "").replace("-", "")
                    while not (add_phone.startswith("+") and add_phone[1:].isdigit() or add_phone.isdigit()):
                        print("Phone number must contain only numbers or start with a single '+' followed by numbers.")
                        add_phone = input("New contractor phone number: ").replace(" ", "").replace("-", "")

                    add_address = input("New contractor address: ")
                    add_opening_hours = (input("Add opening hours for contractor: "))

                    new_contractor = Contractor(None, new_destination, add_rating, add_contractor, add_contact, add_phone, add_address, add_opening_hours, add_type)
                    try:
                        self.ui.logic_api.contractor_add(new_contractor)
                    except Exception as e:
                        print(f"Error adding contractor: {type(e).__name__}: {e}")
                        print("Could not add contractor. Please try again.")
                        input("Press enter to continue.")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # Remove a contractor
            case "r":
                if self.ui.logic_api.is_manager_logged_in():
                    remove_id = input("Remove contractor with the ID: ").upper()

                    try:
                        self.ui.logic_api.contractor_remove(remove_id)
                    except Exception as e:
                        print(f"Error removing contractor: {type(e).__name__}: {e}")
                        print("Could not remove contractor. Try again.")
                        input("Press enter to continue: ")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # View contact info
            case "v":
                contact_by_id = None

                while contact_by_id is None:
                    view_contact = input("View the contact information of contractor with the ID: ").upper()
                    try:
                        contact_by_id = self.ui.logic_api.contractor_get_by_ID(view_contact)
                    except Exception as e:
                        print(f"Error loading contractor info: {type(e).__name__}: {e}")
                        print("Could not load contractor information. Try again.")
                        input("Press enter to continue.")
                        return self

                    if contact_by_id is None:
                        print(f"No contractor with the ID: '{view_contact}', try again (B to cancel).")

                    if view_contact == "B":
                        return self

                contact_by_id_table = PrettyTable()
                contact_by_id_table.field_names = ["ID", "Name", "Phone", "Address", "Rating"]
                contact_by_id_table.add_row([contact_by_id.ID,contact_by_id.name,contact_by_id.phone,contact_by_id.address,contact_by_id.rating])
                print(contact_by_id_table)
                input("Press enter to continue.")
            # Edit contractor
            case "e":
                if self.ui.logic_api.is_manager_logged_in():
                    contractor_edit = None

                    while contractor_edit is None:
                        edit_with_id = input("Edit contractor with the ID: ").upper()

                        try:
                            contractor_edit = self.ui.logic_api.contractor_get_by_ID(edit_with_id)

                        except Exception as e:
                            print(f"Error loading contractor info: {type(e).__name__}: {e}")
                            print("Could not load contractor information. Try again.")
                            input("Press enter to continue.")
                            return self

                        if contractor_edit is None:
                            print(f"No contractor with the ID: '{edit_with_id}' Try again (B to cancel).")

                        if edit_with_id == "B":
                            return self

                    print(all_destinations_table)

                    while True:
                        try:
                            new_destinationID = input("Enter destination ID for contractor (B to go cancel): ").upper()
                            
                            if new_destinationID == "B":
                                return self  

                            if not self.ui.logic_api.destination_get_by_ID(new_destinationID):
                                raise ValueError(f"No destination found with the ID: '{new_destinationID}'")
                            break  

                        except ValueError as e:
                            print(e)
                            print("Please try again or type 'B' to go back.")

                    setattr(contractor_edit, "destinationID", new_destinationID)
                    print("Leave empty if you dont want to change.")

                    contractor_attributes = ["name","contact","phone","address","opening_hours","contractor_type"]

                    for attribute in contractor_attributes:
                        current_value = getattr(contractor_edit, attribute)
                        
                        new_value = input(f"New {attribute.capitalize()} (Current {current_value}): ").strip()
                        if not new_value:
                            continue

                        if attribute in ["phone"]:
                            while not ((new_value.startswith('+') and new_value[1:].isdigit()) or new_value.isdigit()):
                                print("Phone number must contain only numbers or start with a single '+' followed by numbers.")
                                new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()

                        setattr(contractor_edit, attribute, new_value)

                    try:
                        self.ui.logic_api.contractor_edit(contractor_edit)
                    except Exception as e:
                        print(f"Error editing contractor: {type(e).__name__}: {e}")
                        print("Could not edit contractor. Try again.")
                        input("Press enter to continue.")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # Search for contractor
            case "s":
                self.active_search_filter = input("Search for: ")
            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return self
