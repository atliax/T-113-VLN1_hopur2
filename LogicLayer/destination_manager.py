from StorageLayer import StorageAPI

from Model import Destination

class DestinationManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def get_all_destinations(self) -> list[Destination]:
        return self.storage_api.get_all_destinations()

    def add_new_destination(self, new_destination) -> None:
        all_destinations = self.get_all_destinations()
        n = int(len(all_destinations)) + 1
        new_id = "D" + str(n)
        new_destination = f"{new_id}, {new_destination}"
        new_destination = new_destination.split(",")
        new_destination_instance = Destination(new_destination[0],new_destination[1],new_destination[2],new_destination[3],new_destination[4],new_destination[5])
        self.storage_api.add_new_destination(new_destination_instance)
    
    def edit_destination(self, destinations) -> None:
        self.storage_api.edit_destination(destinations)
    
    def get_destination_by_ID(self, destinationID : str) -> Destination:
        all_destinations : list[Destination] = self.storage_api.get_all_destinations()
        for destination in all_destinations:
            if destination.destinationID == destinationID:
                return destination
