from StorageLayer import StorageAPI

from Model import Destination

class DestinationManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def destination_add(self, new_destination : Destination) -> None:
        """Takes a new destination instance and adds it to the system."""
        n = int(self.storage_api.ticket_get_highest_ID()[1:])
        n += 1
        new_id = "D" + str(n)
        new_destination.ID = new_id

        self.storage_api.destination_add(new_destination)

    def destination_edit(self, edited_destination) -> None:
        """Takes a destination instance and replaces a destination in the system that has the same ID."""
        self.storage_api.destination_edit(edited_destination)

    def destination_get_all(self) -> list[Destination]:
        """Returns a list of all the destinations that exist in the system."""
        return self.storage_api.destination_get_all()

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        """Takes a destination ID and returns a destination from the system with the same ID if it exists."""
        return self.storage_api.destination_get_by_ID(destinationID)
