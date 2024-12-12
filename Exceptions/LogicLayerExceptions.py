class LogicLayerException(Exception):
    pass

class IDNotFoundError(LogicLayerException):
    def __init__(self, message) -> None:
        super().__init__(message)
