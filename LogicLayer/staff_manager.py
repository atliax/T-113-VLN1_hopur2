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
            self.logged_in_staff = Staff("S0", "D0", "Manager", "090488-2959", "Grundargata 12", "555-5555", "867-5309", "siggi@nanair.is", "flubber", "Yfirmaður rekstrarsviðs", True)
            self.tmp_destination = Destination("D0", "Ísland", "Keflavík", "555-5556", "24/7", self.logged_in_staff.ID)
            self.logged_in_staff.destinationID = self.tmp_destination.ID
            return True

        if email.upper() == 'PLEB' and password == '1234':
            self.logged_in_staff = Staff("S0", "D0", "Jón afi", "120488-2959", "Grundargata 14", "555-5555", "867-5309", "siggi@nanair.is", "flubber", "Starfsmaður", False)
            self.tmp_destination = Destination("D0", "Ísland", "Keflavík", "555-5556", "24/7", self.logged_in_staff.ID)
            self.logged_in_staff.destinationID = self.tmp_destination.ID
            return True

        return False

    def logout(self) -> None:
        self.logged_in_staff = None

    def get_logged_in_staff(self) -> Staff:
        return self.logged_in_staff

    def staff_get_all(self) -> list[Staff]:
        return self.storage_api.staff_get_all()

    def staff_add(self, new_staff : Staff) -> None:
        all_staff = self.storage_api.staff_get_all()
        n = int(all_staff[len(all_staff)-1].ID[1:])
        n += 1
        new_id = "S" + str(n)
        new_staff.ID = new_id

        # validation

        # ef í lagi:
        self.storage_api.staff_add(new_staff)

    def staff_remove(self, staffID : str):
        # validation

        # ef í lagi:
        self.storage_api.staff_remove(staffID)

    def staff_edit(self, edited_staff):
        self.storage_api.staff_edit(edited_staff)

    def staff_get_by_ID(self, staffID : str) -> Staff:
        return self.storage_api.staff_get_by_ID(staffID)

    def staff_search(self, search_string : str) -> list[Staff]:
        all_staff : list[Staff] = self.storage_api.staff_get_all()
        filtered_staff = []
        for staff in all_staff:
            found = False
            for attribute_value in list(staff.__dict__.values()):
                if search_string.lower() in str(attribute_value).lower():
                    filtered_staff.append(staff)
                    found = True
                    break

            if not found:
                staff_destination = self.storage_api.destination_get_by_ID(staff.destinationID)
                if search_string.lower() in staff_destination.country.lower():
                    filtered_staff.append(staff)

        return filtered_staff
