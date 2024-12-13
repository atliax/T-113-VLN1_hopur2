from StorageLayer.storage_api import StorageAPI

from Model import Property

class PropertyManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api

    def property_add(self, new_property : Property) -> None:
        """Takes a new property instance and adds it to the system."""
        all_properties = self.storage_api.property_get_all()
        if len(all_properties) != 0:
            n = int(all_properties[len(all_properties)-1].ID[1:])
        else:
            n = 0

        n += 1
        new_id = "P" + str(n)
        new_property.ID = new_id

        self.storage_api.property_add(new_property)

    def property_edit(self, edited_property : Property):
        """Takes a property instance and replaces a property in the system that has the same ID."""
        self.storage_api.property_edit(edited_property)

    def property_get_all(self) -> list[Property]:
        """Returns a list of all the properties that exist in the system."""
        return self.storage_api.property_get_all()

    def property_get_by_destinationID(self, destinationID : str) -> list[Property]:
        all_properties = self.property_get_all()
        filtered_properties = []
        for property in all_properties:
            if property.destinationID == destinationID:
                filtered_properties.append(property)
        return filtered_properties

    def property_get_by_ID(self, propertyID : str) -> Property:
        """Takes a property ID and returns a property from the system with the same ID if it exists."""
        return self.storage_api.property_get_by_ID(propertyID)

    def property_remove(self, propertyID : str):
        """Takes a property ID and removes it from the system."""
        self.storage_api.property_remove(propertyID)

    def property_search(self, search_string : str) -> list[Property]:
        """Takes a string and returns a list of properties in the system that have attributes containing that string."""
        all_properties : list[Property] = self.storage_api.property_get_all()
        filtered_properties = []
        for item in all_properties:
            found = False
            for attribute_value in list(item.__dict__.values()):
                if search_string.lower() in str(attribute_value).lower():
                    filtered_properties.append(item)
                    found = True
                    break

            if not found:
                property_destination = self.storage_api.destination_get_by_ID(item.destinationID)
                if property_destination is not None:
                    if search_string.lower() in property_destination.country.lower():
                        filtered_properties.append(item)

        return filtered_properties

    def property_validate(self, propertyID : str) -> bool:
        """Takes in a property ID and returns True if it exists in the system, otherwise returns False."""
        all_property =self.storage_api.property_get_all()
        for property in all_property:
            if propertyID == property.ID:
                return True
        return False
