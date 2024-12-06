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
        property_table.field_names = ["ID","Name","Location","Status","Destination"]

        for property in properties:
            property_table.add_row([property.id, property.name, property.location, property.status, property.destinationID])

        # dæmi um prentun á töflu með ákveðinni breidd:
        property_table._min_table_width = 118

        # dæmi um prentun á hluta af töflu:
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
        


        #print("|   ID   |                 Name               	|   Location   				|  Status  | Last report")
        #print("----------------------------------------------------------------------------------------------------------------------")
        #print("|    1   |  Example Property a                	|  Location a  				| Good	   |  dd/mm/yyyy")
        #print("|    2   |  Example Property b                	|  Location b  				| Normal   |  dd/mm/yyyy")
        #print("|    3   |  Example Property c   		|  Location b  				| Bad	   |  dd/mm/yyyy")
        #print("|   ...  |  ...                               	|      ...     				| ...	   |  ")
        #print("|    n   |  Example Property n                	|  Location n  				|	   |")

        print("|")
        print(ui_consts.SEPERATOR)
        print("")

        cmd = input("Command: ").lower()

        # Add a property
        if cmd == "a": 
            new_property = input("New property name: ")
            new_location = input("New property destionation: ")
            new_address = input("New property address: ")
            new_square = int(input("New property square meters: "))
            new_number_rooms = int(input("New property number of rooms: "))
            new_type = input("New property type: ")

        # Remove a property
        if cmd == "r":
            remove_property = input("Remove a property that has the ID: ")
        
        # View facilities
        if cmd == "v":
            view = input("View the facilities in property with ID: ")
                # If ID does not exist in property list, raise error "No property found with that ID!"
                # If ID does not exist, cancel command	
                # GoTo "Main menu > Properties > Facilities" ******** Á EFTIR AÐ BÚA TIL GLUGGA
                # Print a list of facilities for property with input ID


         # Edit a property 
        if cmd == "e":
            edit_property = input("Edit property with the ID: ") # If nothing is input, the field will be left unchanged
                # If ID does not exist in property list, raise error "No property found with that ID!"
                # If ID does not exist, cancel command
            print("If you do not wish to change a specific field, you can leave the input empty")
            change_name = input("Change property name to: ")
            change_destination = input("Change property destination to: ")
            change_address = input("Change property address to: ")
            change_square_mtrs = int(input("Change property square meters to: "))
            change_rooms = int(input("Change property number of rooms to: "))
            change_property_type = input("Change property type to: ")

        # Search for
        if cmd == "s":
            print("What keyword would you like to search for?")
            print("You can combine keywords by following a word with ,")
            print("Example: (Grænland,Nuukstræti 4)")
            search = input("Search for: ")        
                # print out a new filtered list based on keywords input
                # GoTo "Main menu > Properties > Filtered"
                # "Main menu > Properties > Filtered" window and commands are identical to "Main menu > Properties"
                # Just replace the normal properties list with the filtered one

        # Go Back
        if cmd == "b":
            return ui_consts.BACK
    


        return self
