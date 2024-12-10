from StorageLayer import StorageAPI

from Model import Destination

class DestinationManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def destination_get_all(self) -> list[Destination]:
        return self.storage_api.destination_get_all()

    def destination_add(self, new_destination : Destination) -> None:
        all_destinations = self.destination_get_all()
        n = int(all_destinations[len(all_destinations)-1].destinationID[1:])
        n += 1
        new_id = "D" + str(n)
        new_destination.destinationID = new_id
        #new_destination = f"{new_id}, {new_destination}"
        #new_destination = new_destination.split(",")
        #new_destination_instance = Destination(new_destination[0],new_destination[1],new_destination[2],new_destination[3],new_destination[4],new_destination[5])
        self.storage_api.destination_add(new_destination)

    def destination_edit(self, edited_destination) -> None:
        self.storage_api.destination_edit(edited_destination)

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        return self.storage_api.destination_get_by_ID(destinationID)
