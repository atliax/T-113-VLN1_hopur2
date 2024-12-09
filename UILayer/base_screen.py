import os
from UILayer import ui_consts

class BaseScreen:
    def __init__(self, ui):
        from UILayer import UIManager #lazy import for VSCode completion
        self.ui : UIManager = ui

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self):
        raise NotImplementedError("Subclass needs to implement render()")
