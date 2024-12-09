from StorageLayer.base_storage import BaseStorage

from Model import Destination

class DestinationStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)

    def add_new_destination(self,new_destination : Destination):
        current_destinations = self.load_from_file()
        current_destinations.append(new_destination)
        self.save_to_file(current_destinations)

    def edit_destination(self, destinations):
        self.save_to_file(destinations)
        