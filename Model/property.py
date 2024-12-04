from Model import Destination

class Property:
    def __init__(self, id:str, name:str, location:str, status:str, destination:Destination) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.status = status
        self.destination  = destination

#TODO klára fallið
