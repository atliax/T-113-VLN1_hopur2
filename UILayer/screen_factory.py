from UILayer.login_screen import LoginScreen
from UILayer.main_menu_screen import MainMenuScreen
from UILayer.properties_screen import PropertiesScreen
from UILayer.tickets_screen import TicketsScreen
from UILayer.staff_screen import StaffScreen
from UILayer.destination_screen import DestinationScreen
from UILayer.splash_screen import SplashScreen
from UILayer.contractor_screen import ContractorScreen

from UILayer import ui_consts

class ScreenFactory:
    def __init__(self, ui):
        self.ui = ui

    def create_screen(self, screen_name):
        match screen_name:
            case ui_consts.LOGIN:
                return LoginScreen(self.ui)
            case ui_consts.MAIN_MENU:
                return MainMenuScreen(self.ui)
            case ui_consts.SPLASH:
                return SplashScreen(self.ui)
            case ui_consts.PROPERTY:
                return PropertiesScreen(self.ui)
            case ui_consts.TICKET:
                return TicketsScreen(self.ui)
            case ui_consts.STAFF:
                return StaffScreen(self.ui)
            case ui_consts.DESTINATION:
                return DestinationScreen(self.ui)
            case ui_consts.CONTRACTOR:
                return ContractorScreen(self.ui)


        # TODO, other screens

        #error when unknown screen?