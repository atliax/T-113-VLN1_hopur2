from UILayer.base_screen import BaseScreen

class PropertiesScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        cmd = input("Command: ")

        return self
