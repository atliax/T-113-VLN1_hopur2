import json

class BaseModel:
    def __init__():
        pass

    def toJson(self) -> str:
        """Returns all the attributes of the class instance as a JSON string"""
        return json.dumps(self, default=lambda instance: instance.__dict__)
