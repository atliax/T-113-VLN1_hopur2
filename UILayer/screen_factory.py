from UILayer.login_screen import LoginScreen
from UILayer.main_menu_screen import MainMenuScreen
from UILayer.properties_screen import PropertiesScreen
from UILayer.tickets_screen import TicketsScreen
from UILayer.staff_screen import StaffScreen
from UILayer.destination_screen import DestinationScreen
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
            case 'properties':
                return PropertiesScreen(self.ui)
            case 'tickets':
                return TicketsScreen(self.ui)
            case 'staff':
                return StaffScreen(self.ui)
            case 'destinations':
                return DestinationScreen(self.ui)

        # TODO, other screens

        #error when unknown screen?