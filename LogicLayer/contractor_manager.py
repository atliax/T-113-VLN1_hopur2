from StorageLayer.storage_api import StorageAPI

from Model import Contractor

class ContractorManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def contractor_add(self, new_contractor : Contractor) -> None:
        """Takes a new contractor instance and adds it to the system."""
        all_contractors = self.storage_api.contractor_get_all()
        if len(all_contractors) != 0:
            n = int(all_contractors[len(all_contractors)-1].ID[1:])
        else:
            n = 0

        n += 1
        new_id = "C" + str(n)
        new_contractor.ID = new_id

        self.storage_api.contractor_add(new_contractor)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        """Takes a contractor instance and replaces a contractor in the system that has the same ID."""
        self.storage_api.contractor_edit(edited_contractor)

    def contractor_get_all(self) -> list[Contractor]:
        """Returns a list of all the contractors that exist in the system."""
        return self.storage_api.contractor_get_all()

    def contractor_get_by_destinationID(self, destinationID: str) -> list[Contractor]:
        all_contractors : list[Contractor] = self.storage_api.contractor_get_all()
        contractors_in_dest = []
        for contractor in all_contractors:
            if contractor.destinationID == destinationID:
                contractors_in_dest.append(contractor)
        return contractors_in_dest

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        """Takes a contractor ID and returns a contractor from the system with the same ID if it exists."""
        return self.storage_api.contractor_get_by_ID(contractorID)

    def contractor_remove(self, contractorID : str) -> None:
        """Takes a contractor ID and removes it from the system."""
        self.storage_api.contractor_remove(contractorID)

    def contractor_search(self, search_string : str) -> list[Contractor]:
        """Takes a string and returns a list of contractors in the system that have attributes containing that string."""
        all_contractors : list[Contractor] = self.storage_api.contractor_get_all()
        filtered_contractors = []
        for contractor in all_contractors:
            found = False
            for attribute_value in list(contractor.__dict__.values()):
                if search_string.lower() in str(attribute_value).lower():
                    filtered_contractors.append(contractor)
                    found = True
                    break

            if not found:
                contractor_destination = self.storage_api.destination_get_by_ID(contractor.destinationID)
                if contractor_destination is not None:
                    if search_string.lower() in contractor_destination.country.lower():
                        filtered_contractors.append(contractor)

        return filtered_contractors

    def contractor_update_rating(self, contractorID : str) -> None:
        """Updates the rating of the requested contractor."""
        all_tickets = self.storage_api.ticket_get_all()

        number_of_tickets = 0.0
        rating_sum = 0.0
        new_rating = 0.0

        for ticket in all_tickets:
            if ticket.contractorID == contractorID:
                number_of_tickets += 1.0
                rating_sum += ticket.contractor_rating

        if number_of_tickets > 0:
            new_rating = rating_sum / number_of_tickets

        contractor = self.storage_api.contractor_get_by_ID(contractorID)
        contractor.rating = round(new_rating, 1)

        self.storage_api.contractor_edit(contractor)
