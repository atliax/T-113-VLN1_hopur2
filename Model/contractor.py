from Model.base_model import BaseModel

class Contractor(BaseModel):
    def __init__(self, destinationID:str, contractorID:str, rating:float, name:str, contact:str, phone:str, address:str, opening_hours:str, contractor_type:str) -> None:
        self.destinationID = destinationID
        self.contractorID = contractorID
        self.rating = rating
        self.name = name
        self.contact = contact
        self.phone = phone
        self.address = address
        self.opening_hours = opening_hours
        self.contractor_type = contractor_type

