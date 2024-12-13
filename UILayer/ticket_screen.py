# standard library imports
import math
from datetime import datetime
from textwrap import fill

# pip library imports
from prettytable import PrettyTable
from prompt_toolkit import print_formatted_text, HTML

# local imports
from LogicLayer import logic_consts
from UILayer.base_screen import BaseScreen
from UILayer import ui_consts
from Model import Ticket

class TicketScreen(BaseScreen):
    def __init__(self, logic_api) -> None:
        super().__init__(logic_api)
        self.current_page = -1

        # set the default search filter for managers and regular staff
        if self.logic_api.is_manager_logged_in():
            self.active_search_filter = logic_consts.TICKET_STATUS_DONE
        else:
            self.active_search_filter = logic_consts.TICKET_STATUS_OPEN

        # no other search filters active be default
        self.search_start_date = ""
        self.search_end_date = ""
        self.filter_by_property = ""

    def run(self) -> str | None:
        self.clear_screen()

        ticket_priority_list = ["High", "Medium", "Low"] #TODO setja í const

        print("Main Menu > Tickets")

        print(ui_consts.SEPERATOR)
        print("|")

        if self.logic_api.is_manager_logged_in():
            print("|	[A] Add a ticket		[E] Edit			[B] Go back")
            print("|	[R] Remove a ticket		[S] Search for			[PR] Process")
            print("|	[V] View closed/open tickets	[D] Ticket details")
        else:
            print_formatted_text(HTML("|	[A] Add a ticket		<s>[E] Edit</s>			[B] Go back"))
            print_formatted_text(HTML("|	<s>[R] Remove a ticket</s>		[S] Search for			[PR] Process"))
            print_formatted_text(HTML("|	[V] View closed/open tickets	[D] Ticket details"))

        print("|")
        print(ui_consts.SEPERATOR)

        # uppfæra ticket sem þarf að opna og endurtekna ticket
        try:
            self.logic_api.ticket_update_pending()
            self.logic_api.ticket_update_recurring()
        except Exception as e:
            print(f"Error updating pending/recurring tickets:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        # Sækja áfangastað núverandi innskráðs starfsmanns til að nota seinna
        logged_in_destinationID = self.logic_api.get_logged_in_staff().destinationID

        # Smíða töflu af destinations til að geta nýtt hana á fleiri en einum stað
        try:
            properties = self.logic_api.property_get_by_destinationID(logged_in_destinationID)
        except Exception as e:
            print(f"Error loading properties for destination '{logged_in_destinationID}':")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK
        property_table = PrettyTable()
        property_table.field_names = ["Property ID","Name","Destination","Type"]
        for property in properties:
            property_table.add_row([property.ID, property.name,property.destinationID,property.type])

        # sækja núverandi lista af tickets eftir því hvaða search filterar eru virkir
        try:
            ticket_list = self.logic_api.ticket_search_advanced(self.active_search_filter,logged_in_destinationID,self.search_start_date, self.search_end_date, self.filter_by_property)
        except Exception as e:
            print(f"Error loading tickets:")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK

        # stilla af blaðsíðudót
        total_pages = math.ceil(len(ticket_list) / 10)
        if self.current_page < 0:
            self.current_page = 0
        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        # stofna Ticket töfluna og stilla hana til
        all_tickets_table = PrettyTable()
        all_tickets_table.field_names = ["ID", "Property", "Facility", "Title", "Priority", "Status", "Days Open"]
        all_tickets_table._min_table_width = ui_consts.TABLE_WIDTH

        # sækja Ticket gögnin og setja í töfluna
        for ticket in ticket_list:
            try:
                ticket_property = self.logic_api.property_get_by_ID(ticket.propertyID)
            except Exception as e:
                print(f"Error loading data for property '{ticket.propertyID}':")
                print(f"{type(e).__name__}: {e}")
                input(ui_consts.MSG_ENTER_BACK)
                return ui_consts.CMD_BACK

            if ticket.facilityID == None:
                facility_name = "None"
            else:
                try:
                    facility_name = self.logic_api.facility_get_by_ID(ticket.facilityID).name
                except Exception as e:
                    print(f"Error loading data for facility '{ticket.facilityID}':")
                    print(f"{type(e).__name__}: {e}")
                    input(ui_consts.MSG_ENTER_BACK)
                    return ui_consts.MSG_ENTER_BACK

            try:
                ticket_open_date = datetime.strptime(ticket.open_date, ui_consts.DATE_FORMAT)
                days_delta = datetime.now() - ticket_open_date
            except ValueError:
                print(f"Error creating datetime object:")
                print(f"{type(e).__name__}: {e}")
                input(ui_consts.MSG_ENTER_BACK)
                return ui_consts.CMD_BACK
            days_open = days_delta.days

            if ticket.status != logic_consts.TICKET_STATUS_OPEN:
                days_open = "N/A"
            else:
                days_open = str(days_open)

            all_tickets_table.add_row([ticket.ID, ticket_property.name, facility_name, fill(ticket.title, width=40), ticket.priority, ticket.status, days_open])

        print(f"|  Ticket list (Page {self.current_page + 1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page" + f" [{logged_in_destinationID}]") #TODO DEBUG REMOVE

        if self.active_search_filter != "" or self.search_start_date != "" or self.search_end_date != "" or self.filter_by_property != "":
            print("|  Active filters: ", end="")
            search_description = []
            if self.active_search_filter != "":
                search_description.append(f"Keyword: '{self.active_search_filter}'")
            if self.search_start_date != "":
                search_description.append(f"Start: '{self.search_start_date}'")
            if self.search_end_date != "":
                search_description.append(f"End: '{self.search_end_date}'")
            if self.filter_by_property != "":
                try:
                    selected_property_name = self.logic_api.property_get_by_ID(self.filter_by_property).name
                except Exception as e:
                    print(f"Error loading property name for property '{self.filter_by_property}':")
                    print(f"{type(e).__name__}: {e}")
                    input(ui_consts.MSG_ENTER_BACK)
                    return ui_consts.CMD_BACK
                search_description.append(f"Property: '{selected_property_name}' ({self.filter_by_property})")
            print(" ".join(search_description), end="")
            print("")

        if total_pages != 0:
            print(all_tickets_table.get_string(sortby="Days Open",reversesort=True,start=self.current_page*10, end=(self.current_page+1)*10))
        else:
            print("")
            print("No tickets found.")

        print("")
        cmd = input("Command: ").lower()

        match cmd:

            #DEBUG helper command, left in code for teacher's convenience
            #case "sw":
            #    match self.logic_api.get_logged_in_staff().destinationID:
            #        case "D1":
            #            self.logic_api.get_logged_in_staff().destinationID = "D2"
            #        case "D2":
            #            self.logic_api.get_logged_in_staff().destinationID = "D3"
            #        case "D3":
            #            self.logic_api.get_logged_in_staff().destinationID = "D1"

            # Next page:
            case "n":
                self.current_page += 1

            # Previous page:
            case "p":
                self.current_page -= 1

            # Add a ticket
            case "a":

                print(property_table)

                new_ticket_title = ""
                new_ticket_recurring_days = -1
                new_ticket_priority = ""

                # choose property with verification
                new_property_id = input("Property ID for new ticket: ").upper()
                try:
                    while self.logic_api.property_validate(new_property_id) == False:
                        print(f"No property with ID '{new_property_id}' found.")
                        new_property_id = input("(B) to cancel or Property ID for new ticket: ").upper()
                        if new_property_id == "B":
                            return None
                except Exception as e:
                    print(f"Error validating property '{new_property_id}':")
                    print(f"{type(e).__name__}: {e}")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

                try:
                    new_facility_list = self.logic_api.facility_get_by_propertyID(new_property_id)
                except Exception as e:
                    print(f"Error loading facililies for property '{new_property_id}':")
                    print(f"{type(e).__name__}: {e}")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

                # skip facility ID if there are no facilities matching the propertyID
                if len(new_facility_list) == 0:
                    print ("No Facilities to choose from, using propertyID only.")
                    new_ticket_facility_id = None
                # otherwise choose facility with verification
                else:
                    # first create and display a table of the facilities
                    facility_table = PrettyTable()
                    facility_table.field_names = ["ID","Name","Description"]
                    for facility in new_facility_list:
                        facility_table.add_row([facility.ID,facility.name,facility.description])
                    print(facility_table) 

                    new_ticket_facility_id = input("Enter ID of facility for new ticket: ").upper()
                    try:
                        while self.logic_api.facility_validate(new_ticket_facility_id, new_facility_list) == False:
                            print(f"No facility '{new_ticket_facility_id}' at this property")
                            new_ticket_facility_id = input("(B) to cancel or ID of facility for new ticket: ").upper()
                            if new_ticket_facility_id == "B":
                                return None
                    except Exception as e:
                        print(f"Error validating facility '{new_ticket_facility_id}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                while not (new_ticket_title := input("New ticket title: ").strip()):
                    print("Ticket title can't be empty.")

                while not (new_description := input("New ticket description: ")):
                    print("Ticket description can't be empty.")

                while new_ticket_priority not in ticket_priority_list:
                    new_ticket_priority = input("New ticket priority(high, medium, low): ").lower().capitalize()

                date_validated = False
                while not date_validated:
                    print ("Use DD-MM-YYYY format")
                    new_open_date = input("Date to open ticket (leave empty to open the ticket now): ")
                    if new_open_date == "":
                        try:
                            new_open_date = datetime.now().strftime(ui_consts.DATE_FORMAT)
                        except ValueError as e:
                            print(f"Error creating datetime object using format '{ui_consts.DATE_FORMAT}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_CONTINUE)
                            return None
                        status = logic_consts.TICKET_STATUS_OPEN
                    try:
                        date = new_open_date
                        date_validated = datetime.strptime(date, ui_consts.DATE_FORMAT)
                        status = logic_consts.TICKET_STATUS_PENDING
                    except ValueError:
                        print ("Sorry wrong format, try again.")

                while new_ticket_recurring_days < 0:
                    try:
                        new_ticket_recurring_days = int(input("Recur every N days (0 = never): "))
                    except ValueError:
                        print("Invalid input, Please enter a positive integer.")
                        new_ticket_recurring_days = -1

                ticket_recurring = True if new_ticket_recurring_days > 0 else False

                new_ticket = Ticket(ID = None, facilityID = new_ticket_facility_id, propertyID = new_property_id, \
                                    priority = new_ticket_priority, title = new_ticket_title, description = new_description, status = status, \
                                    recurring = ticket_recurring, recurring_days = new_ticket_recurring_days , open_date = new_open_date, \
                                    close_date = None, staffID = None, report = None, cost = 0, contractorID = None, \
                                    contractor_review = None, contractor_rating = None, contractor_fee = 0)

                try:
                    self.logic_api.ticket_add(new_ticket)
                except Exception as e:
                    print(f"Error adding new ticket: '{new_ticket.title}':")
                    print(f"{type(e).__name__}: {e}")
                    input(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # Remove a ticket
            case "r":
                if self.logic_api.is_manager_logged_in():
                    remove_ticket_ID = input("Remove ticket with ID (B to cancel): ").upper()

                    if remove_ticket_ID == "B":
                        return None

                    if input(f"Are you sure you want to remove ticket '{remove_ticket_ID}' (Y to confirm)? ").upper() != "Y":
                        return None

                    try:
                        self.logic_api.ticket_remove(remove_ticket_ID)
                    except Exception as e:
                        print(f"Error removing ticket '{remove_ticket_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    input(ui_consts.MSG_ENTER_CONTINUE)

            # View open/closed tickets
            case "v":
                if self.active_search_filter == logic_consts.TICKET_STATUS_CLOSED:
                    self.active_search_filter = logic_consts.TICKET_STATUS_OPEN
                else:
                    self.active_search_filter = logic_consts.TICKET_STATUS_CLOSED

            # Ticket details
            case "d":
                ticket_details = None

                while ticket_details is None:
                    ticket_details_ID = input("Type in ID of ticket for details (B to cancel): ").upper()

                    if ticket_details_ID == "B":
                        return None

                    try:
                        ticket_details = self.logic_api.ticket_get_by_ID(ticket_details_ID)
                    except Exception as e:
                        print(f"Error loading data for ticket '{ticket_details_ID}':")
                        print(f"{type(e).__name__}: {e}")
                        input(ui_consts.MSG_ENTER_CONTINUE)
                        return None

                    if ticket_details is None:
                        print(f"No ticket with the ID: '{ticket_details_ID}', try again.")

                self.print_ticket_detail_table(ticket_details)

                input(ui_consts.MSG_ENTER_CONTINUE)
                return None

            # Edit ticket
            case "e":
                if self.logic_api.is_manager_logged_in():
                    edit_priority = ""
                    edit_ticket_title = ""

                    print("If you do not wish to change a specific field, you can leave the input empty.")

                    edit_ticket = None

                    while edit_ticket is None:
                        edit_ticket_ID = input("Type in ID of ticket to edit (B to cancel): ").upper()

                        if edit_ticket_ID == "B":
                            return None
                        
                        try:
                            edit_ticket = self.logic_api.ticket_get_by_ID(edit_ticket_ID)
                        except Exception as e:
                            print(f"Error loading ticket data '{edit_ticket_ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK

                        if edit_ticket is None:
                            print(f"No ticket with the ID: '{edit_ticket_ID}', try again (B to cancel).")

                    # ask the user if they want to open the ticket if it is closed
                    if edit_ticket.status == logic_consts.TICKET_STATUS_CLOSED:
                        self.print_ticket_detail_table(edit_ticket)

                        print ("Tickets need to be open to edit or process them.")

                        answer = input(print ("Do you want to open the ticket? (yes/y to open, no/n to stay closed)")).lower()
                        if answer == "yes" or answer == "y":
                            edit_ticket.status = logic_consts.TICKET_STATUS_OPEN
                        elif answer == "no" or answer == "n":
                            return None
                        try:
                            self.logic_api.ticket_edit(edit_ticket)
                        except Exception as e:
                            print(f"Error editing ticket'{edit_ticket.ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK

                    # otherwise allow them to edit the ticket:
                    else:
                        # Edit property with verification
                        self.print_ticket_detail_table(edit_ticket)

                        print(property_table)

                        print("Leave empty if you don't want to change propertyID")
                        property_ID_prompt = f"New propertyID (Current: {edit_ticket.propertyID}) associated with ticket {edit_ticket.ID} (B to cancel): "
                        try:
                            while not self.logic_api.property_validate(edit_property_id := input(property_ID_prompt).upper()):
                                if edit_property_id == "":
                                    edit_property_id = edit_ticket.propertyID
                                    break

                                if edit_property_id == "B":
                                    return None

                                print(f"No property with ID '{edit_property_id}' found, try again.")
                        except Exception as e:
                            print(f"Error validating property'{edit_property_id}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK

                        edit_ticket.propertyID = edit_property_id

                        try:
                            edit_ticket_facilities = self.logic_api.facility_get_by_propertyID(edit_property_id)
                        except Exception as e:
                            print(f"Error loading facility data for property'{edit_property_id}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK
                        
                        # Edit facility with verification
                        self.print_ticket_detail_table(edit_ticket)
                        if len(edit_ticket_facilities) == 0:
                            print ("No Facilities to choose, using propertyID only.")
                            edit_ticket.facilityID = None
                        else:
                            facility_table = PrettyTable()
                            facility_table.field_names = ["ID","Name","Description"]
                            for facility in edit_ticket_facilities:
                                facility_table.add_row([facility.ID,facility.name,facility.description])
                            print(facility_table) 

                            print ("Leave empty if you don't want to change facilityID")
                            facility_ID_prompt = f"New facilityID (Current: {edit_ticket.facilityID}) associated with ticket {edit_ticket.ID} (B to cancel): "

                            try:
                                while not self.logic_api.facility_validate(edit_ticket_facility_id := input(facility_ID_prompt).strip().upper(), edit_ticket_facilities):
                                    if edit_ticket_facility_id == "":
                                        edit_ticket_facility_id = edit_ticket.facilityID
                                        break

                                    if edit_ticket_facility_id == "B":
                                        return None

                                    print("No such facility at this property, B to cancel or try again")
                            except Exception as e:
                                print(f"Error validating facility'{edit_ticket_facility_id}':")
                                print(f"{type(e).__name__}: {e}")
                                input(ui_consts.MSG_ENTER_BACK)
                                return ui_consts.CMD_BACK

                        edit_ticket.facilityID = edit_ticket_facility_id

                        self.print_ticket_detail_table(edit_ticket)

                        # edit priority 
                        while edit_priority not in ticket_priority_list:
                            print("Leave empty if you don't wish to change priority.")
                            edit_priority = input(f"edit ticket priority(high, medium, low), current ({edit_ticket.priority}): ").lower().capitalize()
                            if edit_priority.strip() == "":
                                edit_priority = edit_ticket.priority

                        edit_ticket.priority = edit_priority.lower().capitalize()

                        self.print_ticket_detail_table(edit_ticket)

                        while not edit_ticket_title:
                            print ("leave empty if you don't wish to change ticket title")
                            edit_ticket_title = input("New ticket title: ").strip()
                            if edit_ticket_title == "":
                                edit_ticket_title = edit_ticket.title
                                break

                        edit_ticket.title = edit_ticket_title

                        self.logic_api.ticket_edit(edit_ticket)
                else:
                    print(ui_consts.MSG_NO_PERMISSION)
                    print(ui_consts.MSG_ENTER_CONTINUE)
                    return None

            # process ticket
            case "pr":
                edit_recurring = -1
                process_cost = -1
                chosen_contractor = ""
                contractor_rating = -1
                contractor_fee = -1

                process_ticket = None

                while process_ticket is None:
                    process_ticket_ID = input("Type in ID of ticket to edit (B to cancel): ").upper()
                    if process_ticket_ID == "B":
                        return None

                    process_ticket = self.logic_api.ticket_get_by_ID(process_ticket_ID)

                    if process_ticket is None:
                        print(f"No ticket with ID '{process_ticket_ID}' found, try again.")

                if process_ticket.status == logic_consts.TICKET_STATUS_DONE and self.logic_api.is_manager_logged_in():
                    self.print_ticket_detail_table(process_ticket)

                    print ("This ticket is ready for completion")
                    answer = input("type yes/y if you want to mark this as complete: ").lower()

                    if answer == "yes" or answer == "y":
                        print ("\nleave empty if you wish to add nothing")
                        report = input("Type in comment to add to report: ").strip()

                        if report != "":
                            userID = self.logic_api.get_logged_in_staff().name
                            process_ticket.report += f"\n{userID} {report}"

                        process_ticket.status = logic_consts.TICKET_STATUS_CLOSED
                        process_ticket.close_date = datetime.now().strftime(ui_consts.DATE_FORMAT)

                        self.logic_api.ticket_edit(process_ticket)

                if process_ticket.status != logic_consts.TICKET_STATUS_CLOSED:
                    self.print_ticket_detail_table(process_ticket)

                    while edit_recurring < 0:
                        print (f"\nCurrent recur rate in days {process_ticket.recurring_days}")

                        try:
                            edit_recurring = int(input("New recur rate every X days (0 = never): "))
                        except ValueError:
                            print("\nInvalid input, Please enter a number")
                            edit_recurring = -1
                    process_ticket.recurring_days = edit_recurring

                    self.print_ticket_detail_table(process_ticket)

                    while process_cost < 0:
                        print (f"\nIf there was material cost, type in how much: ")
                        try:
                            process_cost = int(input("Type 0 if none: "))
                        except ValueError:
                            print ("please enter a valid number or leave empty.")
                            process_cost = -1
                    process_ticket.cost = process_cost

                    print ("\nWas a contractror involved in the ticket?")
                    contractor_answer = input("('yes' if so, anything else if not): ").lower()
                    if contractor_answer == "yes" or contractor_answer == "y":
                        self.print_ticket_detail_table(process_ticket)
                        
                        try:
                            process_ticket_destinationID = self.logic_api.property_get_by_ID(process_ticket.propertyID).destinationID
                        except Exception as e:
                            print(f"Error loading destination data for ticket'{process_ticket.ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK
                        try:
                            contractor_list = self.logic_api.contractor_get_by_destinationID(process_ticket_destinationID)
                        except Exception as e:
                            print(f"Error loading contractor data for destination'{process_ticket_destinationID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK                        

                        contractor_table = PrettyTable()
                        contractor_table.field_names = ["ID","Name","Rating", "phone", "opening hours", "type"]
                        for contractor_inst in contractor_list:
                            contractor_table.add_row([contractor_inst.ID,contractor_inst.name,contractor_inst.rating, contractor_inst.phone, contractor_inst.opening_hours, contractor_inst.contractor_type])

                        print(contractor_table)

                        validated_contractor = False
                        while not validated_contractor:
                            chosen_contractor = input("Choose ID of contractor you want to register for this job: ").upper()
                            for contractor in contractor_list:
                                if chosen_contractor == contractor.ID:
                                    validated_contractor = True
                        process_ticket.contractorID = chosen_contractor

                        print ("\nleave empty if you do not wish to add a review")
                        contractor_review = input ("Review of the job done: ")
                        process_ticket.contractor_review = contractor_review

                        while contractor_rating < 0 or contractor_rating > 10:
                            try:
                                contractor_rating = float(input("\ninput a rating for the contractor used from 0-10: "))
                            except ValueError:
                                print("Enter a valid number between 0 and 10.")
                                contractor_rating = -1
                        process_ticket.contractor_rating = contractor_rating

                        while contractor_fee <= 0:
                            try:
                                contractor_fee = int(input("How much was the fee for the contractor: "))
                            except ValueError:
                                print("Enter a positive interger.")
                                contractor_fee = -1
                        process_ticket.contractor_fee = contractor_fee

                    self.print_ticket_detail_table(process_ticket)

                    process_report = input ("\nWrite report here: ")
                    process_ticket.report = process_report

                    process_ticket.status = logic_consts.TICKET_STATUS_DONE

                    process_ticket.staffID = self.logic_api.get_logged_in_staff().ID
       
                    if contractor_answer == "yes" or contractor_answer == "y":
                        try:
                            self.logic_api.contractor_update_rating(process_ticket.contractorID)
                        except Exception as e:
                            print(f"Error updating rating for contractor '{process_ticket.contractorID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK          

                    self.print_ticket_detail_table(process_ticket)
                    print("This is the final version of the ticket.")
                    save_it = input("Is this acceptable(yes or y to agree, anything else to dismiss): ")
                    if save_it == "yes" or save_it == "y":
                        try:
                            self.logic_api.ticket_edit(process_ticket)
                        except Exception as e:
                            print(f"Error processing ticket '{process_ticket.ID}':")
                            print(f"{type(e).__name__}: {e}")
                            input(ui_consts.MSG_ENTER_BACK)
                            return ui_consts.CMD_BACK          
                    else:
                        return None

            # Search for
            case "s":
                self.active_search_filter = input(ui_consts.MSG_ENTER_SEARCH)

                print ("Use DD-MM-YYYY format")
                date_validated = False
                while not date_validated:
                    self.search_start_date = input("Enter start date (empty to clear filter): ")
                    if self.search_start_date != "":
                        try:
                            date_validated = datetime.strptime(self.search_start_date, ui_consts.DATE_FORMAT)
                        except ValueError:
                            print("Sorry wrong format, try again!")
                    else:
                        date_validated = True

                date_validated = False
                while not date_validated:
                    self.search_end_date = input("Enter end date (empty to clear filter): ")
                    if self.search_end_date != "":
                        try:
                            date_validated = datetime.strptime(self.search_end_date, ui_consts.DATE_FORMAT)
                        except ValueError:
                            print("Sorry wrong format, try again!")
                    else:
                        date_validated = True

                print(property_table)
                found_match = False
                while (filter_propertyID := input("Enter a property ID to filter by (empty to clear filter): ").upper()) != "":
                    for p in properties:
                        if p.ID == filter_propertyID:
                            found_match = True
                            break
                    if found_match:
                        break
                    else:
                        print(f"No property with the ID '{filter_propertyID}' found in your location.")
                self.filter_by_property = filter_propertyID

            # Go back
            case "b":
                return ui_consts.CMD_BACK

        return None

    def print_ticket_detail_table(self, ticket_by_id : Ticket) -> None:
        ticket_table = PrettyTable()

        try: 
            facility = self.logic_api.facility_get_by_ID(ticket_by_id.facilityID)
        except Exception as e:
            print(f"Error loading facility data for ticket '{ticket_by_id.ID}':")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK            
        
        if facility:
            facility_name = facility.name
        else:
            facility_name = "No facility"

        try:
            property_name = self.logic_api.property_get_by_ID(ticket_by_id.propertyID).name
        except Exception as e:
            print(f"Error loading property data for ticket'{ticket_by_id.ID}':")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK            

        try:    
            staff = self.logic_api.staff_get_by_ID(ticket_by_id.staffID)
        except Exception as e:
            print(f"Error loading staff data for ticket '{ticket_by_id.ID}':")
            print(f"{type(e).__name__}: {e}")
            input(ui_consts.MSG_ENTER_BACK)
            return ui_consts.CMD_BACK           
        if staff:
            staff_name = staff.name
        else:
            staff_name = "No staff"

        ticket_table.field_names = ["ID", ticket_by_id.ID]
        ticket_table.add_row(["Facility", facility_name], divider=True)
        ticket_table.add_row(["Property", property_name], divider=True)
        ticket_table.add_row(["Priority", ticket_by_id.priority], divider=True)
        ticket_table.add_row(["Title", ticket_by_id.title], divider=True)
        ticket_table.add_row(["Description", fill(ticket_by_id.description, width=50)], divider=True)
        ticket_table.add_row(["Status", ticket_by_id.status], divider=True)
        ticket_table.add_row(["Recurring?", ticket_by_id.recurring], divider=True)
        ticket_table.add_row(["Recurring days", ticket_by_id.recurring_days], divider=True)
        ticket_table.add_row(["Open date", ticket_by_id.open_date], divider=True)
        ticket_table.add_row(["Staff", staff_name], divider=True)
        if ticket_by_id.report:
            ticket_table.add_row(["Report", fill(ticket_by_id.report)], divider=True)
        ticket_table.add_row(["Cost", ticket_by_id.cost], divider=True)
        ticket_table.add_row(["Contractor", ticket_by_id.contractorID], divider=True)
        ticket_table.add_row(["Contr. review", ticket_by_id.contractor_review], divider=True)
        ticket_table.add_row(["Contr. rating", ticket_by_id.contractor_rating], divider=True)
        ticket_table.add_row(["Contractor fee", ticket_by_id.contractor_fee], divider=True)

        print(ticket_table.get_string())
