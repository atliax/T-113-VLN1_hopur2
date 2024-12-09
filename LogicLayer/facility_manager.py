from Model import Facility
#meira import?

class FacilityManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api

    def get_all_facilities(self):
        return self.storage_api.get_all_facilities()

    def add__new_facility(self, new_facility : Staff):
        all_facilities = self.storage_api.get_all_facilities()
        n = int(all_facilities[len(all_facilities)-1].facilityID[1:])
        n += 1
        new_id = "S" + str(n)
        new_facility.facilityID = new_id

    def remove_facility():
        pass

    def edit_facility():
        pass

    def view_details():
        pass

    def search_facility():
        pass