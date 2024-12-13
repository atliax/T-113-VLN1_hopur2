from StorageLayer.storage_api import StorageAPI

from Model import Staff, Destination

class StaffManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api
        self.logged_in_staff : Staff = None
        self.tmp_destination : Destination = None #tmp, remove later

    def staff_add(self, new_staff : Staff) -> None:
        """Takes a new staff instance and adds it to the system."""
        n = int(self.storage_api.staff_get_highest_ID()[1:])
        n += 1
        new_id = "S" + str(n)
        new_staff.ID = new_id

        # validation

        # ef í lagi:
        self.storage_api.staff_add(new_staff)

    def staff_edit(self, edited_staff):
        """Takes a staff instance and replaces a staff in the system that has the same ID."""
        self.storage_api.staff_edit(edited_staff)

    def staff_get_all(self) -> list[Staff]:
        """Returns a list of all the staff that exist in the system."""
        return self.storage_api.staff_get_all()

    def staff_get_by_ID(self, staffID : str) -> Staff:
        """Takes a staff ID and returns a staff instance from the system with the same ID if it exists."""
        return self.storage_api.staff_get_by_ID(staffID)

    def staff_list_managers(self) -> list[Staff]:
        """Returns a list of all the staff that have manager status."""
        all_staff : list[Staff] = self.staff_get_all()

        managers = []
        for staff in all_staff:
            if staff.is_manager:
                managers.append(staff)

        return managers

    def staff_remove(self, staffID : str):
        """Takes a staff ID and removes it from the system."""
        # validation

        # ef í lagi:
        self.storage_api.staff_remove(staffID)

    def staff_search(self, search_string : str) -> list[Staff]:
        """Takes a string and returns a list of staff in the system that have attributes containing that string."""
        all_staff : list[Staff] = self.staff_get_all()
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
                if staff_destination is not None:
                    if search_string.lower() in staff_destination.country.lower():
                        filtered_staff.append(staff)

        return filtered_staff

    def authenticate_login(self, email : str, password : str) -> bool:
        """Attempts to log in using a specified email/password combination"""
        all_staff = self.storage_api.staff_get_all()
        for employee in all_staff:
            if employee.email == email:
                if employee.password == password:
                    self.logged_in_staff = employee
                    return True

        return False

    def logout(self) -> None:
        """Invalidates the login status of the currently logged in user"""
        self.logged_in_staff = None

    def get_logged_in_staff(self) -> Staff:
        """Returns the currently logged in staff member"""
        return self.logged_in_staff

    def is_manager_logged_in(self) -> bool:
        """Returns True if the currently logged in user is a manager, otherwise False."""
        return self.logged_in_staff.is_manager
