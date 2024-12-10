from StorageLayer.base_storage import BaseStorage

from Model import Contractor

class ContractorStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def contractor_add(self, new_contractor : Contractor) -> None:
        current_contractors : list[Contractor] = self.load_from_file()
        current_contractors.append(new_contractor)
        self.save_to_file(current_contractors)

    def contractor_remove(self, contractorID: str):
        current_contractor : list[Contractor] = self.load_from_file()

        new_contractor_list = []
        for contractor in current_contractor:
            if contractor.contractorID != contractorID:
                new_contractor_list.append(contractor)

        self.save_to_file(new_contractor_list)

    def contractor_edit(self, edited_contractor : Contractor):
        current_contractors : list[Contractor] = self.load_from_file()

        new_contractor_list = []
        for contractor in current_contractors:
            if contractor.contractorID == edited_contractor.contractorID:
                new_contractor_list.append(edited_contractor)
            else:
                new_contractor_list.append(contractor)

        self.save_to_file(new_contractor_list)

    def contractor_get_all(self) -> list[Contractor]:
        return self.load_from_file()

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        current_contractors : list[Contractor] = self.load_from_file()
        for contractor in current_contractors:
            if contractor.contractorID == contractorID:
                return contractor

    def contractor_search(self, search_string : str) -> list[Contractor]:
        return []
