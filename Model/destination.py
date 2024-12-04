from Model.base_model import BaseModel

class Destination(BaseModel):
    def __init__(self, id:str, country:str, airport:str, phone_nr:str, opening_hours:str, manager:str) -> None:
        self.id = id
        self.country = country
        self.airport = airport
        self.phone_nr = phone_nr
        self.opening_hours = opening_hours
        self.manager = manager

#TODO klára fallið


