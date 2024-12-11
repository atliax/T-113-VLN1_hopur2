from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

class MainMenuScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def run(self):
        self.clear_screen()

        logged_in_user = self.ui.logic_api.get_logged_in_staff()

        print("Main Menu")
        print(ui_consts.SEPERATOR)
        print( "|")
        print(f"|    Hello {logged_in_user.name}!")
        print( "|    What would you like to view?")
        print( "|")
        print( "|    [P] Properties")
        print( "|    [T] Tickets")
        print( "|    [S] Staff")
        print( "|    [D] Destinations")
        print( "|")
        print( "|    [L] Log out")
        print( "|    [X] Exit")
        print( "|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        match cmd:
            case "p":
                return ui_consts.PROPERTY_SCREEN
            case "t":
                return ui_consts.TICKET_SCREEN
            case "s":
                return ui_consts.STAFF_SCREEN
            case "d":
                return ui_consts.DESTINATION_SCREEN
            case "l":
                return ui_consts.CMD_LOGOUT
            case "x":
                return ui_consts.CMD_QUIT

        return self
