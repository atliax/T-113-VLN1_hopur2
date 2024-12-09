from StorageLayer.base_storage import BaseStorage
from Model import Contractor

class ContractorStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)

    def add_new_contractor(self,new_contractor : Contractor):
        current_contractor = self.load_from_file()
        current_contractor.append(new_contractor)
        self.save_to_file(current_contractor)

    def remove_contractor(self, remove_id: str):
        current_contractor: list[Contractor] = self.load_from_file()
        new_contractor_list = []
        for contractor in current_contractor:
            if contractor.contractorID != remove_id:
                new_contractor_list.append(contractor)
        self.save_to_file(new_contractor_list)
        