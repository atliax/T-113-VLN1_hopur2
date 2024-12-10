from StorageLayer.base_storage import BaseStorage

from Model import Facility

class FacilityStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)
    
    def facility_add(self, new_facility : Facility) -> None:
        current_facilities : list[Facility] = self.load_from_file()
        current_facilities.append(new_facility)
        self.save_to_file(current_facilities)

    def facility_remove(self, facilityID : str) -> None:
        current_facilities : list[Facility] = self.load_from_file()

        updated_facilites = []
        for facility in current_facilities:
            if facility.facilityID != facilityID:
                updated_facilites.append(facility)

        self.save_to_file(updated_facilites)

    def facility_edit(self, edited_facility : Facility) -> None:
        current_facilities : list[Facility] = self.load_from_file()

        updated_facilities = []
        for facility in current_facilities:
            if facility.facilityID == edited_facility.facilityID:
                updated_facilities.append(edited_facility)
            else:
                updated_facilities.append(facility)

        self.save_to_file(updated_facilities)

    def facility_get_all(self) -> list[Facility]:
        return self.load_from_file()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        current_facilities : list[Facility] = self.load_from_file()
        for facility in current_facilities:
            if facility.facilityID == facilityID:
                return facility

    def facility_search(self, search_string : str) -> list[Facility]:
        return []
