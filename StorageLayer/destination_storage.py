from StorageLayer.base_storage import BaseStorage

from Model import Destination

class DestinationStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def destination_add(self, new_destination : Destination) -> None:
        current_destinations : list[Destination] = self.load_from_file()

        current_destinations.append(new_destination)

        self.save_to_file(current_destinations)

    def destination_remove(self, destinationID : str) -> None:
        current_destinations : list[Destination] = self.load_from_file()

        new_destination_list = []
        for destination in current_destinations:
            if destination.destinationID != destinationID:
                new_destination_list.append(destination)

        self.save_to_file(new_destination_list)

    def destination_edit(self, edited_destination : Destination) -> None:
        current_destinations : list[Destination] = self.load_from_file()

        new_destination_list = []
        for destination in current_destinations:
            if destination.destinationID == edited_destination.destinationID:
                new_destination_list.append(edited_destination)
            else:
                new_destination_list.append(destination)

        self.save_to_file(new_destination_list)

    def destination_get_all(self) -> list[Destination]:
        return self.load_from_file()

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        current_destinations : list[Destination] = self.load_from_file()
        for destination in current_destinations:
            if destination.destinationID == destinationID:
                return destination

    def destination_search(self, search_string : str) -> list[Destination]:
        return []
