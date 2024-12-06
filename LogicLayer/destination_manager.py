from Model import Destination

class DestinationManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api

    def get_all_destinations(self):
        return self.storage_api.get_all_destinations()

    def add_new_destination(self, new_destination):
        new_destination = new_destination.split(",")
        new_destination_instance = Destination(new_destination[0],new_destination[1],new_destination[2],new_destination[3],new_destination[4],new_destination[5])
        self.storage_api.add_new_destination(new_destination_instance)
        return

#   def __init__(self) -> None:
#       self.properties_by_destination = self.load_properties()

#   def load_properties(self):
#       """Loads from text file"""

#   def get_properties(self, destination: str):
#       """Return a list of properties for selected destination"""
#       return self.properties_by_destination.get(destination, [])