from StorageLayer.base_storage import BaseStorage

from Model import Ticket

class TicketStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)
