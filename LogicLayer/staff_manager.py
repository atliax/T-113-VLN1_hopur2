from Model import Staff
from Model import Destination

class StaffManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api
        self.logged_in_staff = None
        self.tmp_destination = None

    def authenticate_login(self,email,password):
        if email.upper() == 'BOSS' and password == 'Man':
            self.logged_in_staff = Staff("1","A1","Dóttir Sigga Ísmanns","090488-2959","Grundargata 12", "555-5555", "867-5309", "siggi@nanair.is", "flubber","Yfirmaður rekstrarsviðs",True)
            self.tmp_destination = Destination("A1","Ísland","Keflavík","555-5556","24/7",self.logged_in_staff.staffID)
            self.logged_in_staff.destinationID = self.tmp_destination.destinationID
            return True

        if email.upper() == 'PLEB' and password == '1234':
            self.logged_in_staff = Staff("2","A1","Jón afi","120488-2959","Grundargata 14", "555-5555", "867-5309", "siggi@nanair.is", "flubber","Yfirmaður rekstrarsviðs",False)
            self.tmp_destination = Destination("A1","Ísland","Keflavík","555-5556","24/7",self.logged_in_staff.staffID)
            self.logged_in_staff.destinationID = self.tmp_destination.destinationID
            return True

        return False
    
    def get_logged_in_staff(self) -> Staff:
        return self.logged_in_staff

    def logout(self):
        self.logged_in_staff = None
        pass