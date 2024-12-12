from getpass import getpass

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

class LoginScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.user_note = ""

    def run(self):
        self.clear_screen()

        print(ui_consts.SEPERATOR)
        print("|")
        print("|                                                           Login")
        print("|                                             User: ___________________")
        print("|                                         Password: ___________________")
        print("|")
        print(ui_consts.SEPERATOR)
        print("")
        print("Demo cheat codes:")
        print("Username: Boss        and    Password: Man")
        print("Username: Pleb        and    Password: 1234")
        print("")

        if self.user_note != "":
            print("\n" + self.user_note)

        # email = input("Username: ")
        # password = getpass("Password: ")

        #Temp
        email = "Pleb"
        password = "1234"

        if self.ui.logic_api.authenticate_login(email,password):
            self.user_note = ""
            return ui_consts.MAIN_MENU_SCREEN
        else:
            self.user_note = "Invalid username or password."
            return self
