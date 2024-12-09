from StorageLayer.base_storage import BaseStorage
from Model import Facility

class FacilityStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)
    
    def add_new_facility(self, new_facility : Facility):
        current_facility = self.load_from_file()
        current_facility.append(new_facility)
        self.save_to_file(current_facility)

    def remove_facility(self, remove_id: str):
        current_facility: list[Facility] = self.load_from_file()
        new_facility_list = []
        for facility in current_facility:
            if facility.facilityID != remove_id:
                new_facility_list.append(new_facility)
        self.save_to_file(new_facility_list)