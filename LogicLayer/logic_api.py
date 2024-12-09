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

    def authenticate_login(self, email, password):
        return self.staff_manager.authenticate_login(email, password)

    def logout(self):
        self.staff_manager.logout()


    #Destinations

    def get_all_destinations(self):
        return self.destination_manager.get_all_destinations()
    
    def add_new_destination(self, new_destination : str) -> None:
        self.destination_manager.add_new_destination(new_destination)
        return 

    def edit_destinations(self, destinations) -> None:
        self.destination_manager.edit_destination(destinations)
        return

    def get_logged_in_staff(self):
        return self.staff_manager.get_logged_in_staff()

    def get_all_properties(self):
        return self.property_manager.get_all_properties()
    
    def add_new_staff(self, new_staff:Staff):
        self.staff_manager.add_new_staff(new_staff)

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_add(self, new_property:Property):
        self.property_manager.property_add(new_property)

    def property_remove(self):
        pass

    def property_edit(self):
        pass

    def property_search(self):
        pass

    def view_facilites(self):
        pass

#==========================================================================

    def get_all_staff(self):
        return self.staff_manager.get_all_staff()

    def get_destination_by_ID(self, destinationID):
        return self.destination_manager.get_destination_by_ID(destinationID)

    def remove_staff(self, remove_id):
        return self.staff_manager.remove_staff(remove_id)
    
    def get_all_contractors(self):
        return self.contractor_manager.get_all_contractors()
