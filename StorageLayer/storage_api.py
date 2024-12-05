from StorageLayer.amenity_storage import AmenityStorage
from StorageLayer.contractor_storage import ContractorStorage
from StorageLayer.destination_storage import DestinationStorage
from StorageLayer.property_storage import PropertyStorage
from StorageLayer.report_storage import ReportStorage
from StorageLayer.staff_storage import StaffStorage
from StorageLayer.ticket_storage import TicketStorage

from Model import Property

class StorageAPI:
    def __init__(self):
        self.amenity_storage = AmenityStorage("filename.json")
        self.contractor_storage = ContractorStorage("filename.json")
        self.destination_storage = DestinationStorage("filename.json")
        self.property_storage = PropertyStorage("data/properties.json")
        self.report_storage = ReportStorage("filename.json")
        self.staff_storage = StaffStorage("filename.json")
        self.ticket_storage = TicketStorage("filename.json")

    def get_all_properties(self) -> list[Property]:
        return self.property_storage.load_from_file(Property)
