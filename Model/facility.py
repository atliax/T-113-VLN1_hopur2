from Model.base_model import BaseModel

class Facility(BaseModel):
    def __init__(self, ID : str, propertyID : str, name : str, \
                 description : str) -> None:
        self.ID = ID
        self.propertyID = propertyID
        self.name = name
        self.description = description
