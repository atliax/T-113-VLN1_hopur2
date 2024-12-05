from StorageLayer.base_storage import BaseStorage

class TicketStorage(BaseStorage):
    def __init__(self, filename):
        super().__init__(filename)