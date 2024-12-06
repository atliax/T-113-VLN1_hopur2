from Model.base_model import BaseModel

class Facility(BaseModel):
    def __init__(self, id:str, propertyID:str,description:str,condition:str) -> None:
        self.id = id
        self.propertyID = propertyID
        self.description = description
        self.condition = condition

#TODO klára fallið



