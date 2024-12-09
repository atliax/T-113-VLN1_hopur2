from Model.base_model import BaseModel

class Contractor(BaseModel):
    def __init__(self, contractorID:str, destinationID:str, rating:float, name:str, contact:str, phone:str, address:str, opening_hours:str, contractor_type:str) -> None:
        self.contractorID = contractorID
        self.name = name
        self.contractor_type = contractor_type        
        self.destinationID = destinationID
        self.contact = contact
        self.rating = rating
        self.contact = contact
        self.phone = phone
        self.address = address
        self.opening_hours = opening_hours


