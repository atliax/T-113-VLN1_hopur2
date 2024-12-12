from LogicLayer.facility_manager import FacilityManager
from LogicLayer.contractor_manager import ContractorManager
from LogicLayer.destination_manager import DestinationManager
from LogicLayer.property_manager import PropertyManager
from LogicLayer.staff_manager import StaffManager
from LogicLayer.ticket_manager import TicketManager

from Model import *

class LogicAPI:
    def __init__(self, storage_api):
        self.facility_manager = FacilityManager(storage_api)
        self.contractor_manager = ContractorManager(storage_api)
        self.destination_manager = DestinationManager(storage_api)
        self.property_manager = PropertyManager(storage_api)
        self.staff_manager = StaffManager(storage_api)
        self.ticket_manager = TicketManager(storage_api)

#==========================================================================
#--Login/Session-----------------------------------------------------------

    def authenticate_login(self, email : str, password : str) -> bool:
        """Attempts to log in using a specified email/password combination"""
        return self.staff_manager.authenticate_login(email, password)

    def get_logged_in_staff(self) -> Staff:
        """Returns the currently logged in staff member"""
        return self.staff_manager.get_logged_in_staff()

    def is_manager_logged_in(self) -> bool:
        """Returns True if the currently logged in user is a manager, otherwise False."""
        return self.staff_manager.is_manager_logged_in()

    def logout(self) -> None:
        """Invalidates the login status of the currently logged in user"""
        self.staff_manager.logout()

#==========================================================================
# --Contractors------------------------------------------------------------

    def contractor_add(self, new_contractor : Contractor) -> None:
        """Takes a new contractor instance and adds it to the system."""
        self.contractor_manager.contractor_add(new_contractor)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        """Takes a contractor instance and replaces a contractor in the system that has the same ID."""
        self.contractor_manager.contractor_edit(edited_contractor)

    def contractor_get_all(self) -> list[Contractor]:
        """Returns a list of all the contractors that exist in the system."""
        return self.contractor_manager.contractor_get_all()

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        """Takes a contractor ID and returns a contractor from the system with the same ID if it exists."""
        return self.contractor_manager.contractor_get_by_ID(contractorID)

    def contractor_remove(self, contractorID : str) -> None:
        """Takes a contractor ID and removes it from the system."""
        self.contractor_manager.contractor_remove(contractorID)

    def contractor_search(self, search_string : str) -> list[Contractor]:
        """Takes a string and returns a list of contractors in the system that have attributes containing that string."""
        return self.contractor_manager.contractor_search(search_string)

#==========================================================================
#--Destinations------------------------------------------------------------

    def destination_add(self, new_destination : str) -> None:
        """Takes a new destination instance and adds it to the system."""
        self.destination_manager.destination_add(new_destination)

    def destination_edit(self, edited_destination : Destination) -> None:
        """Takes a destination instance and replaces a destination in the system that has the same ID."""
        self.destination_manager.destination_edit(edited_destination)

    def destination_get_all(self) -> list[Destination]:
        """Returns a list of all the destinations that exist in the system."""
        return self.destination_manager.destination_get_all()

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        """Takes a destination ID and returns a destination from the system with the same ID if it exists."""
        return self.destination_manager.destination_get_by_ID(destinationID)

#==========================================================================
# --Facilities-------------------------------------------------------------

    def facility_add(self, new_facility : Facility):
        """Takes a new facility instance and adds it to the system."""
        self.facility_manager.facility_add(new_facility)

    def facility_edit(self, edited_facility : Facility):
        """Takes a facility instance and replaces a facility in the system that has the same ID."""
        self.facility_manager.facility_edit(edited_facility)

    def facility_get_all(self) -> list[Facility]:
        """Returns a list of all the facilities that exist in the system."""
        return self.facility_manager.facility_get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        """Takes a facility ID and returns a facility from the system with the same ID if it exists."""
        return self.facility_manager.facility_get_by_ID(facilityID)

    def facility_get_by_propertyID(self, propertyID : str) -> list[Facility]:
        """Takes a property ID and returns a list of facilities that correspond to that property."""
        return self.facility_manager.facility_get_by_propertyID(propertyID)

    def facility_get_selected_property(self) -> str:
        """Returns the property ID that is currently the 'active' property on the Facility screen."""
        return self.facility_manager.get_selected_property()

    def facility_remove(self, facilityID : str):
        """Takes a facility ID and removes it from the system."""
        return self.facility_manager.facility_remove(facilityID)

    def facility_search(self, search_string : str) -> list[Facility]:
        """Takes a string and returns a list of facilities in the system that have attributes containing that string."""
        return self.facility_manager.facility_search(search_string)

    def facility_set_selected_property(self, propertyID : str) -> None:
        """Takes a property ID and sets that as the 'active' property on the Facility screen."""
        self.facility_manager.set_selected_property(propertyID)

    def facility_validate(self, facilityID : str, facility_list : list[Facility] ) -> bool:
        """Takes in a facility ID and a list of Facilities and returns True if the ID exists in the list, otherwise returns False."""
        return self.facility_manager.facility_validate(facilityID, facility_list)

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_add(self, new_property : Property) -> None:
        """Takes a new property instance and adds it to the system."""
        self.property_manager.property_add(new_property)

    def property_edit(self, property : Property) -> None:
        """Takes a property instance and replaces a property in the system that has the same ID."""
        self.property_manager.property_edit(property)

    def property_get_all(self) -> list[Property]:
        """Returns a list of all the properties that exist in the system."""
        return self.property_manager.property_get_all()

    def property_get_by_ID(self, propertyID : str) -> Property:
        """Takes a property ID and returns a property from the system with the same ID if it exists."""
        return self.property_manager.property_get_by_ID(propertyID)

    def property_remove(self, propertyID : str) -> None:
        """Takes a property ID and removes it from the system."""
        self.property_manager.property_remove(propertyID)

    def property_search(self, search_string : str) -> list[Property]:
        """Takes a string and returns a list of properties in the system that have attributes containing that string."""
        return self.property_manager.property_search(search_string)
    
    def property_validate(self, propertyID: str) -> bool:
        """Takes in a property ID and returns True if it exists in the system, otherwise returns False."""
        return self.property_manager.validate_property(propertyID)

#==========================================================================
#--Staff-------------------------------------------------------------------

    def staff_add(self, new_staff : Staff) -> None:
        """Takes a new staff instance and adds it to the system."""
        self.staff_manager.staff_add(new_staff)

    def staff_edit(self, edited_staff : Staff) -> None:
        """Takes a staff instance and replaces a staff in the system that has the same ID."""
        self.staff_manager.staff_edit(edited_staff)

    def staff_get_all(self) -> list[Staff]:
        """Returns a list of all the staff that exist in the system."""
        return self.staff_manager.staff_get_all()

    def staff_get_by_ID(self, staffID : str) -> Staff:
        """Takes a staff ID and returns a staff instance from the system with the same ID if it exists."""
        return self.staff_manager.staff_get_by_ID(staffID)

    def staff_list_managers(self) -> list[Staff]:
        """Returns a list of all the staff that have manager status."""
        return self.staff_manager.staff_list_managers()

    def staff_remove(self, staffID : str) -> None:
        """Takes a staff ID and removes it from the system."""
        self.staff_manager.staff_remove(staffID)

    def staff_search(self, search_string : str) -> list[Staff]:
        """Takes a string and returns a list of staff in the system that have attributes containing that string."""
        return self.staff_manager.staff_search(search_string)

#==========================================================================
#--Tickets-----------------------------------------------------------------

    def ticket_add(self, new_ticket : Ticket) -> None:
        """Takes a new ticket instance and adds it to the system."""
        self.ticket_manager.ticket_add(new_ticket)

    def ticket_edit(self, edited_ticket : Ticket) -> None:
        """Takes a ticket instance and replaces a ticket in the system that has the same ID."""
        self.ticket_manager.ticket_edit(edited_ticket)

    def ticket_get_all(self) -> list[Ticket]:
        """Returns a list of all the tickets that exist in the system."""
        return self.ticket_manager.ticket_get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        """Takes a ticket ID and returns a ticket from the system with the same ID if it exists."""
        return self.ticket_manager.ticket_get_by_ID(ticketID)

    def ticket_remove(self, ticketID : str) -> None:
        """Takes a ticket ID and removes it from the system."""
        self.ticket_manager.ticket_remove(ticketID)

    def ticket_search(self, search_string : str) -> list[Ticket]:
        """Takes a string and returns a list of tickets in the system that have attributes containing that string."""
        return self.ticket_manager.ticket_search(search_string)

#==========================================================================
#--Time-----------------------------------------------------------------

    #def add_new_time(self, time : str) -> 
