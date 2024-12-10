from StorageLayer import StorageAPI

from Model import Facility

class FacilityManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api


    # Birtir lista af facilities     
    def facility_get_all(self) -> list[Facility]:
        return self.storage_api.facility_get_all()
    
    # Leitar að facility eftir innslegnu property ID
    def facility_get_by_propertyID(self, propertyID : str) -> list[Facility]:
        all_facilities = self.storage_api.facility_get_all()

        filtered_facilities = []

        for facility in all_facilities:
            if facility.propertyID == propertyID:
                filtered_facilities.append(facility)

        return filtered_facilities


    # [A] to add a facility
    def facility_add(self, new_facility : Facility) -> None:
        all_facilities = self.storage_api.facility_get_all()
        n = int(all_facilities[len(all_facilities)-1].facilityID[1:])
        n += 1
        new_id = "F" + str(n)
        new_facility.facilityID = new_id

        self.storage_api.facility_add(new_facility)

    # [R] to remove a facility
    def facility_remove(self, facilityID : str) -> None:
        # TODO validation

        # ef í lagi:
        self.storage_api.facility_remove(facilityID)


    # [V] to view details of facility with property ID 
    def facility_get_by_ID(self, facilityID : str) -> Facility:
        return self.storage_api.facility_get_by_ID(facilityID)
    

    # [S] to search for a facility
    def facility_search(self, search_string : str):
        return self.storage_api.facility_search(search_string)

    # [E] to edit a facility
    def facility_edit(self, edited_facility : Facility):
        self.storage_api.facility_edit(edited_facility)


