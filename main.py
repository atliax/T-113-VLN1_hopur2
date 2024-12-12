from StorageLayer import StorageAPI
from LogicLayer import LogicAPI
from UILayer import UIManager

def main():
    storage = StorageAPI()
    logic = LogicAPI(storage)
    ui = UIManager(logic)

    try:
        ui.run()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")

if __name__ == '__main__':
    main()
#