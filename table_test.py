from StorageLayer import StorageAPI

from prettytable import PrettyTable

from Model import Ticket

from textwrap import fill

storage = StorageAPI()

ticket = storage.ticket_get_by_ID('T2')

table = PrettyTable()

table.field_names = ["ID", ticket.ID]

table.add_row(["Facility", ticket.facilityID], divider=True)
table.add_row(["Property", ticket.propertyID], divider=True)
table.add_row(["Priority", ticket.priority], divider=True)
table.add_row(["Title", ticket.title], divider=True)
table.add_row(["Description", fill(ticket.description, width=50)], divider=True)
table.add_row(["Open?", ticket.open], divider=True)
table.add_row(["Status", ticket.status], divider=True)
table.add_row(["Recurring?", ticket.recurring], divider=True)
table.add_row(["Recurring days", ticket.recurring_days], divider=True)
table.add_row(["Open date", ticket.open_date], divider=True)
table.add_row(["Staff", ticket.staffID], divider=True)
table.add_row(["Report", ticket.report], divider=True)
table.add_row(["Cost", ticket.cost], divider=True)
table.add_row(["Contractor", ticket.contractorID], divider=True)
table.add_row(["Contr. review", ticket.contractor_review], divider=True)
table.add_row(["Contr. rating", ticket.contractor_rating], divider=True)
table.add_row(["Contractor fee", ticket.contractor_fee], divider=True)

print(table)
