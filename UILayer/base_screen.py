import os

from LogicLayer import LogicAPI

class BaseScreen:
    def __init__(self, logic_api : LogicAPI):
        self.logic_api = logic_api

    def clear_screen(self) -> None:
        """Clears the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        """Main 'running' function for each screen. Each screen will implement
        its own version of it. Returns None to stay on the same screen, a string
        representing another screen or a UI manager action to perform (exit/back)."""
        raise NotImplementedError("Subclass needs to implement run()")
