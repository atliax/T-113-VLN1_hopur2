from Model.base_model import BaseModel

class Report(BaseModel):
    def __init__(self, reportID:str, staff:str, notes:str, cost:float, date:str, contractorID:str, contractor_review:str, contractor_rating:str, contractor_fee:str) -> None:
        self.reportID = reportID
        self.staff = staff
        self.notes = notes
        self.cost = cost
        self.date = date
        self.contractorID = contractorID
        self.contractor_review = contractor_review
        self.contractor_rating = contractor_rating
        self.contractor_fee = contractor_fee

#TODO klára fallið