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
        destination_table.field_names = ["ID","Country","Airport","Phone_nr","Opening_hours","manager"]

        for destination in destinations:
            destination_table.add_row([destination.id, destination.country, destination.airport, destination.phone_nr, destination.opening_hours, destination.manager])

        print(destination_table)

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add a destination
        if cmd == "a":
            new_destination = input("New destination country: ")
            new_airport = input("New destination airport: ")
            new_opening_hours = input("New destination airport opening hours: ")
            new_phone = int(input("New destination phone number: "))
            new_manager = input("New destination manager: ")

        # Edit destination
        if cmd == "e":
            edit_id = input("Edit destination with the ID: ")
                # If ID does not exist in the destination list, raise error "No destination found with that ID!"    
                 # If ID does not exist, cancel command
            print("If you do not wish to change a specific field, you can leave the input empty")
            change_destination = input("Change destination country to: ")
            change_airport = input("Change destination airport to: ")
            change_opening_hours = input("Change destination airport opening hours to: ")
            change_number = int(input("Change destination phone number to: "))
            change_manager = input("Change desination manager to: ")
        
        if cmd == "b":
            return ui_consts.BACK

        return self
