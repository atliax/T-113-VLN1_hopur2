from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Property

from prettytable import PrettyTable

class PropertiesScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Properties")

        properties : list[Property] = self.ui.logic_api.get_all_properties()

        property_table = PrettyTable()
        property_table.field_names = ["ID","Name","Destination","Address","Sq meters","Rooms","Type"]

        for property in properties:
            property_table.add_row([property.propertyID, property.name, property.destinationID, property.address, property.square_meters, property.rooms, property.type])

        # dæmi um prentun á töflu með ákveðinni breidd:
        property_table._min_table_width = ui_consts.TABLE_WIDTH

        #print(property_table.get_string(start=0, end=10))
        print("|  Property list:")
        print(property_table)

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a property		[E] Edit a property			[B] Go back")
        print("|	[R] Remove a property		[S] Search for")
        print("|	[V] View facilities")
        print("|")
        print(ui_consts.SEPERATOR)
        print("")

        cmd = input("Command: ").lower()

        # [A] Add a property
        if cmd == "a":

            # Get property detail inputs from user 
            p_new_name = input("New property name: ")
            p_new_location = input("New property destionation ID: ")
            p_new_address = input("New property address: ")
            p_new_square = int(input("New property square meters: "))
            p_new_roomnum = int(input("New property number of rooms: "))
            p_new_type = input("New property type: ")

            # construct property
            new_property = Property(None, p_new_name, p_new_location, p_new_address, p_new_square, p_new_roomnum, p_new_type)
            
            # Send property to logic api
            self.ui.logic_api.property_add(new_property)


        # [R] Remove a property
        if cmd == "r":
            remove_property = input("Remove a property that has the ID: ")
        
        # [V] View facilities
        if cmd == "v":
            return ui_consts.FACILITY


        # [E] Edit a property 
        if cmd == "e":
            edit_property = input("Edit property with the ID: ") # If nothing is input, the field will be left unchanged
                # If ID does not exist in property list, raise error "No property found with that ID!"
                # If ID does not exist, cancel command EKKI IMPLEMENTAÐ
            print("If you do not wish to change a specific field, you can leave the input empty")
            change_name = input("Change property name to: ")
            change_destination = input("Change property destination to: ")
            change_address = input("Change property address to: ")
            change_square_mtrs = int(input("Change property square meters to: "))
            change_rooms = int(input("Change property number of rooms to: "))
            change_property_type = input("Change property type to: ")

        # [S] Search for
        if cmd == "s":
            print("What keyword would you like to search for?")
            print("You can combine keywords by following a word with ,")
            print("Example: (Grænland,Nuukstræti 4)")
            search = input("Search for: ")       # Sama search fyrir alla skjái
                # print out a new filtered list based on keywords input
                # GoTo "Main menu > Properties > Filtered"
                # "Main menu > Properties > Filtered" window and commands are identical to "Main menu > Properties"
                # Just replace the normal properties list with the filtered one

        # [B] Go Back
        if cmd == "b":
            return ui_consts.BACK
    


        return self
