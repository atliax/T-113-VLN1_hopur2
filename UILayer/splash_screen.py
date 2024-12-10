from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

class SplashScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)

    def run(self):
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

        input("Press enter to continue.")

        return ui_consts.LOGIN_SCREEN