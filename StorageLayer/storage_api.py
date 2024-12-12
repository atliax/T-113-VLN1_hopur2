from StorageLayer.storage_manager import StorageManager

from Model import *

class StorageAPI:
    def __init__(self):
        self.contractor_storage = StorageManager("data/contractors.json", Contractor)
        self.destination_storage = StorageManager("data/destinations.json", Destination)
        self.facility_storage = StorageManager("data/facilities.json", Facility)
        self.property_storage = StorageManager("data/properties.json", Property)
        self.staff_storage = StorageManager("data/staff.json", Staff)
        self.ticket_storage = StorageManager("data/tickets.json", Ticket)

#==========================================================================
# ----contractors----------------------------------------------------------   

    def contractor_add(self, new_contractor : Contractor) -> None:
        """Takes an instance of a contractor and removes it from the data file."""
        self.contractor_storage.add(new_contractor)

    def contractor_remove(self, contractorID : str) -> None:
        """Takes a contractor ID and removes the corresponding item from the data file."""
        self.contractor_storage.remove(contractorID)

    def contractor_edit(self, edited_contractor : Contractor) -> None:
        """Takes a contractor instance and replaces a contractor from the data file with a corresponding ID."""
        self.contractor_storage.edit(edited_contractor)

    def contractor_get_all(self):
        """Returns a list of all the contractors from the data file."""
        return self.contractor_storage.get_all()

    def contractor_get_by_ID(self, contractorID : str) -> Contractor:
        """Takes an ID and returns an instance of the corresponding contractor from the data file."""
        return self.contractor_storage.get_by_ID(contractorID)

#==========================================================================
#--Destinations------------------------------------------------------------

    def destination_add(self, new_destination : Destination) -> None:
        """Takes an instance of a destination and removes it from the data file."""
        self.destination_storage.add(new_destination)

    def destination_remove(self, destinationID : str) -> None:
        """Takes a destination ID and removes the corresponding item from the data file."""
        self.destination_storage.remove(destinationID)

    def destination_edit(self, edited_destination) -> None:
        """Takes a destination instance and replaces a destination from the data file with a corresponding ID."""
        self.destination_storage.edit(edited_destination)

    def destination_get_all(self) -> list[Destination]:
        """Returns a list of all the destinations from the data file."""
        return self.destination_storage.get_all()

    def destination_get_by_ID(self, destinationID : str) -> Destination:
        """Takes an ID and returns an instance of the corresponding destination from the data file."""
        return self.destination_storage.get_by_ID(destinationID)

#==========================================================================
#--Facilities--------------------------------------------------------------

    def facility_add(self, new_facility : Facility) -> None:
        """Takes an instance of a facility and removes it from the data file."""
        self.facility_storage.add(new_facility)

    def facility_remove(self, facilityID : str) -> None:
        """Takes a facility ID and removes the corresponding item from the data file."""
        self.facility_storage.remove(facilityID)

    def facility_edit(self, edited_facility : Facility) -> None:
        """Takes a facility instance and replaces a facility from the data file with a corresponding ID."""
        self.facility_storage.edit(edited_facility)

    def facility_get_all(self) -> list[Facility]:
        """Returns a list of all the facilities from the data file."""
        return self.facility_storage.get_all()

    def facility_get_by_ID(self, facilityID : str) -> Facility:
        """Takes an ID and returns an instance of the corresponding facility from the data file."""
        return self.facility_storage.get_by_ID(facilityID)

#==========================================================================
#--Properties--------------------------------------------------------------

    def property_add(self, new_property : Property) -> None:
        """Takes an instance of a property and removes it from the data file."""
        self.property_storage.add(new_property)

    def property_remove(self, propertyID : str) -> None:
        """Takes a property ID and removes the corresponding item from the data file."""
        self.property_storage.remove(propertyID)

    def property_edit(self, edited_property : Property) -> None:
        """Takes a property instance and replaces a property from the data file with a corresponding ID."""
        self.property_storage.edit(edited_property)

    def property_get_all(self) -> list[Property]:
        """Returns a list of all the properties from the data file."""
        return self.property_storage.get_all()

    def property_get_by_ID(self, propertyID : str) -> Property:
        """Takes an ID and returns an instance of the corresponding property from the data file."""
        return self.property_storage.get_by_ID(propertyID)

#==========================================================================
#--Staff-------------------------------------------------------------------

    def staff_add(self, new_staff : Staff) -> None:
        """Takes an instance of staff and removes it from the data file."""
        self.staff_storage.add(new_staff)

    def staff_remove(self, staffID : str) -> None:
        """Takes a staff ID and removes the corresponding item from the data file."""
        self.staff_storage.remove(staffID)

    def staff_edit(self, edited_staff : Staff):
        """Takes a staff instance and replaces a staff item from the data file with a corresponding ID."""
        self.staff_storage.edit(edited_staff)
    
    def staff_get_all(self) -> list[Staff]:
        """Returns a list of all the staff from the data file."""
        return self.staff_storage.get_all()

    def staff_get_by_ID(self, staffID : str) -> Staff:
        """Takes an ID and returns an instance of the corresponding staff from the data file."""
        return self.staff_storage.get_by_ID(staffID)

#==========================================================================
#--Tickets-----------------------------------------------------------------

    def ticket_add(self, new_ticket : Ticket) -> None:
        """Takes an instance of a ticket and removes it from the data file."""
        self.ticket_storage.add(new_ticket)

    def ticket_remove(self, ticketID : str) -> None:
        """Takes a ticket ID and removes the corresponding item from the data file."""
        self.ticket_storage.remove(ticketID)

    def ticket_edit(self, edited_ticket : Ticket):
        """Takes a ticket instance and replaces a ticket from the data file with a corresponding ID."""
        self.ticket_storage.edit(edited_ticket)
    
    def ticket_get_all(self) -> list[Ticket]:
        """Returns a list of all the tickets from the data file."""
        return self.ticket_storage.get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        """Takes an ID and returns an instance of the corresponding ticket from the data file."""
        return self.ticket_storage.get_by_ID(ticketID)
