from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Staff
from Model import Destination

class StaffScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)

    def run(self):
        self.clear_screen()

        print("Main Menu > Staff")

        staff = self.ui.logic_api.staff_get_all()

        staff_table = PrettyTable()
        staff_table.field_names = ["ID", "Name","Job title","Destination","SSN"]

        for employee in staff:
            employee_destination = self.ui.logic_api.destination_get_by_ID(employee.destinationID)
            if employee_destination is not None:
                employee_destination_country = employee_destination.country
            else:
                employee_destination_country = "Not assigned"

            staff_table.add_row([employee.staffID, employee.name, employee.job_title, employee_destination_country, employee.ssn])

        staff_table._min_table_width = ui_consts.TABLE_WIDTH

        print(staff_table)

        destinations = self.ui.logic_api.destination_get_all()

        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID","Country"]

        for destination in destinations:
            destination_table.add_row([destination.destinationID, destination.country])

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add an employee		[E] Edit an employee			[B] Go back")
        print("|	[R] Remove an employee		[S] Search for")
        print("|	[V] View contact info		[C] View contractors")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add an employee
        if cmd == "a":
            print(destination_table)

            new_destination = input("Enter destination ID for new employee: ").upper()
            # If ID does not exist in destination list, raise error "No destination found with that ID!"
            # Cancel command if destination ID is not found

            new_employee = input("New employee name: ")
            new_ssn = (input("New employee ssn: "))
            new_address = input("New employee address: ")
            new_phone_nr = (input("New employee phone number: "))
            new_gsm = (input("New employee mobile number: "))
            new_email = input("New employee email: ")
            while "@" and "." not in new_email:
                print("Invalid email address")
                new_email = input("New employee email: ")
            new_password = input("New employee password: ")
            new_title = input("New employee job title: ")
            new_is_manager = input("Is the new employee a manager? y/n ").lower()
            if new_is_manager == "y":
                is_manager = True
            else:
                is_manager = False

            new_staff = Staff(None, new_destination, new_employee, new_ssn, new_address, new_phone_nr, new_gsm, new_email, new_password, new_title, is_manager)

            self.ui.logic_api.staff_add(new_staff)

        # Remove an employee
        if cmd == "r":
            remove_id = input("Remove employee with the ID: ").upper()
            self.ui.logic_api.staff_remove(remove_id)

        # View contact info
        if cmd == "v":
            view = input("View the contact information of employee with the ID: ")
            print(f"Name: {new_employee}")
            print(f"Email: {new_email}")
            print(f"Phone number: {new_phone_nr}")
            print(f"Mobile phone number: {new_gsm}")
            print(f"Address: {new_address}")
                # If ID does not exist in the employee list, raise error "No employee found with that ID!"    
	            # If ID does not exist, cancel command

        if cmd == "e":
            staff_edit = None
            staff_attributes = ["name", "ssn","address","phone_home","phone_gsm","email","password","job_title","is_manager"]

            while staff_edit is None:
                edit_with_id = input("Edit employee with the ID: ").upper()
                #if nothing is input, the field will be left unchanged
                for employee in staff:
                    if employee.staffID == edit_with_id:
                        staff_edit = employee
                        break

                if staff_edit is None:
                    print(f"No employee with the ID: '{edit_with_id}' Try again (B to cancel).")

                if edit_with_id == "B":
                    return ui_consts.CMD_BACK
            
            new_destinationID = input("New destination ID: ").upper()
            setattr(staff_edit, "destinationID", new_destinationID)
            
            for attribute in staff_attributes:
                current_value = getattr(staff_edit, attribute)
                new_value = input(f"New {attribute.capitalize()} (Current {current_value}): ").strip()
                if new_value:
                    setattr(staff_edit,attribute,new_value)

            if staff_edit.is_manager == "y":
                staff_edit.is_manager = True
            else:
                staff_edit.is_manager = False

            self.ui.logic_api.staff_edit(staff_edit)
            # If ID does not exist in the employee list, raise error "No employee found with that ID!"
            # If ID does not exist, cancel command
            # If job title = "manager" or "boss" set isManager = True, otherwise False)

        if cmd == "s":
                # Example gamer, Nuuk
                # Finnur allar línur tengdar gamer, nuuk
            search = input("Search for: ") # Sama search allstaðar nema á tickets

        # View contact info
        if cmd == "c":
            return ui_consts.CONTRACTOR_SCREEN

        # Back
        if cmd == "b":
            return ui_consts.CMD_BACK

        return self
