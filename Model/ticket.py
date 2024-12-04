from Model.base_model import BaseModel

class Ticket(BaseModel):
    def __init__(self, id:str, priority:str, title:str, amenityID:str, status:str, reportID:str, recurring:bool, recurring_days:int,open_date:str) -> None:
        self.id = id
        self.priority = priority
        self.title = title
        self.amenityID = amenityID
        self.status = status
        self.reportID = reportID
        self.recurring = recurring
        self.recurring_days = recurring_days
        self.open_date = open_date

#TODO klára fallið