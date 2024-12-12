from StorageLayer.storage_api import StorageAPI

from Model import Property

class PropertyManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api

    def property_get_all(self) -> list[Property]:
        return self.storage_api.property_get_all()

    def property_get_by_ID(self, propertyID : str) -> Property:
        return self.storage_api.property_get_by_ID(propertyID)

    # [A] Add a property
    def property_add(self, new_property : Property) -> None:
        all_properties = self.storage_api.property_get_all()
        if len(all_properties) != 0:
            n = int(all_properties[len(all_properties)-1].ID[1:])
        else:
            n = 0

        n += 1
        new_id = "P" + str(n)
        new_property.ID = new_id

        self.storage_api.property_add(new_property)

    # [R] Remove a property
    def property_remove(self, propertyID : str):
        self.storage_api.property_remove(propertyID)

    # [E] Edit a property
    def property_edit(self, edited_property : Property):
        self.storage_api.property_edit(edited_property)

    # [S] Search for
    def property_search(self, search_string : str) -> list[Property]:
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
    
    def validate_property(self, propertyID : str) -> bool:
        all_property =self.storage_api.property_get_all()
        for property in all_property:
            if propertyID == property.ID:
                return True
        return False
    # [V] View facilities
    #def view_facilities():
    #    pass