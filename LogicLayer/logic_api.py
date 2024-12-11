from LogicLayer.facility_manager import FacilityManager
from LogicLayer.contractor_manager import ContractorManager
from LogicLayer.destination_manager import DestinationManager
from LogicLayer.property_manager import PropertyManager
from LogicLayer.report_manager import ReportManager
from LogicLayer.staff_manager import StaffManager
from LogicLayer.ticket_manager import TicketManager

from Model import *

class LogicAPI:
    def __init__(self, storage_api):
        self.facility_manager = FacilityManager(storage_api)
        self.contractor_manager = ContractorManager(storage_api)
        self.destination_manager = DestinationManager(storage_api)
        self.property_manager = PropertyManager(storage_api)
        self.report_manager = ReportManager(storage_api)
        self.staff_manager = StaffManager(storage_api)
        self.ticket_manager = TicketManager(storage_api)

#==========================================================================
# --Contractors------------------------------------------------------------

    def contractor_get_all(self) -> list[Contractor]:
        return self.contractor_manager.contractor_get_all()

    def contractor_add(self, new_contractor : Contractor) -> None:
        self.contractor_manager.contractor_add(new_contractor)

    def contractor_remove(self, contractorID : str) -> None:
        self.contractor_manager.contractor_remove(contractorID)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        self.contractor_manager.contractor_edit(edited_contractor)

    def contractor_search(self, search_string : str) -> list[Contractor]:
        return self.contractor_manager.contractor_search(search_string)

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        return self.contractor_manager.contractor_get_by_ID(contractorID)

#==========================================================================
#--Destinations------------------------------------------------------------

    def destination_get_all(self) -> list[Destination]:
        """Returns a list of all available destinations"""
        return self.destination_manager.destination_get_all()

    def destination_add(self, new_destination : str) -> None:
        """Adds a new destination"""
        self.destination_manager.destination_add(new_destination)

    def destination_edit(self, edited_destination : Destination) -> None:
        """Modifies a destination"""
        self.destination_manager.destination_edit(edited_destination)

    def destination_get_by_ID(self, destinationID : str) -> Destination:
     #Returns a destination with a matching destinationID if it exists
        return self.destination_manager.destination_get_by_ID(destinationID)

#==========================================================================
# --Facilities-------------------------------------------------------------

    def facility_add(self, new_facility : Facility):
        self.facility_manager.facility_add(new_facility)

    def facility_remove(self, facilityID : str):
        return self.facility_manager.facility_remove(facilityID)

    def facility_edit(self, edited_facility : Facility):
        self.facility_manager.facility_edit(edited_facility)

    def facility_get_all(self) -> list[Facility]:
        return self.facility_manager.facility_get_all()

    def facility_get_by_propertyID(self, propertyID : str) -> list[Facility]:
        return self.facility_manager.facility_get_by_propertyID(propertyID)

    def facility_search(self, search_string : str) -> list[Facility]:
        return self.facility_manager.facility_search(search_string)

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        return self.facility_manager.facility_get_by_ID(facilityID)

    def facility_set_selected_property(self, propertyID : str) -> None:
        self.facility_manager.set_selected_property(propertyID)

    def facility_get_selected_property(self) -> str:
        return self.facility_manager.get_selected_property()

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_get_all(self) -> list[Property]:
        return self.property_manager.property_get_all()

    def property_get_by_ID(self, propertyID : str) -> Property:
        return self.property_manager.property_get_by_ID(propertyID)

    def property_add(self, new_property : Property) -> None:
        self.property_manager.property_add(new_property)

    def property_remove(self, propertyID : str) -> None:
        self.property_manager.property_remove(propertyID)

    def property_edit(self, property : Property) -> None:
        self.property_manager.property_edit(property)

    def property_search(self, search_string : str) -> list[Property]:
        return self.property_manager.property_search(search_string)

#==========================================================================
#--Staff-------------------------------------------------------------------

    def staff_get_all(self) -> list[Staff]:
        return self.staff_manager.staff_get_all()

    def staff_add(self, new_staff : Staff) -> None:
        self.staff_manager.staff_add(new_staff)

    def staff_edit(self, edited_staff : Staff) -> None:
        self.staff_manager.staff_edit(edited_staff)

    def staff_remove(self, staffID : str) -> None:
        self.staff_manager.staff_remove(staffID)

    def staff_get_by_ID(self, staffID : str) -> Staff:
        return self.staff_manager.staff_get_by_ID(staffID)

    def staff_search(self, search_string : str) -> list[Staff]:
        return self.staff_manager.staff_search(search_string)

#==========================================================================
#--Login/Session-----------------------------------------------------------

    def authenticate_login(self, email : str, password : str) -> bool:
        """Attempts to log in using a specified email/password combination"""
        return self.staff_manager.authenticate_login(email, password)

    def logout(self) -> None:
        """Invalidates the login status of the currently logged in user"""
        self.staff_manager.logout()

    def get_logged_in_staff(self) -> Staff:
        """Returns the currently logged in staff member"""
        return self.staff_manager.get_logged_in_staff()

    def is_manager_logged_in(self) -> bool:
        return self.staff_manager.is_manager_logged_in()

#==========================================================================
#--Tickets-----------------------------------------------------------------

    def ticket_get_all(self) -> list[Ticket]:
        return self.ticket_manager.ticket_get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        return self.ticket_manager.ticket_get_by_ID(ticketID)

    def ticket_add(self, new_ticket : Ticket) -> None:
        self.ticket_manager.ticket_add(new_ticket)

    def ticket_edit(self, edited_ticket : Ticket) -> None:
        self.ticket_manager.ticket_edit(edited_ticket)

    def ticket_remove(self, ticketID : str) -> None:
        self.ticket_manager.ticket_remove(ticketID)

    def ticket_search(self, search_string : str) -> list[Ticket]:
        return self.ticket_manager.ticket_search(search_string)
