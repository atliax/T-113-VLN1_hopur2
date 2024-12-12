from StorageLayer import StorageAPI
from Exceptions import IDNotFoundError
from Model import Ticket

class TicketManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api

    def ticket_get_all(self) -> list[Ticket]:
        return self.storage_api.ticket_get_all()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        return self.storage_api.ticket_get_by_ID(ticketID)

    def ticket_add(self, new_ticket : Ticket) -> None:
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
        self.storage_api.ticket_edit(edited_ticket)

    def ticket_remove(self, ticketID : str) -> None:
        ticket_exists = self.storage_api.ticket_get_by_ID(ticketID)
        if ticket_exists:
            self.storage_api.ticket_remove(ticketID)
        else:
            raise IDNotFoundError(f" {ticketID} does not exist")

    def ticket_search(self, search_string : str) -> list[Ticket]:
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
