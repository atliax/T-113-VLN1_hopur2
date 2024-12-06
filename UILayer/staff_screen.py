from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class StaffScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main Menu > Staff")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add an employee		[E] Edit a destination			[B] Go back")
        print("|	[R] Remove an employee		[S] Search for")
        print("|	[V] View contact info		[C] View contractors")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add an employee
        if cmd == "a":
            new_employee = input("New employee name: ")
            new_ssn = int(input("New employee ssn: "))
            new_address = input("New employee address: ")
            new_phone_nr = int(input("New employee phone number: "))
            new_gms = int(input("New employee mobile number: "))
            new_email = input("New employee email: ")
            new_password = input("New employee password: ")
            new_title = input("New employee job title: ")
            is_manager = input("Is the new employee a manager? y/n ")
            

        # Remove an employee
        if cmd == "r":
            remove_employee = input("Remove employee with the ID: ")

        # View contact info
        if cmd == "v":
            view = input("View the contact information of employee with the ID: ")
            print(f"Name: {new_employee}")
            print(f"Email: {new_email}")
            print(f"Phone number: {new_phone_nr}")
            print(f"Mobile phone number: {new_gms}")
            print(f"Address: {new_address}")
                # If ID does not exist in the employee list, raise error "No employee found with that ID!"    
	            # If ID does not exist, cancel command

        if cmd == "e":
                # If ID does not exist in the employee list, raise error "No employee found with that ID!"    
                # If ID does not exist, cancel command
            edit_with_id = input("Edit employee with the ID: ") # á eftir að implementa
                #if nothing is input, the field will be left unchanged
            change_name = input("Change employey name to: ")
            change_address = input("Change employee address to: ")
            change_number = int(input("Change employee phone number to: "))
            change_mobile = int(input("Change employee mobile phone number to: "))
            change_email = input("Change employee email to: ")
            change_pass = input("Change employee password to: ")
            change_title = input("Change employee job title to: ")
                # If job title = "manager" or "boss" set isManager = True, otherwise False)

        if cmd == "s":
                # Example gamer, Nuuk
                # Finnur allar línur tengdar gamer, nuuk
            search = input("Search for: ") # Sama search allstaðar nema á tickets

        # View contact info
        if cmd == "c":
            return ui_consts.CONTRACTOR
            
        # Back
        if cmd == "b":
            return ui_consts.BACK


        return self
