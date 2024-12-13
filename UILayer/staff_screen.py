# standard library imports
import math

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Staff

class StaffScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1
        self.active_search_filter = ""

    def run(self) -> str | None:
        self.clear_screen()

        print("Main Menu > Staff")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add an employee		[E] Edit an employee			[B] Go back")
            print("|	[R] Remove an employee		[S] Search for")
            print("|	[V] View contact info		[C] View contractors")
        else:
            print_formatted_text(HTML("|	<s>[A] Add an employee</s>		<s>[E] Edit an employee</s>			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove an employee</s>		[S] Search for"))
            print_formatted_text(HTML("|	[V] View contact info		[C] View contractors"))

        print("|")
        print(ui_consts.SEPERATOR)

        try:
            if self.active_search_filter:
                staff_list = self.logic_api.staff_search(self.active_search_filter)
            else:
                staff_list = self.logic_api.staff_get_all()
        except Exception as e:
            print(f"Error loading staff:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        total_pages = math.ceil(len(staff_list) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        staff_table = PrettyTable()
        staff_table.field_names = ["ID", "Name","Job title","Destination","SSN"]
        staff_table._min_table_width = ui_consts.TABLE_WIDTH

        for employee in staff_list:
            try:
                employee_destination = self.logic_api.destination_get_by_ID(employee.destinationID.upper())
            except Exception as e:
                print(f"Error loading destination data for employee '{employee.ID}':")
                print(f"{type(e).__name__}: {e}")
                input(ui_consts.MSG_ENTER_BACK)
                return ui_consts.CMD_BACK

            if employee_destination is not None:
                employee_destination_country = employee_destination.country
            else:
                employee_destination_country = "Not assigned"

            staff_table.add_row([employee.ID, employee.name, employee.job_title, employee_destination_country, employee.ssn])

        print(f"|  Staff list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")

        if self.active_search_filter:
            print(f"|  Active search filter: '{self.active_search_filter}'")

        if total_pages != 0:
            print(staff_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("")
            print("No staff found.")

        print("")
        cmd = input("Command: ").lower()

        # construct a table of destinations for use with the "add" and "edit" commands
        try:
            destinations = self.logic_api.destination_get_all()
        except Exception as e:
            print(f"Error loading destinations:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
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
                if self.logic_api.is_manager_logged_in():

                    print(destination_table)

                    new_destinationID_prompt = "Enter destination ID for new employee (B to cancel): "
                    try:
                        while not self.logic_api.destination_get_by_ID(new_destinationID := input(new_destinationID_prompt).upper()):
                            if new_destinationID == "B":
                                return None
                            print(f"No destination found with the ID: '{new_destinationID}'.")
                    except Exception as e:
                        print(f"Error loading destination '{new_destinationID}' while adding an employee:")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    while (new_staff_name := input("New employee name: ")) == "":
                        print("Staff name can't be empty.")

                    valid_ssn = False
                    while not valid_ssn:
                        new_staff_ssn = input("New employee SSN: ")
                        tmp = new_staff_ssn.replace("-","")
                        if tmp.isdigit():
                            valid_ssn = True
                        else:
                            print("SSN can only include '-' and numbers.")

                    while (new_address := input("New employee address: ")) == "":
                        print("Staff address can't be empty.")

                    valid_phone = False
                    while not valid_phone:
                        new_phone_nr = input("New employee phone number: ")
                        tmp = new_phone_nr.replace("+", "").replace("-", "").replace(" ", "")
                        if not tmp.isdigit():
                            print(ui_consts.MSG_INVALID_PHONE)
                        else:
                            valid_phone = True

                    valid_phone = False
                    while not valid_phone:
                        new_gsm = input("New employee mobile number: ")
                        tmp = new_gsm.replace("+", "").replace("-", "").replace(" ", "")
                        if not tmp.isdigit():
                            print(ui_consts.MSG_INVALID_PHONE)
                        else:
                            valid_phone = True

                    valid_email = False
                    while not valid_email:
                        new_email = input("New employee email: ")
                        if "@" not in new_email or "." not in new_email:
                            print("Invalid email address.")
                        else:
                            valid_email = True

                    while (new_password := input("New employee password: ")) == "":
                        print("Staff password can't be empty.")

                    while (new_title := input("New employee job title: ")) == "":
                        print("Job title can't be empty.")

                    is_manager_yn = input("Is the new employee a manager? y/n ").lower()
                    is_manager = is_manager_yn == "y"

                    # TODO change manager for chosen destination if it already exists?

                    new_staff = Staff(
                        None, new_destinationID, new_staff_name, new_staff_ssn, new_address,
                        new_phone_nr, new_gsm, new_email, new_password, new_title, is_manager)

                    try:
                        self.logic_api.staff_add(new_staff)
                    except Exception as e:
                        print(f"Error adding employee '{new_staff.name}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Remove staff
            case "r":
                if self.logic_api.is_manager_logged_in():
                    remove_id = input("Remove employee with the ID: ").upper()

                    if input(f"Are you sure you want to remove employee '{remove_id}' (Y to confirm)? ").upper() != "Y":
                        return None

                    try:
                        self.logic_api.staff_remove(remove_id)
                    except Exception as e:
                        print(f"Error removing employee '{remove_id}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # View details
            case "v":
                view_staff = None

                while view_staff is None:
                    view_staff_ID = input("View the contact information of employee with the ID (B to cancel): ").upper()

                    if view_staff_ID == "B":
                        return None

                    try:
                        view_staff = self.logic_api.staff_get_by_ID(view_staff_ID)
                    except Exception as e:
                        print(f"Error loading data for employee '{view_staff_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    if view_staff is None:
                        print(f"No employee with the ID: '{view_staff_ID}', try again.")

                contact_by_id_table = PrettyTable()
                contact_by_id_table.field_names = ["ID","Name","Phone Nr.","Mobile Phone Nr.","Address"]
                contact_by_id_table.add_row([view_staff.ID,view_staff.name,view_staff.phone_home,view_staff.phone_gsm,view_staff.address])
                print(contact_by_id_table)

                input(ui_consts.MSG_ENTER_CONTINUE)
                return None

            # [E] to Edit an employee
            case "e":
                if self.logic_api.is_manager_logged_in():
                    staff_edit = None

                    while staff_edit is None:
                        staff_edit_ID = input("Edit employee with the ID (B to cancel): ").upper()

                        if staff_edit_ID == "B":
                            return None

                        try:
                            staff_edit = self.logic_api.staff_get_by_ID(staff_edit_ID)
                        except Exception as e:
                            print(f"Error loading info for employee '{staff_edit_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None

                        if staff_edit is None:
                            print(f"No employee with the ID: '{staff_edit_ID}', try again.")

                    # Display the available destinations
                    print(destination_table)

                    # Get new property details from user
                    new_destination_ID_prompt = "Enter destination ID for employee (B to cancel): "
                    try:
                        while not self.logic_api.destination_get_by_ID(new_destination_ID := input(new_destination_ID_prompt).upper()):
                            if new_destination_ID == "B":
                                return None
                            print(f"No destination found with the ID: {new_destination_ID}")
                    except Exception as e:
                        print(f"Error loading destination '{new_destination_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    setattr(staff_edit, "destinationID", new_destination_ID)

                    print(f"Enter new data for the employee '{staff_edit_ID}', leave the field empty to keep the previous data.")

                    editable_attributes = ["name", "address", "phone_home", "phone_gsm", "email", "password", "job_title", "is_manager"]
                    for attribute in editable_attributes:
                        current_value = getattr(staff_edit, attribute, None)

                        new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()
                        if not new_value:
                            continue

                        if attribute in ["phone_home", "phone_gsm"]:
                            valid_phone = False
                            while not valid_phone:
                                tmp = new_value.replace("+", "").replace("-", "").replace(" ", "")
                                if not tmp.isdigit():
                                    print(ui_consts.MSG_INVALID_PHONE)
                                    new_value = input("New employee mobile number: ")
                                else:
                                    valid_phone = True

                        elif attribute == "email":
                            while "@" not in new_value or "." not in new_value:
                                print("Invalid email address.")
                                new_value = input(f"New {attribute.capitalize()} (Current: {current_value}): ").strip()

                        elif attribute == "is_manager":
                            new_value = new_value.lower()
                            new_value = True if new_value == "y" else False

                            # TODO check if there is already a manager at the chosen destination?

                        setattr(staff_edit, attribute, new_value)

                    try:
                        self.logic_api.staff_edit(staff_edit)
                    except Exception as e:
                        print(f"Error editing employee '{staff_edit_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    print(f"Updated details for employee '{staff_edit_ID}'.")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Search for
            case "s":
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)
                return None

            # View contractors
            case "c":
                return ui_consts.CONTRACTOR_SCREEN

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return None
