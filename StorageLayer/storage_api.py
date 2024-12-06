from StorageLayer.facility_storage import FacilityStorage
from StorageLayer.contractor_storage import ContractorStorage
from StorageLayer.destination_storage import DestinationStorage
from StorageLayer.property_storage import PropertyStorage
from StorageLayer.report_storage import ReportStorage
from StorageLayer.staff_storage import StaffStorage
from StorageLayer.ticket_storage import TicketStorage

from Model import Property
from Model import Destination

class StorageAPI:
    def __init__(self):
        self.facility_storage = FacilityStorage("filename.json")
        self.contractor_storage = ContractorStorage("filename.json")
        self.destination_storage = DestinationStorage("testdata/destinations.json")
        self.property_storage = PropertyStorage("testdata/properties.json")
        self.report_storage = ReportStorage("filename.json")
        self.staff_storage = StaffStorage("filename.json")
        self.ticket_storage = TicketStorage("filename.json")

    def get_all_properties(self) -> list[Property]:
        return self.property_storage.load_from_file(Property)
    
    def get_all_destinations(self) -> list[Destination]:
        return self.destination_storage.load_from_file(Destination)

    #def add_new_destination(self, new_destination_instance):
        #self.destination_storage