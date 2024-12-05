from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class StaffScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main menu > Staff")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add an employee		    [E] Edit a destination			[B] Go back")
        print("|	[R] Remove an employee      [S] Search for")
        print("|	[C] View contractors")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ")

        if cmd == "a":
            new_employee = input("New employee name: ")
            new_phone_nr = input("New employee phone number: ")
            new_email = input("New employee email: ")
            new_ssn = input("New employee ssn: ")
            new_title = input("New employee job title: ")
            new_location = input("New employee location: ")
            # Starfsmaður er bættur við á listann. Auðkenni er búið til sjálfkrafa af forritinu 

        if cmd == "r":
            remove_employee = input("Remove employee with the ID: ")

        if cmd == "e":
            #if nothing is input, the field will be left unchanged
            change_name = input("Change employey name to: ")
            change_number = input("Change employee phone number to: ")
            change_email = input("Change employee email to: ")
            change_title = input("Change employee job title to: ")
            change_location = input("Change employee location: ")

        if cmd == "s":
            # Example gamer, Nuuk
            # Finnur allar línur tengdar gamer, nuuk
            search = input("Search for: ")

        if cmd == "c":
            # return contractor screen
            pass

        if cmd == "b":
            return ui_consts.BACK


        return self
