from StorageLayer.storage_api import StorageAPI

from Model import Contractor

class ContractorManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def contractor_add(self, new_contractor : Contractor) -> None:
        all_contractors = self.storage_api.contractor_get_all()
        n = int(all_contractors[len(all_contractors)-1].ID[1:])
        n += 1
        new_id = "C" + str(n)
        new_contractor.ID = new_id

        self.storage_api.contractor_add(new_contractor)

    def contractor_remove(self, contractorID : str) -> None:
        self.storage_api.contractor_remove(contractorID)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        self.storage_api.contractor_edit(edited_contractor)

    def contractor_search(self, search_string : str) -> list[Contractor]:
        return self.storage_api.contractor_search(search_string)

    def contractor_get_all(self) -> list[Contractor]:
        return self.storage_api.contractor_get_all()
