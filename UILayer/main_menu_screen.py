from UILayer.base_screen import BaseScreen
from Model import Staff
from UILayer import ui_consts

class MainMenuScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        logged_in_user : Staff = self.ui.logic_api.get_logged_in_staff()

        print("Main menu")
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

        cmd = input("Command: ").upper()

        if cmd == "P":
            return ui_consts.PROPERTY
        if cmd == "T":
            return ui_consts.TICKET
        if cmd == "S":
            return ui_consts.STAFF
        if cmd == "D":
            return ui_consts.DESTINATION
        if cmd == "L":
            return ui_consts.LOGOUT
        if cmd == "X":
            return ui_consts.QUIT

        return self
