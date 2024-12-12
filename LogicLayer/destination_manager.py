from StorageLayer import StorageAPI

from Model import Destination

class DestinationManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def destination_get_all(self) -> list[Destination]:
        return self.storage_api.destination_get_all()

    def destination_add(self, new_destination : Destination) -> None:
        all_destinations = self.destination_get_all()
        if len(all_destinations) != 0:
            n = int(all_destinations[len(all_destinations)-1].ID[1:])
        else:
            n = 0

        n += 1
        new_id = "D" + str(n)
        new_destination.ID = new_id

        self.storage_api.destination_add(new_destination)

    def destination_edit(self, edited_destination) -> None:
        self.storage_api.destination_edit(edited_destination)

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        return self.storage_api.destination_get_by_ID(destinationID)
