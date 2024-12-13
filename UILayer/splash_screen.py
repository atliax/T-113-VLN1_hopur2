# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class SplashScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)

    def run(self) -> str | None:
        self.clear_screen()

        print("          ___           ___           ___                    ___                       ___     ")
        print("         /\\__\\         /\\  \\         /\\__\\                  /\\  \\          ___        /\\  \\    ")
        print("        /::|  |       /::\\  \\       /::|  |                /::\\  \\        /\\  \\      /::\\  \\   ")
        print("       /:|:|  |      /:/\\:\\  \\     /:|:|  |               /:/\\:\\  \\       \\:\\  \\    /:/\\:\\  \\  ")
        print("      /:/|:|  |__   /::\\~\\:\\  \\   /:/|:|  |__            /::\\~\\:\\  \\      /::\\__\\  /::\\~\\:\\  \\ ")
        print("     /:/ |:| /\\__\\ /:/\\:\\ \\:\\__\\ /:/ |:| /\\__\\          /:/\\:\\ \\:\\__\\  __/:/\\/__/ /:/\\:\\ \\:\\__\\")
        print("     \\/__|:|/:/  / \\/__\\:\\/:/  / \\/__|:|/:/  /          \\/__\\:\\/:/  / /\\/:/  /    \\/_|::\\/:/  /")
        print("         |:/:/  /       \\::/  /      |:/:/  /                \\::/  /  \\::/__/        |:|::/  / ")
        print("         |::/  /        /:/  /       |::/  /                 /:/  /    \\:\\__\\        |:|\\/__/  ")
        print("         /:/  /        /:/  /        /:/  /                 /:/  /      \\/__/        |:|  |    ")
        print("         \\/__/         \\/__/         \\/__/                  \\/__/                     \\|__|    ")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

        input(ui_consts.MSG_ENTER_CONTINUE)

        return ui_consts.LOGIN_SCREEN
