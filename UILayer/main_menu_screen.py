from UILayer.base_screen import BaseScreen

class MainMenuScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        print("Menu")

        input()

        return self
