from getpass import getpass

from UILayer.base_screen import BaseScreen

class LoginScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)
        self.user_note = ""

    def render(self):
        self.clear_screen()

        print(self.separator_line)
        print("|")
        print("|                                                           Login")
        print("|                                             User: ___________________")
        print("|                                         Password: ___________________")
        print("|")
        print(self.separator_line)
        print("")
        print("Demo cheat codes:")
        print("Username: Boss        and    Password: Man")
        print("Username: Pleb        and    Password: 1234")
        print("")

        if self.user_note != "":
            print(self.user_note)

        email = input("Username: ")
        password = getpass("Password: ")

        if self.ui.logic_api.authenticate_login(email,password):
            self.user_note = ""
            return 'main_menu'
        else:
            self.user_note = "Wrong password."
            return self
