# standard library imports
import math
from textwrap import fill

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Facility

class FacilityScreen(BaseScreen):
    """
    Screen class to manage facilities within a property,
    allows adding, editing viewing, removing 
    and searching for facilities
    """
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1 # track current page for navigation
        self.active_search_filter = "" 

    def run(self) -> str | None:
        """
        Main method to display the facilities management 
        screen and handle user input"""
        self.clear_screen()

        print("Main Menu > Properties > Facilities")

        print(ui_consts.SEPERATOR)
        print("|")

        # Display options based on user permissions
        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add a facility		[E] Edit a facility			[B] Go back")
            print("|	[R] Remove a facility		[S] Search for")
            print("|	[V] View details")
        else:
            print_formatted_text(HTML("|	<s>[A] Add a facility</s>		<s>[E] Edit a facility</s>			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove a facility</s>		[S] Search for"))
            print_formatted_text(HTML("|	[V] View details"))

        print("|")
        print(ui_consts.SEPERATOR)

        # Get the currently selected property ID
        propertyID = self.logic_api.facility_get_selected_property()

       # Load facilities based on search filter or selected property
        try:
            if self.active_search_filter:
                facility_list = self.logic_api.facility_search(self.active_search_filter)
            else:
                facility_list = self.logic_api.facility_get_by_propertyID(propertyID)
        except Exception as e:
            print(f"Error loading facilities:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        total_pages = math.ceil(len(facility_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        # Set up facilities table
        facilities_table = PrettyTable()
        facilities_table.field_names = ["ID","Name","Description"]
        facilities_table._min_table_width = ui_consts.TABLE_WIDTH

        for facility in facility_list:
            facilities_table.add_row([facility.ID,facility.name,facility.description])

        # Fetch the active property details
        try:
            active_property = self.logic_api.property_get_by_ID(propertyID)
        except Exception as e:
            print(f"Error loading property data for '{propertyID}':")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        if active_property is not None:
            property_name = active_property.name
        else:
            property_name = "-"

        # Display facilities and page nagivation options
        print(f"|  Facility list for Property '{property_name}' ({propertyID}) (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(facilities_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("")
            print("No facilities found.")

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

            # Add a facility
            case "a":
                if self.logic_api.is_manager_logged_in():
                    # Prompt for facility name, ensuring its not empty
                    while (f_new_name := input("New facility name: ")) == "":
                        print("Facility name can't be empty.")

                    f_new_description = input("New facility description: ")

                    new_facility = Facility(None, propertyID, f_new_name, f_new_description)

                    # Attempt to add the facility
                    try:
                        self.logic_api.facility_add(new_facility)
                    except Exception as e:
                        print(f"Error creating facility '{f_new_name}' for property '{propertyID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Remove an existing facility
            case "r":
                if self.logic_api.is_manager_logged_in():
                    remove_facility_prompt = "Enter ID for facility to remove (B to cancel): "
                    try:
                        # Prompt for a valic facility ID
                        while not self.logic_api.facility_get_by_ID(remove_facility_ID := input(remove_facility_prompt).strip().upper()):
                            if remove_facility_ID == "B":
                                return None
                            print(f"No facility found with the ID: '{remove_facility_ID}'.")

                        # Confirm removal if facility belongs to a different property
                        if not self.logic_api.facility_get_by_ID(remove_facility_ID).propertyID == propertyID:
                            if input(f"Facility '{remove_facility_ID}' does not belong to the currently active property, do you still want to remove it? (Y to confirm)? ").upper() != "Y":
                                return None
                        elif input(f"Are you sure you want to remove facility '{remove_facility_ID}' (Y to confirm)? ").upper() != "Y":
                            return None

                        # Remove the facility
                        self.logic_api.facility_remove(remove_facility_ID)
                    except Exception as e:
                        print(f"Error removing facility '{remove_facility_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None


            # Search for
            case "s":
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)
                return None

            # View details
            case "v":
                view_facility = None

                while view_facility is None:
                    # Prompt for a valid facility ID
                    view_facility_ID = input("View details of the facility with the ID (B to cancel): ").strip().upper()

                    if view_facility_ID == "B":
                        return None

                    try:
                        # Fetch facility details
                        view_facility = self.logic_api.facility_get_by_ID(view_facility_ID)
                    except Exception as e:
                        print(f"Error loading data for facility '{view_facility_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    if view_facility is None:
                        print(f"No facility with the ID: '{view_facility_ID}'.")
                        input(ui_consts.MSG_ENTER_CONTINUE)

                # Display facility details
                view_facility_table = PrettyTable()
                view_facility_table.field_names = ["ID", "Name", "Description"]
                view_facility_table.add_row([view_facility.ID, fill(view_facility.name, width=30) ,fill(view_facility.description, width=40)])
                view_facility_table._min_table_width = ui_consts.TABLE_WIDTH

                print(view_facility_table)

                input(ui_consts.MSG_ENTER_CONTINUE)
                return None

    
            # Edit a facility
            case "e":
                if self.logic_api.is_manager_logged_in():

                    edit_facility = None

                    while edit_facility is None:
                        # Prompt for valid facility ID
                        edit_facility_ID = input("Edit the facility with the ID (B to cancel): ").strip().upper()

                        if edit_facility_ID == "B":
                            return None

                        try:
                            # Fetch facility details
                            edit_facility = self.logic_api.facility_get_by_ID(edit_facility_ID)
                        except Exception as e:
                            print(f"Error loading data for facility '{edit_facility_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None

                        if edit_facility is None:
                            print(f"No facility with the ID: '{edit_facility_ID}'.")

                    # Confirm editing if the facility belongs to a different property
                    if not edit_facility.propertyID == propertyID:
                        if input(f"Facility '{edit_facility_ID}' does not belong to the currently active property, do you still want to edit it? (Y to confirm)? ").upper() != "Y":
                            return None

                    print("Enter new data for the facility, leave the field empty to keep the previous data.")

                    # Prompt for editable attributes
                    editable_attributes = ["name", "description"]

                    for attribute in editable_attributes:
                        current_value = getattr(edit_facility, attribute)
                        new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()

                        if new_value:
                            setattr(edit_facility, attribute, new_value)
                            # Save changes

                    try:
                        self.logic_api.facility_edit(edit_facility)
                    except Exception as e:
                        print(f"Error editing facility '{edit_facility_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return None
