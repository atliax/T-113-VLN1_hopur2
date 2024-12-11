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

        match cmd:
            case "n":
                self.current_page += 1
            case "p":
                self.current_page -= 1
            # Add a facility
            case "a":
                #f_new_name = input("New facility name: ")
                #f_new_description = input("New facility description: ")
                #new_facility = Facility(None, propertyID, f_new_name, f_new_description)
                #self.ui.logic_api.facility_add(new_facility)
                while (f_new_name := input("New facility name: ")) != "":
                    print("Facility name cannot be empty. Please enter a valid name.")

                # f_new_name = input("New facility name: ").strip()
                # while not f_new_name:  
                #    print("Facility name cannot be empty. Please enter a valid name.")
                #    f_new_name = input("New facility name: ").strip()

                f_new_description = input("New facility description: ").strip()
                while not f_new_description:  
                    print("Facility description cannot be empty. Please enter a valid description.")
                    f_new_description = input("New facility description: ").strip()

                new_facility = Facility(None, propertyID, f_new_name, f_new_description)

                self.ui.logic_api.facility_add(new_facility)
            # Remove a facility
            case "r":
                #remove_id = input("Remove facility that has the ID: ").upper() # Klára þegar skjalakerfi er klárt
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command
                #self.ui.logic_api.facility_remove(remove_id)
                removing_facility = True  

                while removing_facility:
                    remove_id = input("Remove facility that has the ID (B to cancel): ").strip().upper()

                    if remove_id == "B":
                        print("Facility removal canceled.")
                        removing_facility = False 
                        continue

                    facility_to_remove = None
                    for facility in all_facilities:
                        if facility.ID == remove_id:
                            facility_to_remove = facility
                            break

                    if facility_to_remove:
                        confirm = input(f"Are you sure you want to remove the facility '{facility_to_remove.name}' (ID: {remove_id})?!?! (Y/N): ").strip().upper()
                        if confirm == "Y":
                            self.ui.logic_api.facility_remove(remove_id)
                            print(f"Facility '{facility_to_remove.name}' (ID: {remove_id}) removed!")
                            removing_facility = False 
                        else:
                            print("Facility removal canceled.")
                            removing_facility = False 
                    else:
                        print(f"No facility found with the ID: '{remove_id}'. Please try again (B to cancel).")
            # Search for
            case "s":
                #search = input("Search for: ") # Sama search allstaðar nema á tickets
                #eftir að implementa
                searching = True 

                while searching:
                    search = input("Search for: ").strip()

                    filtered_facilities = self.ui.logic_api.facility_search(search)

                    if not filtered_facilities:
                        print(f"No facilities found matching '{search}'.")
                    else:
                    
                        search_results_table = PrettyTable()
                        search_results_table.field_names = ["ID", "Name", "Description"]

                        for facility in filtered_facilities:
                            search_results_table.add_row([facility.ID, facility.name, facility.description])

                        print("\nSearch Results:")
                        print(search_results_table)

                    while True:
                        choice = input("\nDo you want to search for another facility? (Y to search again, (B to go back)): ").strip().upper()
                        if choice == "Y":
                            break  
                        elif choice == "B":
                            searching = False  
                            break
                        else:
                            print("Invalid choice. Please enter 'Y' to search again (B to go back)")
            # View details
            case "v":
                facility_by_id = None
                viewing_facilities = True  

                while viewing_facilities:  
                    facility_by_id = None
                    finding_facility = True  

                    while finding_facility:  
                        view_facility = input("View the details of facility with the ID (B to cancel): ").strip().upper()

                        if view_facility == "B":
                            finding_facility = False  
                            viewing_facilities = False  
                            break  
                    
                        facility_by_id = self.ui.logic_api.facility_get_by_ID(view_facility)

                        if facility_by_id:  
                            finding_facility = False  
                        else:
                            print(f"No facility with the ID: '{view_facility}'. Try again, (B to cancel).\n")

                    if facility_by_id:  
                   
                        facility_by_id_table = PrettyTable()
                        facility_by_id_table.field_names = ["ID", "Name", "Description"]
                        facility_by_id_table.add_row([facility_by_id.ID, facility_by_id.name, facility_by_id.description])
                        print(facility_by_id_table)

                    if viewing_facilities: 
                        choice = input("\nDo you want to view another facility? (Y to continue, B to go back): ").strip().upper()
                        if choice == "B":
                            viewing_facilities = False  

                # view_facility = input("View the details of facility with the ID: ").upper()
                # facility_by_id = self.ui.logic_api.facility_get_by_ID(view_facility)
                # facility_by_id_table = PrettyTable()
                # facility_by_id_table.field_names = ["ID","Name","Description"]
                # facility_by_id_table.add_row([facility_by_id.ID,facility_by_id.name,facility_by_id.description])
                # # If ID does not exist in property list, raise error "No facility found with that ID!"
                # # If ID does not exist, cancel command	
                # print(facility_by_id_table)
                # input("Press enter to continue.")
            # Edit a facility
            case "e":
                facility_edit = None

                while facility_edit is None:
                    f_edit_facility = input("Edit the facility with the ID (B to cancel): ").strip().upper()

                    if f_edit_facility == "B":
                        return ui_consts.CMD_BACK  

                
                    for facility in all_facilities:
                        if facility.ID == f_edit_facility:
                            facility_edit = facility  
                            break

                    if facility_edit is None:
                        print(f"No facility with the ID: '{f_edit_facility}'. Try again, (B to cancel)")

            
                editable_attributes = ["name", "description"]  

                for attribute in editable_attributes:
                    current_value = getattr(facility_edit, attribute)
                    new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()

                    if new_value:  
                        setattr(facility_edit, attribute, new_value)

            
                self.ui.logic_api.facility_edit(facility_edit)
                print(f"Facility '{facility_edit.ID}' updated successfully!")

                # f_edit_facility = input("Edit the facility with the ID:").upper()
                # # If ID does not exist in facility list, raise error "No facility found with that ID!"
                # #If ID does not exist, cancel command, á eftir að implementa
                # print("If you do not wish to change a specific field you can leave the input empty")
                # f_change_name = input("Change facility name to: ")
                # f_change_description = input("Change facility description to: ")
            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return self
