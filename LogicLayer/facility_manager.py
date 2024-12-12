from StorageLayer import StorageAPI

from Model import Facility

class FacilityManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api
        self.selected_property = None

    def set_selected_property(self, propertyID) -> None:
        self.selected_property = propertyID

    def get_selected_property(self) -> str:
        return self.selected_property

    def facility_add(self, new_facility : Facility) -> None:
        all_facilities = self.storage_api.facility_get_all()
        n = int(all_facilities[len(all_facilities)-1].ID[1:])
        n += 1
        new_id = "F" + str(n)
        new_facility.ID = new_id

        self.storage_api.facility_add(new_facility)

    def facility_remove(self, facilityID : str) -> None:
        self.storage_api.facility_remove(facilityID)

    def facility_get_all(self) -> list[Facility]:
        return self.storage_api.facility_get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        return self.storage_api.facility_get_by_ID(facilityID)
    
    # [S] to search for a facility
    def facility_search(self, search_string : str):
        all_facilities : list[Facility] = self.facility_get_by_propertyID(self.selected_property)

        filteded_facilities = []
        for facility in all_facilities:
            for attribute_value in list(facility.__dict__.values()):
                if search_string.lower() in str(attribute_value).lower():
                    filteded_facilities.append(facility)
                    break

        return filteded_facilities
    
#var að prufa ef attributes eru "none" en er buið að laga það þannig það geti aldrei verið
#def facility_search(self, search_string: str):
 #   all_facilities: list[Facility] = self.facility_get_by_propertyID(self.selected_property)
#
#   filtered_facilities = []
#   for facility in all_facilities:
#       for attribute_value in facility.__dict__.values():
#           if attribute_value is not None and search_string.lower() in str(attribute_value).lower():
#               filtered_facilities.append(facility)
#               break

#    return filtered_facilities

    # [E] to edit a facility

    def facility_edit(self, edited_facility : Facility):
        self.storage_api.facility_edit(edited_facility)

    def facility_get_by_propertyID(self, propertyID : str) -> list[Facility]:
        all_facilities = self.storage_api.facility_get_all()

        filtered_facilities = []

        for facility in all_facilities:
            if facility.propertyID == propertyID:
                filtered_facilities.append(facility)

        return filtered_facilities

    def facility_validate(self, facilityID : str, facility_list : list[Facility]) -> bool:
        if len(facility_list) == 0:
            return True
        for facility in facility_list:
            if facilityID == facility.ID:
                return True
        return False