from StorageLayer.base_storage import BaseStorage

from Model import Report

class ReportStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)
