from StorageLayer import StorageAPI

from Model import Facility

class FacilityManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api

    def facility_add(self, new_facility : Facility) -> None:
        all_facilities = self.storage_api.facility_get_all()
        n = int(all_facilities[len(all_facilities)-1].ID[1:])
        n += 1
        new_id = "F" + str(n)
        new_facility.ID = new_id

        self.storage_api.facility_add(new_facility)

    def facility_remove(self, facilityID : str) -> None:
        # TODO validation

        # ef í lagi:
        self.storage_api.facility_remove(facilityID)


    def facility_get_all(self) -> list[Facility]:
        return self.storage_api.facility_get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        return self.storage_api.facility_get_by_ID(facilityID)
    

    # [S] to search for a facility
    def facility_search(self, search_string : str):
        return self.storage_api.facility_search(search_string)

    # [E] to edit a facility
    def facility_edit(self, edited_facility : Facility):
        self.storage_api.facility_edit(edited_facility)

        return filtered_facilities
