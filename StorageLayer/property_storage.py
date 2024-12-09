from StorageLayer.base_storage import BaseStorage

from Model import Property

class PropertyStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)