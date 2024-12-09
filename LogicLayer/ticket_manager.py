from StorageLayer import StorageAPI

class TicketManager:
    def __init__(self, storage_api):
        self.storage_api : StorageAPI = storage_api
