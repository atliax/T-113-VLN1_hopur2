from UILayer.login_screen import LoginScreen
from UILayer.menu_screen import MenuScreen

class ScreenFactory:
    def __init__(self, ui):
        self.ui = ui

    def create_screen(self, screen_name):
        if screen_name == 'login':
            return LoginScreen(self.ui)
        elif screen_name == 'menu':
            return MenuScreen(self.ui)

        # TODO, other screens

        #error when unknown screen?