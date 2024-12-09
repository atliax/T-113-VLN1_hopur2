from Model import Contractor

class ContractorManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api

    def get_all_contractors(self):
        return self.storage_api.get_all_contractors()

    def add_new_contractor(self, new_contractor : Contractor):
        all_contractor = self.storage_api.get_all_contractors()
        n = int(all_contractor[len(all_contractor)-1].contractorID[1:])
        n += 1
        new_id = "C" + str(n)
        new_contractor.contractorID = new_id


        self.storage_api.add_new_contractor(new_contractor)

    def remove_contractor(self):
        pass

    def edit_contractor(self):
        pass

    def search_contractor(self):
        pass
