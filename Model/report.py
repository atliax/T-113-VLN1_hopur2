from Model.base_model import BaseModel

class Report(BaseModel):
    def __init__(self, id:str, staff:str, contractorID:str, notes:str, contractor_review:str, contractor_rating:str, contractor_fee:str, cost:float, date:str) -> None:
        self.id = id
        self.staff = staff
        self.contractorID = contractorID
        self.notes = notes
        self.contractor_review = contractor_review
        self.contractor_rating = contractor_rating
        self.contractor_fee = contractor_fee
        self.cost = cost
        self.date = date

#TODO klára fallið