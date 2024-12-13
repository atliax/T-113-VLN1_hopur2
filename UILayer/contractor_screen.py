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
    """
    Class representing the contractor management screen in the UI.
    Handles displaying contractor information and allowing user actions.
    """
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self) -> str | None:
     # main method to display contractor screen and handle commands

        self.clear_screen()

        print("Main Menu > Staff > Contractors")

        print(ui_consts.SEPERATOR)
        print("|")

        #display menu options based on user permissions
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
        # load contractor list
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
        # make sure the current page is within valid bounds
        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)
        # set up contractor table
        contractor_table = PrettyTable()
        contractor_table.field_names = ["ID", "Name","Type","Destination","Contact","Rating","Opening hours"]
        contractor_table._min_table_width = ui_consts.TABLE_WIDTH

        for contractor in contractor_list:
            try:
                # get destination details for contractor
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

            contractor_table.add_row([
                contractor.ID,
                fill(contractor.name,width=20),
                fill(contractor.contractor_type,width=18),
                fill(contractor_destination_country,width=15),
                fill(contractor.contact,width=18),
                contractor.rating if contractor.name != "Chuck Norris" else "Infinity",
                fill(contractor.opening_hours,width=18)])
            
        # display contractor list and navigation options
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

        # load all destinations for use in commands
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

            # Add a contractor if manager permission exists
            case "a":
                if self.logic_api.is_manager_logged_in():
                    # display all available destinations for user
                    print(all_destinations_table)
                    # prompt for destination ID and validate it
                    new_destinationID_prompt = "Enter destination ID for new contractor (B to cancel): "
                    try:
                        while not self.logic_api.destination_get_by_ID(new_destinationID := input(new_destinationID_prompt).upper()):
                            if new_destinationID == "B":
                                return None #user cancels adding contractor
                            print(f"No destination found with the ID: '{new_destinationID}'")
                    except Exception as e:
                        # Handle errors related to fetching destination
                        print(f"Error loading destination '{new_destinationID}' for new contractor:")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    # name and type inputs can not be empty
                    while (new_name := input("New contractor name: ")) == "":
                        print("Contractor name can't be empty.")

                    while (new_type := input("New contractor type: ")) == "":
                        print("Contractor type can't be empty.")

                    new_contact = input("New contractor contact (optional): ")
                    # only valid digits can be input, removing space, '-' and '+'
                    phone_prompt = "New contractor phone number: "
                    check_phone = "this string needs to contain letters :)"
                    while not check_phone.isdigit():
                        new_phone = input(phone_prompt)
                        check_phone = new_phone.replace("+","").replace("-","").replace(" ","")

                    while (new_address := input("New contractor address: ")) == "":
                        print("Contractor address can't be empty.")

                    add_opening_hours = input("Enter opening hours for contractor: ")

                    # Create a new contractor instance with collected information, ID will be generated automatically and default rating is 0.0
                    new_contractor = Contractor(None, new_destinationID, 0.0, new_name, new_contact, new_phone, new_address, add_opening_hours, new_type)

                    try:
                        # Try to add new contractor using the logic API, handling errors in the process
                        self.logic_api.contractor_add(new_contractor)
                    except Exception as e:
                        print(f"Error adding contractor '{new_name}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    # Display message if user lacks necesary permission
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Remove a contractor
            case "r":
                # if user has manager permissions
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

            # View contact info for a specific contractor
            case "v":
                view_contact = None

                while view_contact is None:
                    view_contact_ID = input("View the contact information of contractor with the ID: ").upper()

                    try:
                        # Attempt to fetch contractor details using logic API, handling errors in getting data
                        view_contact = self.logic_api.contractor_get_by_ID(view_contact_ID)
                    except Exception as e:
                        print(f"Error loading contact info for contractor '{view_contact_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    if view_contact is None:
                        # Inform user if contractor ID is invalid
                        print(f"No contractor found with the ID: '{view_contact_ID}', try again (B to cancel).")

                    if view_contact_ID == "B":
                        return None

                # Create a table to display contact information
                view_contact_table = PrettyTable()
                view_contact_table.field_names = ["ID", "Name", "Phone", "Address", "Rating"]
                # Add details to the table
                view_contact_table.add_row([
                    view_contact.ID,
                    fill(view_contact.name,width=25),
                    fill(view_contact.phone,width=25),
                    fill(view_contact.address,width=30),
                    view_contact.rating if view_contact.name != "Chuck Norris" else "Infinity"])

                print(view_contact_table)
                input(ui_consts.MSG_ENTER_CONTINUE)
                return None

            # Edit contractor if the user has manager permissions
            case "e":
                if self.logic_api.is_manager_logged_in():
                    contractor_edit = None

                    while contractor_edit is None:
                        contractor_edit_ID = input("Edit contractor with the ID (B to cancel): ").upper()

                        if contractor_edit_ID == "B":
                            return None

                        try:
                            # Fetch contractor details using logic API and handle errors while fetching data
                            contractor_edit = self.logic_api.contractor_get_by_ID(contractor_edit_ID)
                        except Exception as e:
                            print(f"Error loading contractor data for contractor '{contractor_edit_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None

                        if contractor_edit is None:
                            # Inform user if contractor ID is invalid
                            print(f"No contractor with the ID: '{contractor_edit_ID}', try again.")

                    # display the available destinations
                    print(all_destinations_table)

                    # Prompt for new destination ID and validate it
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

                    # Update the destination ID for the contractor
                    setattr(contractor_edit, "destinationID", new_destinationID)

                    print("Enter new data for the contractor, leave the field empty to keep the previous data.")

                    editable_attributes = ["name","contact","phone","address","opening_hours","contractor_type"]
                    # Loop through each attribute, allowing user to edit
                    for attribute in editable_attributes:
                        current_value = getattr(contractor_edit, attribute) # Get current value of attribute

                        new_value = input(f"New {attribute.capitalize().replace("_", " ")} (Current {current_value}): ").strip()
                        if not new_value:
                            continue # Keep current value if nothing is input

                        if attribute == "phone":
                            # Validate phone number
                            check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")
                            while not check_phone.isdigit():
                                print(ui_consts.MSG_INVALID_PHONE)
                                new_value = input(f"New {attribute.capitalize().replace("_", " ")} (Current {current_value}): ").strip()
                                check_phone = new_value.replace("+", "").replace("-", "").replace(" ", "")

                        # Update the contractor object with the new value
                        setattr(contractor_edit, attribute, new_value)

                    try:
                        # Save the updated contractor using the logic API
                        self.logic_api.contractor_edit(contractor_edit)
                    except Exception as e:
                        # Handle errors when updating
                        print(f"Error editing contractor '{contractor_edit.ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION) # Displays if user is not a manager
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Search for contractor by filter 
            case "s":
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)
                return None

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return None
