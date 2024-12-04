import os
from UILayer import ui_consts


class BaseScreen:
    def __init__(self, ui):
        self.ui = ui
        self.separator_line = ui_consts.SEPERATOR

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self):
        raise NotImplementedError("Subclass needs to implement render()")
