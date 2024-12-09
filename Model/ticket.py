from Model.base_model import BaseModel

class Ticket(BaseModel):
    def __init__(self, ticketID : str, facilityID : str, reportID : str, \
                 propertyID : str, priority : str, title : str, description : str, \
                 status : str, recurring : bool, recurring_days : int, \
                 open_date : str) -> None:
        self.ticketID = ticketID
        self.facilityID = facilityID
        self.reportID = reportID
        self.propertyID = propertyID
        self.priority = priority
        self.title = title
        self.description = description
        self.status = status
        self.recurring = recurring
        self.recurring_days = recurring_days
        self.open_date = open_date
