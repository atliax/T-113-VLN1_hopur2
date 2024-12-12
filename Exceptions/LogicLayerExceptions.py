class LogicLayerException(Exception):
    pass

class IDNotFoundError(LogicLayerException):
    """Raised when a requested Model instance does not exist in the system."""
    def __init__(self, message) -> None:
        super().__init__(message)
