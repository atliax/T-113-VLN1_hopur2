from StorageLayer import StorageAPI
from LogicLayer import LogicAPI
from UILayer import UIManager

def main():
    storage = StorageAPI()
    logic = LogicAPI(storage)
    ui = UIManager(logic)
    ui.run()

if __name__ == '__main__':
    main()
