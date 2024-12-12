from Model.base_model import BaseModel

class Ticket(BaseModel):
    def __init__(self, ID : str, facilityID : str,
                 propertyID : str, priority : str, title : str, description : str, \
                 open : bool, status : str, recurring : bool, recurring_days : int, \
                 open_date : str, close_date : str, staffID : str, report : str, cost : int, 
                 contractorID : str, contractor_review : str, contractor_rating : float,
                 contractor_fee : int) -> None:
        self.ID = ID
        self.facilityID = facilityID
        self.propertyID = propertyID
        self.priority = priority
        self.title = title
        self.description = description
        self.open = open
        self.status = status
        self.recurring = recurring
        self.recurring_days = recurring_days
        self.open_date = open_date
        self.close_date = close_date
        self.staffID = staffID
        self.report = report
        self.cost = cost
        self.contractorID = contractorID
        self.contractor_review = contractor_review
        self.contractor_rating = contractor_rating
        self.contractor_fee = contractor_fee