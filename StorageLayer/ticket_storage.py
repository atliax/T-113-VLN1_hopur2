from StorageLayer.base_storage import BaseStorage

from Model import Ticket

class TicketStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def ticket_add(self, new_ticket : Ticket) -> None:
        current_tickets = self.load_from_file()
        current_tickets.append(new_ticket)
        self.save_to_file(current_tickets)

    def ticket_remove(self, ticketID : str) -> None:
        current_tickets : list[Ticket] = self.load_from_file()

        updated_tickets = []
        for ticket in current_tickets:
            if ticket.ticketID != ticketID:
                updated_tickets.append(ticket)

        self.save_to_file(updated_tickets)
    
    def ticket_edit(self, edited_ticket : Ticket) -> None:
        current_tickets : list[Ticket] = self.load_from_file()

        updated_tickets = []
        for ticket in current_tickets:
            if ticket.ticketID == edited_ticket.ticketID:
                updated_tickets.append(edited_ticket)
            else:
                updated_tickets.append(ticket)

        self.save_to_file(updated_tickets)

    def ticket_get_all(self) -> list[Ticket]:
        return self.load_from_file()

    def ticket_get_by_ID(self, ticketID : str) -> Ticket:
        current_tickets : list[Ticket] = self.load_from_file()

        for ticket in current_tickets:
            if ticket.ticketID == ticketID:
                return ticket

    def ticket_search(self, search_string : str) -> list[Ticket]:
        return []
