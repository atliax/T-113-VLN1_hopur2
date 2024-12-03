from UILayer.base_screen import BaseScreen

class LoginScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        print("Login")
        email = input("Email: ")
        password = input("Password: ")

        if self.ui.logic_api.authenticate_login(email,password):
            return 'main_menu'
        else:
            print("Wrong password.")
            return self
