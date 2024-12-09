from StorageLayer.storage_api import StorageAPI

from Model import Property

class PropertyManager:
    def __init__(self, storage_api):
        self.storage_api : StorageAPI = storage_api

    def get_all_properties(self):
        return self.storage_api.get_all_properties()

    # [A] Add a property
    def property_add(self, new_property : Property):
        all_properties = self.storage_api.get_all_properties()
        n = int(all_properties[len(all_properties)-1].propertyID[1:])
        n += 1
        new_id = "P" + str(n)
        new_property.propertyID = new_id

        self.storage_api.property_add(new_property)


    # [R] Remove a property
    def property_remove():
        pass

    # [E] Edit a property
    def property_edit():
        pass

    # [S] Search for
    def property_search():
        pass

    # [V] View facilities
    def view_facilities():
        pass