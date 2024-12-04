from Model import Destination

class Staff:
    def __init__(self, id:str, name:str, ssn:str, address:str, phone_home:str, phone_gsm:str, email:str, password:str, destination:Destination, job_title:str, is_manager:str) -> None:
        self.id = id
        self.name = name
        self.ssn = ssn
        self.address = address
        self.phone_home = phone_home
        self.phone_gsm = phone_gsm
        self.email = email
        self.password = password
        self.destination = destination
        self.job_title = job_title
        self.is_manager = is_manager

#TODO klára fallið