from UILayer.screen_factory import ScreenFactory
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class UIManager:
    """Class for switching between screens."""
    def __init__(self, logic_api) -> None:
        self.logic_api = logic_api
        self.running = True
        self.screen_factory = ScreenFactory(logic_api)
        self.start_screen = self.screen_factory.create_screen(ui_consts.SPLASH_SCREEN)
        self.screen_stack : list[BaseScreen] = []
        self.reset_screens()

    def reset_screens(self) -> None:
        """Clears the screen stack and starts back on the splash screen."""
        self.screen_stack = []
        self.screen_stack.append(self.start_screen)

    def push_screen(self, screen : BaseScreen) -> None:
        """Takes an instance of a BaseScreen child class and pushes it on the
        screen stack, therefore switching to that screen."""
        if screen is not None:
            self.screen_stack.append(screen)

    def pop_screen(self) -> None:
        """Pops the currently active screen off the screen stack, switching to
        the previously active screen."""
        if self.screen_stack:
            self.screen_stack.pop()

    def run(self) -> None:
        """Main loop for the program."""
        while self.running:
            # Run the .run() function of the screen at the top of the screen stack
            next_screen = self.screen_stack[len(self.screen_stack)-1].run()

            # If the .run() function of the last screen returned a string, it means a new screen or a command
            if isinstance(next_screen, str):
                match next_screen:
                    # quit command, exits program
                    case ui_consts.CMD_QUIT:
                        print(ui_consts.MSG_EXIT)
                        self.running = False
                    # logout command, resets the screens
                    case ui_consts.CMD_LOGOUT:
                        self.reset_screens()
                    # back command, goes back a screen
                    case ui_consts.CMD_BACK:
                        self.pop_screen()
                    # any other string, create a new screen
                    case _:
                        self.push_screen(self.screen_factory.create_screen(next_screen))
            else:
                # if the screen returned itself, do nothing and run that screen again
                pass
