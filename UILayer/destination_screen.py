from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class DestinationScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Destinations")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        print("|	[R] Remove a destination	[S] Search for")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ")

        # Add a destination
        if cmd == "a":
            new_dest = input("New destination: ")
            new_airport = input("New destination airport: ")
            new_opening_hours = input("New destination airport opening hours: ")

        # Remove destination
        if cmd == "r":
            remove = input("Remove destination with ID: ")

        # Edit destination
        if cmd == "e":
            #if nothing is input, the name/loc will be unchanged
            change_dest = input("Change destination: ")
            change_airport = input("Change destination airport: ")
            change_opening_hours = input("Change destination airport opening hours: ")

        if cmd == "s":
            search = input("Search for: ")

        if cmd == "b":
            return ui_consts.BACK

        return self
