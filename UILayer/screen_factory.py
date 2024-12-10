from UILayer.login_screen import LoginScreen
from UILayer.main_menu_screen import MainMenuScreen
from UILayer.property_screen import PropertyScreen
from UILayer.ticket_screen import TicketScreen
from UILayer.staff_screen import StaffScreen
from UILayer.destination_screen import DestinationScreen
from UILayer.splash_screen import SplashScreen
from UILayer.contractor_screen import ContractorScreen
from UILayer.facility_screen import FacilityScreen

from UILayer import ui_consts

class ScreenFactory:
    def __init__(self, ui):
        self.ui = ui

    def create_screen(self, screen_name):
        match screen_name:
            case ui_consts.CONTRACTOR_SCREEN:
                return ContractorScreen(self.ui)
            case ui_consts.DESTINATION_SCREEN:
                return DestinationScreen(self.ui)
            case ui_consts.FACILITY_SCREEN:
                return FacilityScreen(self.ui)
            case ui_consts.LOGIN_SCREEN:
                return LoginScreen(self.ui)
            case ui_consts.MAIN_MENU_SCREEN:
                return MainMenuScreen(self.ui)
            case ui_consts.PROPERTY_SCREEN:
                return PropertyScreen(self.ui)
            case ui_consts.SPLASH_SCREEN:
                return SplashScreen(self.ui)
            case ui_consts.STAFF_SCREEN:
                return StaffScreen(self.ui)
            case ui_consts.TICKET_SCREEN:
                return TicketScreen(self.ui)

        # TODO, other screens?

        #error when unknown screen?