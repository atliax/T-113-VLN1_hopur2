from Model.base_model import BaseModel

class Contractor(BaseModel):
    def __init__(self, ID : str, destinationID : str, rating : float, \
                 name : str, contact : str, phone : str, address : str, \
                 opening_hours : str, contractor_type : str) -> None:
        self.ID = ID
        self.destinationID = destinationID
        self.rating = rating
        self.name = name
        self.contact = contact
        self.phone = phone
        self.address = address
        self.opening_hours = opening_hours
        self.contractor_type = contractor_type
