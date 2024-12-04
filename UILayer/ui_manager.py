import os

from UILayer.screen_factory import ScreenFactory

class UIManager:
    def __init__(self, logic_api):
        self.logic_api = logic_api
        self.running = True
        self.screen_factory = ScreenFactory(self)
        self.screen_stack = []
        self.current_screen = self.screen_factory.create_screen('splash')

    def run(self):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')

            next_screen = self.current_screen.render()

            if next_screen == 'quit':
                print("Exiting...")
                self.running = False
            elif next_screen == 'back':
                self.pop_screen()
            elif isinstance(next_screen, str):
                self.push_screen(self.screen_factory.create_screen(next_screen))
            elif next_screen is not None:
                self.push_screen(next_screen)

    def push_screen(self, screen):
        self.screen_stack.append(self.current_screen)
        self.current_screen = screen

    def pop_screen(self):
        if self.screen_stack:
            self.current_screen = self.screen_stack.pop()
        else:
            self.running = False
