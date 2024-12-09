from StorageLayer.base_storage import BaseStorage
from Model import Contractor

class ContractorStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def add_new_contractor(self, new_contractor : Contractor) -> None:
        current_contractors : list[Contractor] = self.load_from_file()
        current_contractors.append(new_contractor)
        self.save_to_file(current_contractors)

    def remove_contractor(self, contractorID: str):
        current_contractor : list[Contractor] = self.load_from_file()

        new_contractor_list = []
        for contractor in current_contractor:
            if contractor.contractorID != contractorID:
                new_contractor_list.append(contractor)

        self.save_to_file(new_contractor_list)
        
    def edit_contractor(self, edit_contractor: str):
        self.save_to_file(edit_contractor)
