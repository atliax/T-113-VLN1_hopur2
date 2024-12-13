from StorageLayer import StorageAPI

from Model import Facility

class FacilityManager:
    def __init__(self, storage_api : StorageAPI) -> None:
        self.storage_api = storage_api
        self.selected_property = None

    def facility_add(self, new_facility : Facility) -> None:
        """Takes a new facility instance and adds it to the system."""
        n = int(self.storage_api.facility_get_highest_ID()[1:])
        n += 1
        new_id = "F" + str(n)
        new_facility.ID = new_id

        self.storage_api.facility_add(new_facility)

    def facility_edit(self, edited_facility : Facility):
        """Takes a facility instance and replaces a facility in the system that has the same ID."""
        self.storage_api.facility_edit(edited_facility)

    def facility_get_all(self) -> list[Facility]:
        """Returns a list of all the facilities that exist in the system."""
        return self.storage_api.facility_get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        """Takes a facility ID and returns a facility from the system with the same ID if it exists."""
        return self.storage_api.facility_get_by_ID(facilityID)

    def facility_get_by_propertyID(self, propertyID : str) -> list[Facility]:
        """Takes a property ID and returns a list of facilities that correspond to that property."""
        all_facilities = self.storage_api.facility_get_all()

        filtered_facilities = []

        for facility in all_facilities:
            if facility.propertyID == propertyID:
                filtered_facilities.append(facility)

        return filtered_facilities

    def facility_get_selected_property(self) -> str:
        """Returns the property ID that is currently the 'active' property on the Facility screen."""
        return self.selected_property

    def facility_remove(self, facilityID : str) -> None:
        """Takes a facility ID and removes it from the system."""
        self.storage_api.facility_remove(facilityID)
    
    def facility_search(self, search_string : str):
        """Takes a string and returns a list of facilities in the system that have attributes containing that string. Only searches facilities matching the 'active' property ID."""
        all_facilities : list[Facility] = self.facility_get_by_propertyID(self.selected_property)

        filtered_facilities = []
        for facility in all_facilities:
            for attribute_value in list(facility.__dict__.values()):
                if search_string.lower() in str(attribute_value).lower():
                    filtered_facilities.append(facility)
                    break

        return filtered_facilities

    def facility_set_selected_property(self, propertyID) -> None:
        """Takes a property ID and sets that as the 'active' property on the Facility screen."""
        self.selected_property = propertyID

    def facility_validate(self, facilityID : str, facility_list : list[Facility]) -> bool:
        """Takes in a facility ID and a list of Facilities and returns True if the ID exists in the list, otherwise returns False."""
        for facility in facility_list:
            if facilityID == facility.ID:
                return True
        return False
