from LogicLayer.facility_manager import FacilityManager
from LogicLayer.contractor_manager import ContractorManager
from LogicLayer.destination_manager import DestinationManager
from LogicLayer.property_manager import PropertyManager
from LogicLayer.report_manager import ReportManager
from LogicLayer.staff_manager import StaffManager
from LogicLayer.ticket_manager import TicketManager

from Model import Property

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

    def get_logged_in_staff(self):
        return self.staff_manager.get_logged_in_staff()

    def get_all_properties(self):
        return self.property_manager.get_all_properties()
