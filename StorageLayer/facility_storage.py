from StorageLayer.base_storage import BaseStorage
from Model import Facility

class FacilityStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)
    
    def add_new_facility(self, new_facility : Facility) -> None:
        current_facilities : list[Facility] = self.load_from_file()
        current_facilities.append(new_facility)
        self.save_to_file(current_facilities)

    def remove_facility(self, facilityID: str) -> None:
        current_facilities: list[Facility] = self.load_from_file()

        updated_facilites = []
        for facility in current_facilities:
            if facility.facilityID != facilityID:
                updated_facilites.append(facility)

        self.save_to_file(updated_facilites)
