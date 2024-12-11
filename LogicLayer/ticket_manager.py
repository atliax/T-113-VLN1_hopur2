from StorageLayer import StorageAPI

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
        n = int(all_tickets[len(all_tickets)-1].ID[1:])
        n += 1
        new_id = "T" + str(n)
        new_ticket.ID = new_id

        self.storage_api.ticket_add(new_ticket)

    def ticket_edit(self, edited_ticket : Ticket) -> None:
        self.storage_api.ticket_edit(edited_ticket)

    def ticket_remove(self, ticketID : str) -> None:
        self.storage_api.ticket_remove(ticketID)

    def ticket_search(self, search_string : str) -> list[Ticket]:
        # TODO
        return []
