from Model import Destination

class Contractor:
    def __init__(self, id:str, rating:float, name:str, contact:str, phone_nr:str, address:str, opening_hours:str, destination:Destination, contractor_type:str) -> None:
        self.id = id
        self.rating = rating
        self.name = name
        self.contact = contact
        self.phone_nr = phone_nr
        self.address = address
        self.opening_hours = opening_hours
        self.destination = destination
        self.contractor_type = contractor_type

    #TODO - klára föllin