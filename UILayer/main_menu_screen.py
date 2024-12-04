from UILayer.base_screen import BaseScreen
from Model import Staff

class MainMenuScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        logged_in_user : Staff = self.ui.logic_api.get_logged_in_staff()

        print(self.separator_line)
        print( "|")
        print(f"|    Hello {logged_in_user.name}!")
        print( "|    What would you like to view?")
        print( "|")
        print( "|    [P] Properties")
        print( "|    [S] Staff")
        print( "|    [T] Tickets")
        print( "|    [D] Destinations")
        print( "|")
        print( "|    [L] Log out")
        print( "|")
        print(self.separator_line)

        cmd = input("Command: ")

        return self
