

class Staff:
    def __init__(self ,name ,ssn ,address ,home_phone ,mobile_phone ,email ,location ,username ,password):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.email = email
        self.location = location
        self.username = username
        self.password = password

    def update_contact_info(self, address = None, home_phone = None, mobile_phone = None, email = None):
        """updates the selected attribute"""
        if address:
            self.address = address
        if home_phone:
            self.home_phone = home_phone
        if mobile_phone:
            self.mobile_phone = mobile_phone
        if email:
            self.email = email
    
    def verify_password(self, password):
        """checks the password, kannski er þetta ekkert hér."""
        return self.password == password

    def change_password(self, old_password: str, new_password: str):
        if self.verify_password(old_password):
            self.password = new_password
            print("passwrod changed succesfully")
            return True
        else:
            print("FAILed to change password")
            return False
            
    def display_details(self):
        """
        Display staff member details.
        """
        return (
            f"Name: {self.name}\n"
            f"SSN: {self.ssn}\n"
            f"Address: {self.address}\n"
            f"Home Phone: {self.home_phone}\n"
            f"Mobile Phone: {self.mobile_phone}\n"
            f"Email: {self.email}\n"
            f"Location: {self.location}\n"
            f"Username: {self.username}"
        )
    
    def __str__(self):
        return f"Staff Member: {self.name}, Location: {self.location}, Email: {self.email}"    
#TODO klára fallið