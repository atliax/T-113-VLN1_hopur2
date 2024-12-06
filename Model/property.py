from Model.base_model import BaseModel

class Property(BaseModel):
    def __init__(self, propertyID:str, destinationID:str, name:str, address:str, square_meters:int, rooms:int, type:str) -> None:
        self.propertyID = propertyID
        self.destinationID = destinationID
        self.name = name
        self.address = address
        self.square_meters = square_meters
        self.rooms = rooms
        self.type = type

#TODO klára fallið
