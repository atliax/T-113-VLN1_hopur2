class StorageLayerException(Exception):
    pass

class FileWriteError(StorageLayerException):
    """Raised when there are errors during file writing."""
    def __init__(self, message) -> None:
        super().__init__(message)

class FileReadError(StorageLayerException):
    """Raised when there are errors during file reading."""
    def __init__(self, message) -> None:
        super().__init__(message)
