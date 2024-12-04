from LogicLayer.staff_manager import StaffManager

class LogicAPI:
    def __init__(self, storage_api):
        self.staff_manager = StaffManager(storage_api)

    def authenticate_login(self, email, password):
        return self.staff_manager.authenticate_login(email, password)

    def get_logged_in_staff(self):
        return self.staff_manager.get_logged_in_staff()
