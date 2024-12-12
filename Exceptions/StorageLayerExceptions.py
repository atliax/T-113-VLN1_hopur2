class StorageLayerException(Exception):
    pass

class FileWriteError(StorageLayerException):
    def __init__(self, message) -> None:
        super().__init__(message)

class FileReadError(StorageLayerException):
    def __init__(self, message) -> None:
        super().__init__(message)
