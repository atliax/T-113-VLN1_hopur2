import os

class BaseScreen:
    def __init__(self, ui):
        from UILayer import UIManager #lazy import so VSCode can autocomplete
        self.ui : UIManager = ui

    def clear_screen(self) -> None:
        """Clears the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        raise NotImplementedError("Subclass needs to implement render()")
