from Model.base_model import BaseModel

class Staff(BaseModel):
    def __init__(self, id:str, name:str, ssn:str, address:str, phone_home:str, phone_gsm:str, email:str, password:str, destinationID:str, job_title:str, is_manager:bool) -> None:
        self.id = id
        self.name = name
        self.ssn = ssn
        self.address = address
        self.phone_home = phone_home
        self.phone_gsm = phone_gsm
        self.email = email
        self.password = password
        self.destinationID = destinationID
        self.job_title = job_title
        self.is_manager = is_manager

#TODO klára fallið