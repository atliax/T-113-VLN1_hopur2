from Model.base_model import BaseModel

class Destination(BaseModel):
    def __init__(self, ID : str, managerID : str, country : str, \
                 airport : str, phone : str, opening_hours : str) -> None:
        self.ID = ID
        self.managerID = managerID
        self.country = country
        self.airport = airport
        self.phone = phone
        self.opening_hours = opening_hours
