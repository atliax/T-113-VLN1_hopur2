from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Facility

class FacilityScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)

    def run(self):
        self.clear_screen()

        properties = self.ui.logic_api.get_all_properties()

        property_table = PrettyTable()
        property_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]

        for property in properties:
            property_table.add_row([property.propertyID, property.name, property.destinationID, property.address, property.square_meters, property.rooms, property.type])

        property_table._min_table_width = ui_consts.TABLE_WIDTH

        print("|  Property list:")
        print(property_table)
        property_ID = input("View the facilities in property with ID: ")
        # If ID does not exist in property list, raise error "No property found with that ID!"
        # If ID does not exist, cancel command	
        # Print a list of facilities for property with input ID

        facilities = self.ui.logic_api.get_facilities_by_propertyID(property_ID)

        facility_table = PrettyTable()
        facility_table.field_names = ["ID","Name","Description"]

        for facility in facilities:
            facility_table.add_row([facility.facilityID,facility.name,facility.description])

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
            new_facility = input("New facility name: ")
            new_description = input("New facility description: ")

        # Remove a facility
        if cmd == "r":
            remove = input("Remove facility that has the ID: ") # Klára þegar skjalakerfi er klárt
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command


        if cmd == "s":
            search = input("Search for: ") # Sama search allstaðar nema á tickets
            #eftir að implementa

        # View details
        if cmd == "v":
            view = input("View the details of facility with the ID: ")
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command	
            print(f"Facility name: {new_facility}")
            print(f"Facility description: {new_description}")

        if cmd == "b":
            return ui_consts.CMD_BACK

        return self
