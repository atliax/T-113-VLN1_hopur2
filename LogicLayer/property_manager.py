class PropertyManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api

    def get_all_properties(self):
        return self.storage_api.get_all_properties()