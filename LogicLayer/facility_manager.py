from Model import Facility

from StorageLayer import StorageAPI

class FacilityManager:
    def __init__(self, storage_api):
        self.storage_api : StorageAPI = storage_api

    def get_all_facilities(self):
        return self.storage_api.get_all_facilities()

    def add_new_facility(self, new_facility : Facility):
        all_facilities = self.storage_api.get_all_facilities()
        n = int(all_facilities[len(all_facilities)-1].facilityID[1:])
        n += 1
        new_id = "F" + str(n)
        new_facility.facilityID = new_id

    def edit_facility():
        pass

    def view_details_by_ID(self, facilityID):
        all_facilities : list[Facility] = self.storage_api.get_all_facilities()
        for facility in all_facilities:
             if facility.facilityID == facilityID:
                  return facility
             
    def remove_facility(self, remove_id: str):
        # validation
        
        # ef í lagi:
        self.storage_api.remove_facility(remove_id)

    def search_facility():
        pass

    def get_facilities_by_propertyID(self, propertyID):
        all_facilities = self.storage_api.get_all_facilities()
        filtered_facilities = []
        for facility in all_facilities:
            if facility.propertyID == propertyID:
                filtered_facilities.append(facility)
        return filtered_facilities
