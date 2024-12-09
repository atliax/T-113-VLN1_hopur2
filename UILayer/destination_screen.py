from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Destination

from prettytable import PrettyTable

class DestinationScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Destinations")

        destinations : list[Destination] = self.ui.logic_api.get_all_destinations()

        destination_table = PrettyTable()
        destination_table.field_names = ["ID","managerID","Destination","Airport", "Phone", "Opening hours"]

        for destination in destinations:
            destination_table.add_row([destination.destinationID, destination.managerID, destination.country, destination.airport, destination.phone, destination.opening_hours])

        print(destination_table)

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add a destination
        if cmd == "a":
            destination_attributes = ["managerID", "country", "airport", "phone", "opening_hours"]
            new_destination = ""
            for attribute in destination_attributes:
                new_value = input(f"New {attribute}: ")
                new_destination += new_value + ","
            self.ui.logic_api.add_new_destination(new_destination)


        # Edit destination
        if cmd == "e":
            # 
            destination_attributes = ["managerID", "country", "airport", "phone", "opening_hours"]
            pick_destination = input("Type in the id of the destination you want to edit: ")
            for destination in destinations:
                if destination.destinationID == pick_destination:
                    destination_edit = destination
            for attribute in destination_attributes:
                current_value = getattr(destination, attribute)
                new_value = input(f"New {attribute} (current: {current_value}): ").strip()
                if new_value:
                    setattr(destination_edit, attribute, new_value)   
            self.ui.logic_api.edit_destinations(destinations)   

        if cmd == "b":
            return ui_consts.BACK

        return self
