from Model.base_model import BaseModel

class Property(BaseModel):
    def __init__(self, ID : str, destinationID : str, name : str, \
                 address : str, square_meters : int, rooms : int, \
                 type : str, deleted : bool = False) -> None:
        self.ID = ID
        self.destinationID = destinationID
        self.name = name
        self.address = address
        self.square_meters = square_meters
        self.rooms = rooms
        self.type = type
        self.deleted = deleted
