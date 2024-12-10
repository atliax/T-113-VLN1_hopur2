from StorageLayer.storage_manager import StorageManager

from Model import *

class StorageAPI:
    def __init__(self):
        self.contractor_storage = StorageManager("data/contractors.json", Contractor)
        self.destination_storage = StorageManager("data/destinations.json", Destination)
        self.facility_storage = StorageManager("data/facilities.json", Facility)
        self.property_storage = StorageManager("data/properties.json", Property)
        self.report_storage = StorageManager("data/reports.json", Report)
        self.staff_storage = StorageManager("data/staff.json", Staff)
        self.ticket_storage = StorageManager("data/tickets.json", Ticket)

#==========================================================================
# ----contractors----------------------------------------------------------   

    def contractor_add(self, new_contractor : Contractor) -> None:
        self.contractor_storage.add(new_contractor)

    def contractor_remove(self, contractorID : str) -> None:
        self.contractor_storage.remove(contractorID)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        self.contractor_storage.edit(edited_contractor)

    def contractor_get_all(self):
        return self.contractor_storage.get_all()

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        return self.contractor_storage.get_by_ID(contractorID)

#==========================================================================
#--Destinations------------------------------------------------------------

    def destination_add(self, new_destination : Destination) -> None:
        self.destination_storage.add(new_destination)

    def destination_remove(self, destinationID : str) -> None:
        self.destination_storage.remove(destinationID)

    def destination_edit(self, edited_destination) -> None:
        self.destination_storage.edit(edited_destination)

    def destination_get_all(self) -> list[Destination]:
        return self.destination_storage.get_all()

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        return self.destination_storage.get_by_ID(destinationID)

#==========================================================================
#--Facilities--------------------------------------------------------------

    def facility_add(self, new_facility : Facility) -> None:
        self.facility_storage.add(new_facility)

    def facility_remove(self, facilityID : str) -> None:
        self.facility_storage.remove(facilityID)

    def facility_edit(self, edited_facility : Facility) -> None:
        self.facility_storage.edit(edited_facility)

    def facility_get_all(self) -> list[Facility]:
        return self.facility_storage.get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        return self.facility_storage.get_by_ID(facilityID)

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_add(self, new_property : Property) -> None:
        self.property_storage.add(new_property)

    def property_remove(self, propertyID : str) -> None:
        self.property_storage.remove(propertyID)

    def property_edit(self, edited_property : Property) -> None:
        self.property_storage.edit(edited_property)

    def property_get_all(self) -> list[Property]:
        return self.property_storage.get_all()

    def property_get_by_ID(self, propertyID : str) -> Property:
        return self.property_storage.get_by_ID(propertyID)

#==========================================================================
#--Reports-----------------------------------------------------------------

    def report_add(self, new_report : Report) -> None:
        self.report_storage.add(new_report)

    def report_remove(self, reportID : str) -> None:
        self.report_storage.remove(reportID)

    def report_edit(self, edited_report : Report) -> None:
        self.report_storage.edit(edited_report)

    def report_get_all(self) -> list[Report]:
        return self.report_storage.get_all()

    def report_get_by_ID(self, reportID : str) -> Report:
        return self.report_storage.get_by_ID(reportID)

#==========================================================================
#--Staff-------------------------------------------------------------------

    def staff_add(self, new_staff : Staff) -> None:
        self.staff_storage.add(new_staff)

    def staff_remove(self, staffID : str) -> None:
        self.staff_storage.remove(staffID)

    def staff_edit(self, edited_staff : Staff):
        self.staff_storage.edit(edited_staff)
    
    def staff_get_all(self) -> list[Staff]:
        return self.staff_storage.get_all()

    def staff_get_by_ID(self, staffID : str) -> Staff:
        return self.staff_storage.get_by_ID(staffID)

#==========================================================================
#--Tickets-----------------------------------------------------------------

    def ticket_add(self, new_ticket : Ticket) -> None:
        self.ticket_storage.add(new_ticket)

    def ticket_remove(self, ticketID : str) -> None:
        self.ticket_storage.remove(ticketID)

    def ticket_edit(self, edited_ticket : Ticket):
        self.ticket_storage.edit(edited_ticket)
    
    def ticket_get_all(self) -> list[Ticket]:
        return self.ticket_storage.get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        return self.ticket_storage.get_by_ID(ticketID)
