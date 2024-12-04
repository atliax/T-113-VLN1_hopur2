from UILayer.base_screen import BaseScreen

class TicketsScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Tickets")

        cmd = input("Command: ")

        return self
