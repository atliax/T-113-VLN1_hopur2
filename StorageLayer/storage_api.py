from StorageLayer.facility_storage import FacilityStorage
from StorageLayer.contractor_storage import ContractorStorage
from StorageLayer.destination_storage import DestinationStorage
from StorageLayer.property_storage import PropertyStorage
from StorageLayer.report_storage import ReportStorage
from StorageLayer.staff_storage import StaffStorage
from StorageLayer.ticket_storage import TicketStorage

# TODO: skoða sameiningu á storage klösum í einn

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

#==========================================================================
# ----contractors----------------------------------------------------------   

    def contractor_get_all(self):
        return self.contractor_storage.contractor_get_all()

    def contractor_add(self, new_contractor : Contractor) -> None:
        self.contractor_storage.contractor_add(new_contractor)

    def contractor_remove(self, contractorID : str) -> None:
        self.contractor_storage.contractor_remove(contractorID)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        self.contractor_storage.contractor_edit(edited_contractor)

    def contractor_search(self, search_string : str) -> list[Contractor]:
        return self.contractor_storage.contractor_search(search_string)

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        return self.contractor_storage.contractor_get_by_ID(contractorID)

#==========================================================================
#--Destinations------------------------------------------------------------

    def destination_add(self, new_destination : Destination) -> None:
        self.destination_storage.destination_add(new_destination)

    def destination_remove(self, destinationID : str) -> None:
        self.destination_storage.destination_remove(destinationID)

    def destination_edit(self, edited_destination) -> None:
        self.destination_storage.destination_edit(edited_destination)

    def destination_get_all(self) -> list[Destination]:
        return self.destination_storage.destination_get_all()

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        return self.destination_storage.destination_get_by_ID(destinationID)

    def destination_search(self, search_string : str) -> list[Destination]:
        return self.destination_search(search_string)

#==========================================================================
#--Facilities--------------------------------------------------------------

    def facility_add(self, new_facility : Facility) -> None:
        self.facility_storage.facility_add(new_facility)

    def facility_remove(self, facilityID : str) -> None:
        self.facility_storage.facility_remove(facilityID)

    def facility_edit(self, edited_facility : Facility) -> None:
        self.facility_storage.facility_edit(edited_facility)

    def facility_get_all(self) -> list[Facility]:
        return self.facility_storage.facility_get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        return self.facility_storage.facility_get_by_ID(facilityID)

    def facility_search(self, search_string : str) -> list[Facility]:
        return self.facility_storage.facility_search(search_string)

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_add(self, new_property : Property) -> None:
        self.property_storage.property_add(new_property)

    def property_remove(self, propertyID : str) -> None:
        self.property_storage.property_remove(propertyID)

    def property_edit(self, edited_property : Property) -> None:
        self.property_storage.property_edit(edited_property)

    def property_get_all(self) -> list[Property]:
        return self.property_storage.property_get_all()

    def property_get_by_ID(self, propertyID : str) -> Property:
        return self.property_storage.property_get_by_ID(propertyID)

    def property_search(self, search_string : str) -> list[Property]:
        return self.property_storage.property_search(search_string)

#==========================================================================
#--Reports-----------------------------------------------------------------

    def report_add(self, new_report : Report) -> None:
        self.report_storage.report_add(new_report)

    def report_remove(self, reportID : str) -> None:
        self.report_storage.report_remove(reportID)

    def report_edit(self, edited_report : Report) -> None:
        self.report_storage.report_edit(edited_report)

    def report_get_all(self) -> list[Report]:
        return self.report_storage.report_get_all()

    def report_get_by_ID(self, reportID : str) -> Report:
        return self.report_storage.report_get_by_ID(reportID)

    def report_search(self, search_string : str) -> list[Report]:
        return self.report_storage.report_search(search_string)

#==========================================================================
#--Staff-------------------------------------------------------------------

    def staff_add(self, new_staff : Staff) -> None:
        self.staff_storage.staff_add(new_staff)

    def staff_remove(self, staffID : str) -> None:
        self.staff_storage.staff_remove(staffID)

    def staff_edit(self, edited_staff : Staff):
        self.staff_storage.staff_edit(edited_staff)
    
    def staff_get_all(self) -> list[Staff]:
        return self.staff_storage.staff_get_all()

    def staff_get_by_ID(self, staffID : str) -> Staff:
        return self.staff_storage.staff_get_by_ID(staffID)

    def staff_search(self, search_string : str) -> list[Staff]:
        return self.staff_storage.staff_search(search_string)

#==========================================================================
#--Tickets-----------------------------------------------------------------

    def ticket_add(self, new_ticket : Ticket) -> None:
        self.ticket_storage.ticket_add(new_ticket)

    def ticket_remove(self, ticketID : str) -> None:
        self.ticket_storage.ticket_remove(ticketID)

    def ticket_edit(self, edited_ticket : Ticket):
        self.ticket_storage.ticket_edit(edited_ticket)
    
    def ticket_get_all(self) -> list[Ticket]:
        return self.ticket_storage.ticket_get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        return self.ticket_storage.ticket_get_by_ID(ticketID)

    def ticket_search(self, search_string : str) -> list[Ticket]:
        return self.ticket_storage.ticket_search(search_string)
