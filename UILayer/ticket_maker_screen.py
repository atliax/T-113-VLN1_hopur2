from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class TicketmakerScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

print("Main menu > Tickets > Ticket Maker")