# standard library imports
import math
from textwrap import fill

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Contractor

class ContractorScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self) -> str | None:
        self.clear_screen()

        print("Main Menu > Staff > Contractors")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
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
                contractor_list = self.logic_api.contractor_search(self.active_search_filter)
            else:
                contractor_list = self.logic_api.contractor_get_all()
        except Exception as e:
            print(f"Error loading contractor list:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        total_pages = math.ceil(len(contractor_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        contractor_table = PrettyTable()
        contractor_table.field_names = ["ID", "Name","Type","Destination","Contact","Rating","Opening hours"]
        contractor_table._min_table_width = ui_consts.TABLE_WIDTH

        for contractor in contractor_list:
            try:
                contractor_destination = self.logic_api.destination_get_by_ID(contractor.destinationID)
            except Exception as e:
                print(f"Error loading destination data for contractor '{contractor.ID}':")
                print(f"{type(e).__name__}: {e}")
                input(ui_consts.MSG_ENTER_BACK)
                return ui_consts.CMD_BACK

            if contractor_destination is not None:
                contractor_destination_country = contractor_destination.country
            else:
                contractor_destination_country = "Not assigned"

            contractor_table.add_row([contractor.ID, fill(contractor.name,width=20), contractor.contractor_type, contractor_destination_country, contractor.contact, contractor.rating, contractor.opening_hours])

        print(f"|  Contractor list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(contractor_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("")
            print("No contractors found.")

        print("")
        cmd = input("Command: ").lower()

        try:
            all_destinations = self.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destination data:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
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
                if self.logic_api.is_manager_logged_in():
                    print(all_destinations_table)

                    new_destinationID_prompt = "Enter destination ID for new contractor (B to cancel): "
                    try:
                        while not self.logic_api.destination_get_by_ID(new_destinationID := input(new_destinationID_prompt).upper()):
                            if new_destinationID == "B":
                                return None
                            print(f"No destination found with the ID: '{new_destinationID}'")
                    except Exception as e:
                        print(f"Error loading destination '{new_destinationID}' for new contractor:")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    while (new_name := input("New contractor name: ")) == "":
                        print("Contractor name can't be empty.")

                    while (new_type := input("New contractor type: ")) == "":
                        print("Contractor type can't be empty.")

                    new_contact = input("New contractor contact (optional): ")

                    phone_prompt = "New contractor phone number: "
                    check_phone = "this string needs to contain letters :)"
                    while not check_phone.isdigit():
                        new_phone = input(phone_prompt)
                        check_phone = new_phone.replace("+","").replace("-","").replace(" ","")

                    while (new_address := input("New contractor address: ")) == "":
                        print("Contractor address can't be empty.")

                    add_opening_hours = input("Add opening hours for contractor: ")

                    new_contractor = Contractor(None, new_destinationID, 0.0, new_name, new_contact, new_phone, new_address, add_opening_hours, new_type)

                    try:
                        self.logic_api.contractor_add(new_contractor)
                    except Exception as e:
                        print(f"Error adding contractor '{new_name}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Remove a contractor
            case "r":
                if self.logic_api.is_manager_logged_in():
                    remove_id = input("Remove contractor with the ID: ").upper()

                    if input(f"Are you sure you want to remove contractor '{remove_id}' (Y to confirm)? ").upper() != "Y":
                        return None

                    try:
                        self.logic_api.contractor_remove(remove_id)
                    except Exception as e:
                        print(f"Error removing contractor '{remove_id}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # View contact info
            case "v":
                view_contact = None

                while view_contact is None:
                    view_contact_ID = input("View the contact information of contractor with the ID: ").upper()

                    try:
                        view_contact = self.logic_api.contractor_get_by_ID(view_contact_ID)
                    except Exception as e:
                        print(f"Error loading contact info for contractor '{view_contact_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    if view_contact is None:
                        print(f"No contractor found with the ID: '{view_contact_ID}', try again (B to cancel).")

                    if view_contact_ID == "B":
                        return None

                view_contact_table = PrettyTable()
                view_contact_table.field_names = ["ID", "Name", "Phone", "Address", "Rating"]
                view_contact_table.add_row([view_contact.ID,view_contact.name,view_contact.phone,view_contact.address,view_contact.rating])
                print(view_contact_table)
                input(ui_consts.MSG_ENTER_CONTINUE)
                return None

            # Edit contractor
            case "e":
                if self.logic_api.is_manager_logged_in():
                    contractor_edit = None

                    while contractor_edit is None:
                        contractor_edit_ID = input("Edit contractor with the ID (B to cancel): ").upper()

                        if contractor_edit_ID == "B":
                            return None

                        try:
                            contractor_edit = self.logic_api.contractor_get_by_ID(contractor_edit_ID)
                        except Exception as e:
                            print(f"Error loading contractor data for contractor '{contractor_edit_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None

                        if contractor_edit is None:
                            print(f"No contractor with the ID: '{contractor_edit_ID}', try again (B to cancel).")

                        if contractor_edit_ID == "B":
                            return None

                    # Since we found a valid contractor to edit, display the available destinations
                    print(all_destinations_table)

                    new_destinationID_prompt = "Enter new destination ID for the contractor (B to cancel): "
                    try:
                        while not self.logic_api.destination_get_by_ID(new_destinationID := input(new_destinationID_prompt).upper()):
                            if new_destinationID == "B":
                                return None
                            print(f"No destination found with the ID: '{new_destinationID}'.")
                    except Exception as e:
                        print(f"Error loading destination '{new_destinationID}' while editing contractor '{contractor_edit_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    setattr(contractor_edit, "destinationID", new_destinationID)

                    print("Enter new data for the contractor, leave the field empty to keep the previous data.")

                    editable_attributes = ["name","contact","phone","address","opening_hours","contractor_type"]
                    for attribute in editable_attributes:
                        current_value = getattr(contractor_edit, attribute)

                        new_value = input(f"New {attribute.capitalize().replace("_", " ")} (Current {current_value}): ").strip()
                        if not new_value:
                            continue

                        if attribute == "phone":
                            check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")
                            while not check_phone.isdigit():
                                print(ui_consts.MSG_INVALID_PHONE)
                                new_value = input(f"New {attribute.capitalize().replace("_", " ")} (Current {current_value}): ").strip()
                                check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")

                        setattr(contractor_edit, attribute, new_value)

                    try:
                        self.logic_api.contractor_edit(contractor_edit)
                    except Exception as e:
                        print(f"Error editing contractor '{contractor_edit.ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Search for contractor
            case "s":
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)
                return None

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return None
