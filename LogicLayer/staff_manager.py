class StaffManager:
    def __init__(self, storage_api):
        self.storage_api = storage_api
        self.logged_in = False
        self.logged_in_user = ""

    def authenticate_login(self,email,password):
        if email == 'test' and password == 'test':
            self.logged_in = True
            self.logged_in_user = "Siggi"
            return True

        return False
    
    def get_logged_in_user(self):
        return self.logged_in_user
