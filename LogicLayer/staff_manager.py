from Model import Staff
from Model import Destination

class StaffManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api
        self.logged_in_staff = None
        self.tmp_destination = None

    def authenticate_login(self,email,password):
        if email == 'test' and password == 'test':
            self.logged_in_staff = Staff("1","Torfi","090488-2959","Grundargata 12", "555-5555", "867-5309", "siggi@nanair.is", "flubber", None,"Yfirmaður rekstrarsviðs",True)
            self.tmp_destination = Destination("A1","Ísland","Keflavík","555-5556","24/7",self.logged_in_staff.id)
            self.logged_in_staff.destinationID = self.tmp_destination.id
            return True

        return False
    
    def get_logged_in_staff(self) -> Staff:
        return self.logged_in_staff