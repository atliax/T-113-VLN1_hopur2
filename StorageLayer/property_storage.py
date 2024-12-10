from StorageLayer.base_storage import BaseStorage

from Model import Property

class PropertyStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def property_add(self, new_property : Property) -> None:
        current_properties = self.load_from_file()
        current_properties.append(new_property)
        self.save_to_file(current_properties)

    def property_remove(self, propertyID : str) -> None:
        current_properties = self.load_from_file()

        updated_properties = []
        for property in current_properties:
            if property.propertyID != propertyID:
                updated_properties.append(property)

        self.save_to_file(updated_properties)

    def property_edit(self, edited_property : Property) -> None:
        current_properties : list[Property] = self.load_from_file()

        updated_properties = []
        for property in current_properties:
            if property.propertyID == edited_property.propertyID:
                updated_properties.append(edited_property)
            else:
                updated_properties.append(property)

        self.save_to_file(updated_properties)

    def property_get_all(self) -> list[Property]:
        return self.load_from_file()

    def property_get_by_ID(self, propertyID : str) -> Property:
        current_properties : list[Property] = self.load_from_file()
        for property in current_properties:
            if property.propertyID == propertyID:
                return property

    def property_search(self, search_string : str) -> list[Property]:
        return []
