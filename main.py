# local imports
from StorageLayer import StorageAPI
from LogicLayer import LogicAPI
from UILayer import UIManager
from UILayer.ui_consts import MSG_EXIT

def main():
    storage = StorageAPI()
    logic = LogicAPI(storage)
    ui = UIManager(logic)

    try:
        ui.run()
    except (KeyboardInterrupt, EOFError):
        print("\n"+MSG_EXIT)

if __name__ == '__main__':
    main()
