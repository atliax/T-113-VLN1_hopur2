from getpass import getpass

from UILayer.base_screen import BaseScreen

class LoginScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)
        self.user_note = ""

    def render(self):
        print("Login")

        if self.user_note != "":
            print(self.user_note)

        email = input("Email: ")
        password = getpass("Password: ")

        if self.ui.logic_api.authenticate_login(email,password):
            self.user_note = ""
            return 'main_menu'
        else:
            self.user_note = "Wrong password."
            return self
