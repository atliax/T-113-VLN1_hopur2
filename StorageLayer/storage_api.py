from StorageLayer.facility_storage import FacilityStorage
from StorageLayer.contractor_storage import ContractorStorage
from StorageLayer.destination_storage import DestinationStorage
from StorageLayer.property_storage import PropertyStorage
from StorageLayer.report_storage import ReportStorage
from StorageLayer.staff_storage import StaffStorage
from StorageLayer.ticket_storage import TicketStorage

from Model import *

class StorageAPI:
    def __init__(self):
        self.facility_storage = FacilityStorage("data/facilities.json", Facility)
        self.contractor_storage = ContractorStorage("data/contractors.json", Contractor)
        self.destination_storage = DestinationStorage("data/destinations.json", Destination)
        self.property_storage = PropertyStorage("data/properties.json", Property)
        self.report_storage = ReportStorage("data/reports.json", Report)
        self.staff_storage = StaffStorage("data/staff.json", Staff)
        self.ticket_storage = TicketStorage("data/tickets.json", Ticket)

    def get_all_properties(self) -> list[Property]:
        return self.property_storage.load_from_file()
    
    def get_all_destinations(self) -> list[Destination]:
        return self.destination_storage.load_from_file()

    def get_all_staff(self) -> list[Staff]:
        return self.staff_storage.load_from_file()

    def add_new_staff(self, new_staff : Staff):
        self.staff_storage.add_new_staff(new_staff)

    def add_new_destination(self, new_destination : Destination):
        self.destination_storage.add_new_destination(new_destination)
        return

    def edit_destination(self, destinations):
        self.destination_storage.edit_destination(destinations)
        return

    def remove_staff(self, remove_id):
        return self.staff_storage.remove_staff(remove_id)
    
    def get_all_facilities(self) -> list[Facility]:
        return self.facility_storage.load_from_file()
    
    def add_new_facility(self, new_facility : Facility):
        self.facility_storage.add_new_facility(new_facility)

    def get_all_contractors(self) -> list[Contractor]:
        return self.contractor_storage.load_from_file()

    
    def add_new_contractor(self, new_contractor : Contractor):
        self.contractor_storage.add_new_contractor(new_contractor)
    def add_new_contractor(self, new_contractor : Contractor):
        self.contractor_storage.add_new_contractor(new_contractor)

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_add(self):
        self.property_storage.property_add(new_property)

    def property_remove(self):
        pass

    def property_edit(self):
        pass

    def property_search(self):
        pass

#==========================================================================
