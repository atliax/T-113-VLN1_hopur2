from StorageLayer.storage_api import StorageAPI

from Model import Contractor

class ContractorManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def contractor_add(self, new_contractor : Contractor) -> None:
        all_contractors = self.storage_api.contractor_get_all()
        if len(all_contractors) != 0:
            n = int(all_contractors[len(all_contractors)-1].ID[1:])
        else:
            n = 0

        n += 1
        new_id = "C" + str(n)
        new_contractor.ID = new_id

        self.storage_api.contractor_add(new_contractor)

    def contractor_remove(self, contractorID : str) -> None:
        self.storage_api.contractor_remove(contractorID)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        self.storage_api.contractor_edit(edited_contractor)

    def contractor_search(self, search_string : str) -> list[Contractor]:
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

    def contractor_get_all(self) -> list[Contractor]:
        return self.storage_api.contractor_get_all()

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        return self.storage_api.contractor_get_by_ID(contractorID)