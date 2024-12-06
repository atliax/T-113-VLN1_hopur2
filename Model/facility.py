from Model.base_model import BaseModel

class Facility(BaseModel):
    def __init__(self, facilityID:str, propertyID:str, name:str, description:str) -> None:
        self.facilityID = facilityID
        self.propertyID = propertyID
        self.name = name
        self.description = description

#TODO klára fallið



