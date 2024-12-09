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
#--Destinations--------------------------------------------------------------

    def get_all_destinations(self) -> list[Destination]:
        """Returns a list of all available destinations"""
        return self.destination_manager.get_all_destinations()
    
    def add_new_destination(self, new_destination : str) -> None:
        """Adds a new destination"""
        self.destination_manager.add_new_destination(new_destination)

    def edit_destinations(self, destinations) -> None:
        """Modifies a destination"""
        self.destination_manager.edit_destination(destinations)

    def get_destination_by_ID(self, destinationID : str) -> Destination:
        """Returns a destination with a matching destinationID if it exists"""
        return self.destination_manager.get_destination_by_ID(destinationID)

#==========================================================================
#--Properties--------------------------------------------------------------

    def get_all_properties(self) -> list[Property]:
        return self.property_manager.get_all_properties()

    def property_add(self, new_property : Property) -> None:
        self.property_manager.property_add(new_property)

    def property_remove(self, propertyID : str) -> None:
        self.property_manager.property_remove(propertyID)

    def property_edit(self, property : Property) -> None:
        self.property_manager.property_edit(property)

    def property_search(self):
        pass

#==========================================================================
#--Staff--------------------------------------------------------------

    def authenticate_login(self, email : str, password : str) -> bool:
        """Attempts to log in using a specified email/password combination"""
        return self.staff_manager.authenticate_login(email, password)

    def logout(self) -> None:
        """Invalidates the login status of the currently logged in user"""
        self.staff_manager.logout()

    def get_logged_in_staff(self) -> Staff:
        """Returns the currently logged in staff member"""
        return self.staff_manager.get_logged_in_staff()

    def get_all_staff(self) -> list[Staff]:
        return self.staff_manager.get_all_staff()

    def add_new_staff(self, new_staff : Staff) -> None:
        self.staff_manager.add_new_staff(new_staff)

    def edit_staff(self, staff : Staff) -> None:
        self.staff_manager.edit_staff(staff)

    def remove_staff(self, staffID : str) -> None:
        self.staff_manager.remove_staff(staffID)

#==========================================================================
# ----contractors----------------------------------------------------------   

    def get_all_contractors(self) -> list[Contractor]:
        return self.contractor_manager.get_all_contractors()
    
    def add_new_contractor(self, new_contractor : Contractor) -> None:
        self.contractor_manager.add_new_contractor(new_contractor)

    def remove_contractor(self, contractorID : str) -> None:
        self.contractor_manager.remove_contractor(contractorID)
    
    def edit_contractor(self, contractor: str) -> None:
        self.contractor_manager.edit_contractor(contractor)

    def contractor_search(self):
        pass

    def view_contractor_contact(self):
        pass

#==========================================================================
# ----facilities-----------------------------------------------------------

    def get_facilities_by_propertyID(self, propertyID : str) -> list[Facility]:
        return self.facility_manager.get_facilities_by_propertyID(propertyID)

    def add_new_facility(self,new_facility: Facility):
        self.facility_manager.add_new_facility(new_facility)
    
    def remove_facility(self, remove_id: str):
        return self.facility_manager.remove_facility(remove_id)
    
    def facility_search(self):
        pass

    def edit_facilities(self):
        pass

    def get_all_facilities(self) -> list[Facility]:
        return self.facility_manager.get_all_facilities()

    def view_facilites(self):
        pass