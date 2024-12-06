from StorageLayer.base_storage import BaseStorage

class DestinationStorage(BaseStorage):
    def __init__(self, filename):
        super().__init__(filename)

    #def add_new_destination(new_destination):
        