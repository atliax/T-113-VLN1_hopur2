from StorageLayer import StorageAPI

class TicketManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api
