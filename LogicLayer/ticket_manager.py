from datetime import datetime

from StorageLayer import StorageAPI
from Exceptions import IDNotFoundError
from Model import Ticket

class TicketManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api

    def ticket_add(self, new_ticket : Ticket) -> None:
        """Takes a new ticket instance and adds it to the system."""
        all_tickets = self.storage_api.ticket_get_all()
        if len(all_tickets) != 0:
            n = int(all_tickets[len(all_tickets)-1].ID[1:])
        else:
            n = 0

        n += 1
        new_id = "T" + str(n)
        new_ticket.ID = new_id

        self.storage_api.ticket_add(new_ticket)

    def ticket_edit(self, edited_ticket : Ticket) -> None:
        """Takes a ticket instance and replaces a ticket in the system that has the same ID."""
        self.storage_api.ticket_edit(edited_ticket)

    def ticket_get_all(self) -> list[Ticket]:
        """Returns a list of all the tickets that exist in the system."""
        return self.storage_api.ticket_get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        """Takes a ticket ID and returns a ticket from the system with the same ID if it exists."""
        return self.storage_api.ticket_get_by_ID(ticketID)

    def ticket_remove(self, ticketID : str) -> None:
        """Takes a ticket ID and removes it from the system."""
        ticket_exists = self.storage_api.ticket_get_by_ID(ticketID)
        if ticket_exists:
            self.storage_api.ticket_remove(ticketID)
        else:
            raise IDNotFoundError(f" {ticketID} does not exist")

    def ticket_search_only_destinationID(self, search_string : str, destinationID : str, start_date : str, end_date : str) -> list[Ticket]:
        searched_tickets = self.ticket_search(search_string)

        # create datetime objects from the date strings if applicable
        if start_date != "":
            start_date = datetime.strptime(start_date,"%d-%m-%Y")
        if end_date != "":
            end_date = datetime.strptime(end_date,"%d-%m-%Y")

        filtered_tickets : list[Ticket] = []

        # first filter by keyword ("" will return all of them)
        for ticket in searched_tickets:
            if self.storage_api.property_get_by_ID(ticket.propertyID).destinationID == destinationID:
                filtered_tickets.append(ticket)

        # then filter by start date if applicable
        searched_tickets = filtered_tickets[:]
        if start_date:
            filtered_tickets = []
            for ticket in searched_tickets:
                ticket_date = datetime.strptime(ticket.open_date,"%d-%m-%Y")
                if ticket_date >= start_date:
                    filtered_tickets.append(ticket)

        # finally filter by end date if applicable
        searched_tickets = filtered_tickets[:]
        if end_date:
            filtered_tickets = []
            for ticket in searched_tickets:
                ticket_date = datetime.strptime(ticket.open_date,"%d-%m-%Y")
                if ticket_date <= end_date:
                    filtered_tickets.append(ticket)

        return filtered_tickets

    def ticket_get_by_destinationID(self, destinationID : str) -> list[Ticket]:
        all_tickets : list[Ticket] = self.ticket_get_all()
        filtered_tickets = []
        for ticket in all_tickets:
            if self.storage_api.property_get_by_ID(ticket.propertyID).destinationID == destinationID:
                filtered_tickets.append(ticket)

        return filtered_tickets

    def ticket_search(self, search_string : str) -> list[Ticket]:
        """Takes a string and returns a list of tickets in the system that have attributes containing that string."""
        all_tickets : list[Ticket] = self.storage_api.ticket_get_all()
        filtered_tickets = []
        for item in all_tickets:
            found = False
            for attribute_value in list(item.__dict__.values()):
                if search_string.lower() in str(attribute_value).lower():
                    filtered_tickets.append(item)
                    found = True
                    break

            if not found:
                ticket_property = self.storage_api.property_get_by_ID(item.propertyID)
                if ticket_property is not None:
                    if search_string.lower() in ticket_property.name.lower():
                        filtered_tickets.append(item)
                        found = True
                        continue

            if not found:
                ticket_facility = self.storage_api.facility_get_by_ID(item.facilityID)
                if ticket_facility is not None:
                    if search_string.lower() in ticket_facility.name.lower():
                        filtered_tickets.append(item)
                        found = True
                        continue

        return filtered_tickets

    def ticket_update_pending(self) -> None:
        pass

    def ticket_update_recurring(self) -> None:
        pass
