import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Facility

class FacilityScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self):
        self.clear_screen()

        print("Main Menu > Properties > Facilities")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.ui.logic_api.is_manager_logged_in():
            print("|	[A] Add a facility		[E] Edit a facility			[B] Go back")
            print("|	[R] Remove a facility		[S] Search for")
            print("|	[V] View details")
        else:
            print("|	[V] View details		[S] Search for				[B] Go back")

        print("|")
        print(ui_consts.SEPERATOR)

        propertyID = self.ui.logic_api.facility_get_selected_property()

        if self.active_search_filter:
            facility_list = self.ui.logic_api.facility_search(self.active_search_filter)
        else:
            facility_list = self.ui.logic_api.facility_get_by_propertyID(propertyID)

        facilities_table = PrettyTable()
        facilities_table.field_names = ["ID","Name","Description"]

        for facility in facility_list:
            facilities_table.add_row([facility.ID,facility.name,facility.description])

        facilities_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(facility_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Facility list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(facilities_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        match cmd:
            case "n":
                self.current_page += 1
            case "p":
                self.current_page -= 1
            # Add a facility
            case "a":
                if self.ui.logic_api.is_manager_logged_in():
                    while (f_new_name := input("New facility name: ")) == "":
                        print("Facility name can't be empty.")

                    f_new_description = input("New facility description: ")

                    new_facility = Facility(None, propertyID, f_new_name, f_new_description)
                    self.ui.logic_api.facility_add(new_facility)
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # Remove a facility
            case "r":
                if self.ui.logic_api.is_manager_logged_in():
                    remove_id = input("Remove facility that has the ID (B to cancel): ").strip().upper()

                    if remove_id == "B":
                        return self

                    facility_to_remove = self.ui.logic_api.facility_get_by_ID(remove_id)

                    if facility_to_remove is not None:
                        self.ui.logic_api.facility_remove(remove_id)
                    else:
                        print(f"No facility found with the ID: '{remove_id}'.")
                        input("Press enter to continue.")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # Search for
            case "s":
                self.active_search_filter = input("Search for: ")
            # View details
            case "v":
                view_facility = input("View the details of facility with the ID (B to cancel): ").strip().upper()

                if view_facility == "B":
                    return self

                facility_by_id = self.ui.logic_api.facility_get_by_ID(view_facility)

                if facility_by_id is None:
                    print(f"No facility with the ID: '{view_facility}'.")
                else:
                    facility_by_id_table = PrettyTable()
                    facility_by_id_table.field_names = ["ID", "Name", "Description"]
                    facility_by_id_table.add_row([facility_by_id.ID, facility_by_id.name, facility_by_id.description])
                    print(facility_by_id_table)

                input("Press enter to continue.")
            # Edit a facility
            case "e":
                if self.ui.logic_api.is_manager_logged_in():
                    f_edit_facility = input("Edit the facility with the ID (B to cancel): ").strip().upper()

                    if f_edit_facility == "B":
                        return ui_consts.CMD_BACK

                    f_edit_facility = self.ui.logic_api.facility_get_by_ID(f_edit_facility)

                    if f_edit_facility is None:
                        print(f"No facility with the ID: '{f_edit_facility}'.")

                    editable_attributes = ["name", "description"]

                    for attribute in editable_attributes:
                        current_value = getattr(f_edit_facility, attribute)
                        new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()

                        if new_value:
                            setattr(f_edit_facility, attribute, new_value)

                    self.ui.logic_api.facility_edit(f_edit_facility)
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return self
