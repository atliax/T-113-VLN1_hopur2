from StorageLayer.base_storage import BaseStorage

class TicketStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)