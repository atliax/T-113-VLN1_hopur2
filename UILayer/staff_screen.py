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

        if self.ui.logic_api.is_manager_logged_in():
            print("|	[A] Add an employee		[E] Edit an employee			[B] Go back")
            print("|	[R] Remove an employee		[S] Search for")
            print("|	[V] View contact info		[C] View contractors")
        else:
            print("|	[V] View contact info		[C] View contractors		[B] Go back")
            print("|	[S] Search for")

        print("|")
        print(ui_consts.SEPERATOR)

        try:
            if self.active_search_filter:
                staff_list = self.ui.logic_api.staff_search(self.active_search_filter)
            else:
                staff_list = self.ui.logic_api.staff_get_all()
        except Exception as e:
            print(f"Error getting employee: {e}")
            print("Could not load employee list. Try again.")
            input("Press enter to go back.")
            return ui_consts.CMD_BACK

        staff_table = PrettyTable()
        staff_table.field_names = ["ID", "Name","Job title","Destination","SSN"]

        for employee in staff_list:
            try:
                employee_destination = self.ui.logic_api.destination_get_by_ID(employee.destinationID.upper())
            except Exception as e:
                print(f"Error loading destination data for contractor '{employee.ID}': {e}")
                print("Error displaying employee details.")
                input("Press enter to go back.")
                return ui_consts.CMD_BACK

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
        try:    
            destinations = self.ui.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destination data: {e}")
            print("Could not load destinations. Try again.")
            input("Press enter to go back.")
            return ui_consts.CMD_BACK

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
                if self.ui.logic_api.is_manager_logged_in():
                    print(destination_table)
                    while True:
                        try:
                            new_destination = input("Enter destination ID for new employee (B to go back): ").upper()
                            
                            if new_destination == "B".lower():
                                return ui_consts.CMD_BACK  

                            
                            if not self.ui.logic_api.destination_get_by_ID(new_destination):
                                raise ValueError(f"No destination found with the ID: '{new_destination}'")
                            break  

                        except ValueError as e:
                            print(e)
                            print("Please try again or type 'B' to go back.")

                    
                    new_employee = input("New employee name: ")
                    new_ssn = input("New employee SSN: ")
                    while not new_ssn.isdigit():
                        print("SSN can only contain numbers.")
                        new_ssn = input("New employee SSN: ")
                    new_address = input("New employee address: ")
                    new_phone_nr = input("New employee phone number: ").replace(" ", "").replace("-", "")
                    while not (new_phone_nr.startswith("+") and new_phone_nr[1:].isdigit() or new_phone_nr.isdigit()):
                        print("Phone number must contain only numbers or start with a single '+' followed by numbers.")
                        new_phone_nr = input("New employee phone number: ").replace(" ", "").replace("-", "")
                    new_gsm = input("New employee mobile number: ").replace(" ", "").replace("-", "")
                    while not (new_gsm.startswith("+") and new_gsm[1:].isdigit() or new_gsm.isdigit()):
                        print("Mobile number must contain only numbers or start with a single '+' followed by numbers.")
                        new_gsm = input("New employee mobile number: ").replace(" ", "").replace("-", "")
                    new_email = input("New employee email: ")
                    while "@" not in new_email or "." not in new_email:
                        print("Invalid email address.")
                        new_email = input("New employee email: ")
                    new_password = input("New employee password: ")
                    new_title = input("New employee job title: ")
                    new_is_manager = input("Is the new employee a manager? y/n ").lower()
                    is_manager = new_is_manager == "y"

                    
                    new_staff = Staff(
                        None, new_destination, new_employee, new_ssn, new_address,
                        new_phone_nr, new_gsm, new_email, new_password, new_title, is_manager
                    )

                    try:
                        self.ui.logic_api.staff_add(new_staff)
                    except Exception as e:
                        print(f"Error removing employee: {e}")
                        print("Could not remove employee. Try again.")
                        input("Press enter to continue: ")                       
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")

            #[R] to remove staff
            case "r":
                if self.ui.logic_api.is_manager_logged_in():
                    remove_id = input("Remove employee with the ID: ").upper()
                    self.ui.logic_api.staff_remove(remove_id)
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")
            #[V] to view details
            case "v":
                contact_by_id = None

                while contact_by_id is None:
                    view_contact = input("View the contact information of employee with the ID: ").upper()

                    contact_by_id = self.ui.logic_api.staff_get_by_ID(view_contact)

                    if contact_by_id is None:
                        print(f"No employee with the ID: '{view_contact}', try again (B to cancel).")
                    if view_contact == "B":
                        return self

                contact_by_id_table = PrettyTable()
                contact_by_id_table.field_names = ["ID","Name","Phone Nr.","Mobile Phone Nr.","Address"]
                contact_by_id_table.add_row([contact_by_id.ID,contact_by_id.name,contact_by_id.phone_home,contact_by_id.phone_gsm,contact_by_id.address])
                print(contact_by_id_table)
                input("Press enter to continue.")
            # [E] to Edit an employee
            case "e":
                if self.ui.logic_api.is_manager_logged_in():
                    staff_edit = None
                    staff_attributes = ["destinationID", "name", "address", "phone_home", "phone_gsm", "email", "password", "job_title", "is_manager"]

                    while staff_edit is None:
                        edit_with_id = input("Edit employee with the ID: ").upper()

                        if edit_with_id == "B":
                            return ui_consts.CMD_BACK
                        
                            # First display the available destinations
                        print(destination_table)

                        try:
                            staff_edit = self.ui.logic_api.staff_get_by_ID(edit_with_id)
                        except Exception as e:
                            print(f"Error loading contractor info: {e}")
                            print("Could not load contractor information. Try again.")
                            input("Press enter to continue.")
                            return self

                        if staff_edit is None:
                            print(f"No employee with the ID: '{edit_with_id}' try again (B to return).")

                    
                    print(f"Editing details for employee ID: {edit_with_id}")
                    
                    for attribute in staff_attributes:
                        current_value = getattr(staff_edit, attribute, None)
                        new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()
                        if not new_value:
                            continue
                    
                        if attribute in ["phone_home", "phone_gsm"]:
                            while not ((new_value.startswith('+') and new_value[1:].isdigit()) or new_value.isdigit()):
                                print(f"{attribute.capitalize()} must contain only numbers or start with '+' followed by numbers.")
                                new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()
                      
                        elif attribute == "email":
                            while "@" not in new_value or "." not in new_value:
                                print("Invalid email address.")
                                new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()
                        
                        elif attribute == "is_manager":
                            new_value = new_value.lower()
                            while new_value not in ["y", "n"]:
                                print("Invalid input. Enter 'y' for yes or 'n' for no.")
                                new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip().lower()
                            new_value = True if new_value == "y" else False
                        
                        
                        setattr(staff_edit, attribute, new_value)

                    try:
                        self.ui.logic_api.staff_edit(staff_edit)
                    except Exception as e:
                        print(f"Error editing employee: {e}")
                        print("Could not edit employee. Try again.")
                        input("Press enter to continue.")  

                    print(f"Updated details for employee ID: {edit_with_id}")
                else:
                    print("You don't have permission to do that.")
                    input("Press enter to continue.")

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
