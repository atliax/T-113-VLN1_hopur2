from Model import Amenity
from Model import Report

class Ticket:
    def __init__(self, id:str, priority:str, title:str, amenity:Amenity, status:str, report:Report, recurring:bool, recurring_days:int,open_date:str) -> None:
        self.id = id
        self.priority = priority
        self.title = title
        self.amenity = amenity
        self.status = status
        self.report = report
        self.recurring = recurring
        self.recurring_days = recurring_days
        self.open_date = open_date

#TODO klára fallið