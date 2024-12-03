from UILayer.login_screen import LoginScreen
from UILayer.main_menu_screen import MainMenuScreen
from UILayer.splash_screen import SplashScreen

class ScreenFactory:
    def __init__(self, ui):
        self.ui = ui

    def create_screen(self, screen_name):
        match screen_name:
            case 'login':
                return LoginScreen(self.ui)
            case 'main_menu':
                return MainMenuScreen(self.ui)
            case 'splash':
                return SplashScreen(self.ui)

        # TODO, other screens

        #error when unknown screen?