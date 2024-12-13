from Model.base_model import BaseModel

class Staff(BaseModel):
    def __init__(self, ID : str, destinationID : str, name : str, ssn : str, \
                 address : str, phone_home : str, phone_gsm : str, email : str, \
                 password : str, job_title : str, is_manager : bool, deleted : bool = False) -> None:
        self.ID = ID
        self.destinationID = destinationID
        self.name = name
        self.ssn = ssn
        self.address = address
        self.phone_home = phone_home
        self.phone_gsm = phone_gsm
        self.email = email
        self.password = password
        self.job_title = job_title
        self.is_manager = is_manager
        self.deleted = deleted
