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
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a property		[E] Edit a property			[B] Go back")
        print("|	[R] Remove a property		[S] Search for")
        print("|	[D] Property details		[V] View last property report")
        print("|	[WR] Write a property report")
        print("|")
        print(ui_consts.SEPERATOR)
        print("|	Property list")

        properties : list[Property] = self.ui.logic_api.get_all_properties()

        property_table = PrettyTable()
        property_table.field_names = ["ID","Name","Location","Status","Destination"]

        for property in properties:
            property_table.add_row([property.id, property.name, property.location, property.status, property.destinationID])

        print(property_table)

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

        cmd = input("Command: ")

        return self
