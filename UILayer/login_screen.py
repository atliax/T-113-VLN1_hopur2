from UILayer.base_screen import BaseScreen

class LoginScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        print("Login")
        user = input("User: ")
        password = input("Password: ")

        if self.ui.logic_api.logic_test_function():
            print("was True")
        else:
            print("was False")

        # TODO: call some LogicAPI here to validate
        if user == 'test' and password == 'test':
            print("correct password")
            return 'menu'
        else:
            print("wrong password")
            return self
