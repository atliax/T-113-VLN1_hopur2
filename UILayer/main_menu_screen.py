# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class MainMenuScreen(BaseScreen):
    def __init__(self, logic_api):
        super().__init__(logic_api)

    def run(self) -> str | None:
        self.clear_screen()

        logged_in_user = self.logic_api.get_logged_in_staff()

        if logged_in_user is None:
            print("Can't detect a logged in user.")
            print("Press enter to return to login screen.")
            return ui_consts.CMD_BACK

        print("Main Menu")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|             __   _ _______ __   _                     ______")
        print("|             | \\  | |_____| | \\  |                     _\\ _~-\\___")
        print("|             |  \\_| |     | |  \\_|             =  = ==(____AA____D")
        print("|                                                           \\_____\\___________________,-~~~~~~~`-.._")
        print("|             _______ _____  ______                         /     o O o o o o O O o o o o o o O o  |\\_")
        print("|             |_____|   |   |_____/                         `~-.__        ___..----..                  )")
        print("|             |     | __|__ |    \\_                               `---~~\\___________/------------`````")
        print("|                                                                 =  ===(_________D")
        print("|")
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

            # [P] Properties
            case "p":
                return ui_consts.PROPERTY_SCREEN

            # [T] Tickets
            case "t":
                return ui_consts.TICKET_SCREEN

            # [S] Staff
            case "s":
                return ui_consts.STAFF_SCREEN

            # [D] Destinations
            case "d":
                return ui_consts.DESTINATION_SCREEN

            # [L] Log out
            case "l":
                self.logic_api.logout()
                return ui_consts.CMD_LOGOUT

            # [X] Exit
            case "x":
                return ui_consts.CMD_QUIT

        return None
