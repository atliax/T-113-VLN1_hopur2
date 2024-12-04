from Model.base_model import BaseModel

class Property(BaseModel):
    def __init__(self, id:str, name:str, location:str, status:str, destinationID:str) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.status = status
        self.destinationID = destinationID

#TODO klára fallið
