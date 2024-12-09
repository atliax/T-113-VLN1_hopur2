from UILayer.screen_factory import ScreenFactory
from UILayer.base_screen import BaseScreen
from LogicLayer import LogicAPI
from UILayer import ui_consts

class UIManager:
    def __init__(self, logic_api : LogicAPI) -> None:
        self.logic_api = logic_api
        self.running = True
        self.screen_factory = ScreenFactory(self)
        self.screen_stack = []
        self.start_screen = self.screen_factory.create_screen(ui_consts.SPLASH_SCREEN)
        self.current_screen = self.start_screen

    def run(self) -> None:
        while self.running:
            next_screen = self.current_screen.run()

            if isinstance(next_screen, str):
                match next_screen:
                    case ui_consts.CMD_QUIT:
                        print(ui_consts.MSG_EXIT)
                        self.running = False
                    case ui_consts.CMD_LOGOUT:
                        self.logic_api.logout()
                        self.screen_stack = []
                        self.current_screen = self.start_screen
                    case ui_consts.CMD_BACK:
                        self.pop_screen()
                    case _:
                        self.push_screen(self.screen_factory.create_screen(next_screen))

    def push_screen(self, screen : BaseScreen) -> None:
        self.screen_stack.append(self.current_screen)
        self.current_screen = screen

    def pop_screen(self) -> None:
        if self.screen_stack:
            self.current_screen = self.screen_stack.pop()
        else:
            self.running = False
