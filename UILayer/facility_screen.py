from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Facility

from Model import Property

class FacilityScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        properties = self.ui.logic_api.property_get_all()

        property_table = PrettyTable()
        property_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]

        for property in properties:
            property_table.add_row([property.ID, property.name, property.destinationID, property.address, property.square_meters, property.rooms, property.type])

        property_table._min_table_width = ui_consts.TABLE_WIDTH

        print("|  Property list:")
        print(property_table)
        property_ID = input("View the facilities in property with ID: ")
        # If ID does not exist in property list, raise error "No property found with that ID!"
        # If ID does not exist, cancel command	
        # Print a list of facilities for property with input ID

        facilities = self.ui.logic_api.facility_get_by_propertyID(property_ID)

        facility_table = PrettyTable()
        facility_table.field_names = ["ID","Name","Description"]

        for facility in facilities:
            facility_table.add_row([facility.ID,facility.name,facility.description])

        facility_table._min_table_width = ui_consts.TABLE_WIDTH

        print("Main Menu > Properties > Facilities")

        print(facility_table)

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a facility		[E] Edit a facility			[B] Go back")
        print("|	[R] Remove a facility		[S] Search for")
        print("|	[V] View details")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add a facility
        if cmd == "a":
            f_new_name = input("New facility name: ")
            f_new_description = input("New facility description: ")

            new_facility= Facility(None, property_ID, f_new_name, f_new_description)

            self.ui.logic_api.facility_add(new_facility)


        # Remove a facility
        if cmd == "r":
            remove_id = input("Remove facility that has the ID: ") # Klára þegar skjalakerfi er klárt
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command
            self.ui.logic_api.facility_remove(remove_id)

        if cmd == "s":
            search = input("Search for: ") # Sama search allstaðar nema á tickets
            #eftir að implementa

        # View details
        if cmd == "v":
            view = input("View the details of facility with the ID: ")
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command	
            print(f"Facility name: {f_new_name}")
            print(f"Facility description: {f_new_description}")

        # Edit a facility

        if cmd == "e":
            f_edit_facility = input("Edit the facility with the ID:")
            # If ID does not exist in facility list, raise error "No facility found with that ID!"
            #If ID does not exist, cancel command, á eftir að implementa
            print("If you do not wish to change a specific field you can leave the input empty")
            f_change_name = input("Change facility name to: ")
            f_change_description = input("Change facility description to: ")

        if cmd == "b":
            return ui_consts.CMD_BACK

        return self
