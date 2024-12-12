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
    """Class to handle creation of BaseScreen child class instances."""
    def __init__(self, logic_api):
        self.logic_api = logic_api

    def create_screen(self, screen_name : str):
        """Creates an instance of the requested screen based on its string ID.
        Deliberately no return type hint since it would be too messy."""
        match screen_name:
            case ui_consts.CONTRACTOR_SCREEN:
                return ContractorScreen(self.logic_api)
            case ui_consts.DESTINATION_SCREEN:
                return DestinationScreen(self.logic_api)
            case ui_consts.FACILITY_SCREEN:
                return FacilityScreen(self.logic_api)
            case ui_consts.LOGIN_SCREEN:
                return LoginScreen(self.logic_api)
            case ui_consts.MAIN_MENU_SCREEN:
                return MainMenuScreen(self.logic_api)
            case ui_consts.PROPERTY_SCREEN:
                return PropertyScreen(self.logic_api)
            case ui_consts.SPLASH_SCREEN:
                return SplashScreen(self.logic_api)
            case ui_consts.STAFF_SCREEN:
                return StaffScreen(self.logic_api)
            case ui_consts.TICKET_SCREEN:
                return TicketScreen(self.logic_api)
            case _:
                return None
