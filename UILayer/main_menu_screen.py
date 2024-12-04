from UILayer.base_screen import BaseScreen

class MainMenuScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        username = self.ui.logic_api.get_logged_in_user()

        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("|")
        print(f"|    Hello {username}!")
        print("|    What would you like to view?")
        print("|")
        print("|    [P] Properties")
        print("|    [S] Staff")
        print("|    [T] Tickets")
        print("|    [D] Destinations")
        print("|")
        print("|    [L] Log out")
        print("|")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

        cmd = input("Command: ")

        return self
