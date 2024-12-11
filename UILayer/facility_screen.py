import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Facility

class FacilityScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        print("Main Menu > Properties > Facilities")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a facility		[E] Edit a facility			[B] Go back")
        print("|	[R] Remove a facility		[S] Search for")
        print("|	[V] View details")
        print("|")
        print(ui_consts.SEPERATOR)

        propertyID = self.ui.logic_api.facility_get_selected_property()

        all_facilities = self.ui.logic_api.facility_get_by_propertyID(propertyID)

        all_facilities_table = PrettyTable()
        all_facilities_table.field_names = ["ID","Name","Description"]

        for facility in all_facilities:
            all_facilities_table.add_row([facility.ID,facility.name,facility.description])

        all_facilities_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(all_facilities) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Facility list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if total_pages != 0:
            print(all_facilities_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        if cmd == "n":
            self.current_page += 1

        if cmd == "p":
            self.current_page -= 1

        # Add a facility
        if cmd == "a":
            f_new_name = input("New facility name: ")
            f_new_description = input("New facility description: ")

            new_facility= Facility(None, propertyID, f_new_name, f_new_description)

            self.ui.logic_api.facility_add(new_facility)


        # Remove a facility
        if cmd == "r":
            remove_id = input("Remove facility that has the ID: ").upper() # Klára þegar skjalakerfi er klárt
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command
            self.ui.logic_api.facility_remove(remove_id)

        if cmd == "s":
            search = input("Search for: ") # Sama search allstaðar nema á tickets
            #eftir að implementa

        # View details
        if cmd == "v":
            view_facility = input("View the details of facility with the ID: ").upper()
            facility_by_id = self.ui.logic_api.facility_get_by_ID(view_facility)
            facility_by_id_table = PrettyTable()
            facility_by_id_table.field_names = ["ID","Name","Description"]
            facility_by_id_table.add_row([facility_by_id.ID,facility_by_id.name,facility_by_id.description])
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command	
            print(facility_by_id_table)
            input()
        # Edit a facility

        if cmd == "e":
            f_edit_facility = input("Edit the facility with the ID:").upper()
            # If ID does not exist in facility list, raise error "No facility found with that ID!"
            #If ID does not exist, cancel command, á eftir að implementa
            print("If you do not wish to change a specific field you can leave the input empty")
            f_change_name = input("Change facility name to: ")
            f_change_description = input("Change facility description to: ")

        if cmd == "b":
            return ui_consts.CMD_BACK

        return self
