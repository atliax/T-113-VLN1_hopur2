from StorageLayer.storage_api import StorageAPI

import json
from Model import Staff
from Model import Destination

class StaffManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api
        self.logged_in_staff : Staff = None
        self.tmp_destination : Destination = None #tmp, remove later

    def authenticate_login(self, email : str, password : str) -> bool:
        if email.upper() == 'BOSS' and password == 'Man':
            self.logged_in_staff = Staff("S1", "D0", "Manager", "090488-2959", "Grundargata 12", "555-5555", "867-5309", "siggi@nanair.is", "flubber", "Yfirmaður rekstrarsviðs", True)
            self.tmp_destination = Destination("D0", "Ísland", "Keflavík", "555-5556", "24/7", self.logged_in_staff.staffID)
            self.logged_in_staff.destinationID = self.tmp_destination.destinationID
            return True

        if email.upper() == 'PLEB' and password == '1234':
            self.logged_in_staff = Staff("S2", "D0", "Jón afi", "120488-2959", "Grundargata 14", "555-5555", "867-5309", "siggi@nanair.is", "flubber", "Starfsmaður", False)
            self.tmp_destination = Destination("D0", "Ísland", "Keflavík", "555-5556", "24/7", self.logged_in_staff.staffID)
            self.logged_in_staff.destinationID = self.tmp_destination.destinationID
            return True

        return False
    
    def get_all_staff(self) -> list[Staff]:
        return self.storage_api.get_all_staff()
    
    def get_logged_in_staff(self) -> Staff:
        return self.logged_in_staff

    def logout(self) -> None:
        self.logged_in_staff = None

    def add_new_staff(self, new_staff : Staff) -> None:
        all_staff = self.storage_api.get_all_staff()
        n = int(all_staff[len(all_staff)-1].staffID[1:])
        n += 1
        new_id = "S" + str(n)
        new_staff.staffID = new_id

        # validation

        # ef í lagi:
        self.storage_api.add_new_staff(new_staff)

    def remove_staff(self, staffID : str):
        # validation
        
        # ef í lagi:
        self.storage_api.remove_staff(staffID)

    def edit_staff(self, edit_staff):
        self.storage_api.edit_staff(edit_staff)
  