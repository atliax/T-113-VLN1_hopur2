class LogicAPI:
    def __init__(self, storage_api):
        pass

    def authenticate_login(self, email, password):
        if email == 'test' and password == 'test':
            return True

        return False
