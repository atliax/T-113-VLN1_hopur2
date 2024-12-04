from UILayer.base_screen import BaseScreen

class StaffScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Staff")

        cmd = input("Command: ")

        return self
