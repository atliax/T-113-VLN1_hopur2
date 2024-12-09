from StorageLayer import StorageAPI

class ReportManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api
