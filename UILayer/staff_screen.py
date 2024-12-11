import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Staff

class StaffScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self):
        self.clear_screen()

        print("Main Menu > Staff")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add an employee		[E] Edit an employee			[B] Go back")
        print("|	[R] Remove an employee		[S] Search for")
        print("|	[V] View contact info		[C] View contractors")
        print("|")
        print(ui_consts.SEPERATOR)

        if self.active_search_filter:
            staff_list = self.ui.logic_api.staff_search(self.active_search_filter)
        else:
            staff_list = self.ui.logic_api.staff_get_all()

        staff_table = PrettyTable()
        staff_table.field_names = ["ID", "Name","Job title","Destination","SSN"]

        for employee in staff_list:
            employee_destination = self.ui.logic_api.destination_get_by_ID(employee.destinationID.upper())

            if employee_destination is not None:
                employee_destination_country = employee_destination.country
            else:
                employee_destination_country = "Not assigned"

            staff_table.add_row([employee.ID, employee.name, employee.job_title, employee_destination_country, employee.ssn])

        staff_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(staff_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Staff list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(staff_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        # construct a table of destinations for use with the "add" and "edit" commands
        destinations = self.ui.logic_api.destination_get_all()
        destination_table = PrettyTable()
        destination_table.field_names = ["Destination ID","Country","Airport"]
        for destination in destinations:
            destination_table.add_row([destination.ID, destination.country, destination.airport])

        match cmd:
            # Next page
            case "n":
                self.current_page += 1
            # Previous page
            case "p":
                self.current_page -= 1
            # Add an employee
            case "a":
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
            case "r":
                remove_id = input("Remove employee with the ID: ").upper()
                self.ui.logic_api.staff_remove(remove_id)
            # View contact info
            case "v":
                contact_by_id = None

                while contact_by_id is None:
                    view_contact = input("View the contact information of employee with the ID: ").upper()

                    contact_by_id = self.ui.logic_api.staff_get_by_ID(view_contact)

                    if contact_by_id is None:
                        print(f"No employee with the ID: '{view_contact}', try again (B to return).")
                    if view_contact == "B":
                        return ui_consts.CMD_BACK

                contact_by_id_table = PrettyTable()
                contact_by_id_table.field_names = ["ID","Name","Phone Nr.","Mobile Phone Nr.","Address"]
                contact_by_id_table.add_row([contact_by_id.ID,contact_by_id.name,contact_by_id.phone_home,contact_by_id.phone_gsm,contact_by_id.address])
                print(contact_by_id_table)
                input("Press enter to continue.")
            # Edit an employee
            case "e":
                staff_edit = None
                staff_attributes = ["destinationID","name","address","phone_home","phone_gsm","email","password","job_title","is_manager"]

                while staff_edit is None:
                    edit_with_id = input("Edit employee with the ID: ").upper()

                    staff_edit = self.ui.logic_api.staff_get_by_ID(edit_with_id)

                    if staff_edit is None:
                        print(f"No employee with the ID: '{edit_with_id}' try again (B to return).")

                    if edit_with_id == "B":
                        return ui_consts.CMD_BACK

                # First display the available destinations
                print(destination_table)

                # Then get the new info from the user
                # if nothing is input, the field will be left unchanged
                for attribute in staff_attributes:
                    current_value = getattr(staff_edit, attribute)
                    new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()
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
            # Search for
            case "s":
                self.active_search_filter = input("Search for: ") 
            # View contractors
            case "c":
                return ui_consts.CONTRACTOR_SCREEN
            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return self
