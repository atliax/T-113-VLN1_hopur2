import json

class BaseModel:
    def __init__():
        pass

    def toJson(self):
        return json.dumps(self, default=lambda instance: instance.__dict__)
