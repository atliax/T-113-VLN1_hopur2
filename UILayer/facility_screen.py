# Standard library imports
import math
from textwrap import fill

# pip libabry imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

#local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Facility

class FacilityScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self) -> str | None:
        self.clear_screen()

        print("Main Menu > Properties > Facilities")

        print(ui_consts.SEPERATOR)
        print("|")

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

        propertyID = self.logic_api.facility_get_selected_property()

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

        facilities_table = PrettyTable()
        facilities_table.field_names = ["ID","Name","Description"]
        facilities_table._min_table_width = ui_consts.TABLE_WIDTH

        for facility in facility_list:
            facilities_table.add_row([facility.ID,facility.name,facility.description])

        print(f"|  Facility list for Property '{propertyID}' (Page {self.current_page+1}/{total_pages}):")
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
                    while (f_new_name := input("New facility name: ")) == "":
                        print("Facility name can't be empty.")

                    f_new_description = input("New facility description: ")

                    new_facility = Facility(None, propertyID, f_new_name, f_new_description)

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

            # Remove a facility
            case "r":
                if self.logic_api.is_manager_logged_in():
                    remove_facility_prompt = "Enter ID for facility to remove (B to cancel): "
                    try:
                        while True:
                            remove_facility_ID = input(remove_facility_prompt).strip().upper()

                            if remove_facility_ID == "B":
                                return None  

                            facility_to_remove = self.logic_api.facility_get_by_ID(remove_facility_ID)

                            if not facility_to_remove:
                                print(f"No facility found with the ID: '{remove_facility_ID}'.")
                                continue

                            """Check if the facility belongs to the currently selected property"""
                            if facility_to_remove.propertyID != propertyID:
                                print(f"Warning: Facility '{remove_facility_ID}' does not belong to property '{propertyID}'.")
                                continue_remove = input("Do you still want to remove this facility (Y/N)? ").strip().upper()
                                if continue_remove == "N":
                                    return None  
                                elif continue_remove != "Y":
                                    print("Invalid input. Returning to menu.")
                                    return None

                            
                            break

                        
                        if input(f"Are you sure you want to remove facility '{remove_facility_ID}' (Y to confirm)? ").strip().upper() != "Y":
                            return None  

                        self.logic_api.facility_remove(remove_facility_ID)
                        print(f"Facility '{remove_facility_ID}' removed successfully.")

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
                    view_facility_ID = input("View details of the facility with the ID (B to cancel): ").strip().upper()

                    if view_facility_ID == "B":
                        return None

                    try:
                        view_facility = self.logic_api.facility_get_by_ID(view_facility_ID)
                    except Exception as e:
                        print(f"Error loading data for facility '{view_facility_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    if view_facility is None:
                        print(f"No facility with the ID: '{view_facility_ID}'.")
                        input(ui_consts.MSG_ENTER_CONTINUE)

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
                        edit_facility_ID = input("Edit the facility with the ID (B to cancel): ").strip().upper()

                        if edit_facility_ID == "B":
                            return None

                        try:
                            edit_facility = self.logic_api.facility_get_by_ID(edit_facility_ID)
                        except Exception as e:
                            print(f"Error loading data for facility '{edit_facility_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None

                        if edit_facility is None:
                            print(f"No facility with the ID: '{edit_facility_ID}'.")
                        else:
                            """ Check if the facility belongs to the selected property"""
                            if edit_facility.propertyID != propertyID:
                                print(f"Warning: Facility '{edit_facility_ID}' does not belong to property '{propertyID}'.")
                                continue_edit = input("Do you want to continue editing this facility (Y/N)? ").strip().upper()
                                if continue_edit == "N":
                                    return None
                                elif continue_edit != "Y":
                                    print("Invalid input. Returning to menu.")
                                    return None  
                                

                    """continue editing if user chooses to edit a facility not within chosen property"""
                    print("Enter new data for the facility, leave the field empty to keep the previous data.")

                    editable_attributes = ["name", "description"]

                    for attribute in editable_attributes:
                        current_value = getattr(edit_facility, attribute)
                        new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()

                        if new_value:
                            setattr(edit_facility, attribute, new_value)

                    try:
                        self.logic_api.facility_edit(edit_facility)
                        print(f"Facility '{edit_facility_ID}' updated successfully.")
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
