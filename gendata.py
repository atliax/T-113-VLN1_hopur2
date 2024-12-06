from StorageLayer.facility_storage import FacilityStorage
from StorageLayer.contractor_storage import ContractorStorage
from StorageLayer.destination_storage import DestinationStorage
from StorageLayer.property_storage import PropertyStorage
from StorageLayer.report_storage import ReportStorage
from StorageLayer.staff_storage import StaffStorage
from StorageLayer.ticket_storage import TicketStorage

from Model import Facility
from Model import Contractor
from Model import Destination
from Model import Property
from Model import Report
from Model import Staff
from Model import Ticket

facility_storage = FacilityStorage("testdata/facilities.json")
contractor_storage = ContractorStorage("testdata/contractors.json")
destination_storage = DestinationStorage("testdata/destinations.json")
property_storage = PropertyStorage("testdata/properties.json")
report_storage = ReportStorage("testdata/reports.json")
staff_storage = StaffStorage("testdata/staff.json")
ticket_storage = TicketStorage("testdata/tickets.json")

destinations = []
properties = []
staff = []
facilities = []

destinations.append(Destination('1','1','Greenland','Nuuk','+299 33 21 65','06:00 - 23:30 alla daga'))

properties.append(Property('64-3900','1','iGloo-Ville móttökubygging','Aalisartut Aqqutaa 47, Nuuk 3900',0,0,'Móttaka'))

properties.append(Property('64-3901','1','iGloo-Ville 1','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3902','1','iGloo-Ville 2','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3903','1','iGloo-Ville 3','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3904','1','iGloo-Ville 4','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3905','1','iGloo-Ville 5','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3906','1','iGloo-Ville 6','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3907','1','iGloo-Ville 7','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3908','1','iGloo-Ville 8','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3909','1','iGloo-Ville 9','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('64-3910','1','iGloo-Ville 10','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))

staff.append(Staff('1','1','Minik Wallace','120369-1119','Isaajap Aqqutaa 1, 3900, Nuuk, Greenland','+299 34 24 67','+354 777 1361','minik.wallace@nanair.is','MiniSo1!','Yfirmaður Rekstrarsviðs',True))
staff.append(Staff('2','1','Aqqaluk Lynge','150675-2139','Qattaaq 44, 3905, Nuuk, Greenland','+299 35 24 66','+354 777 1362','aqqaluk.lynge@nanair.is','LyngAq44!','Starfsmaður',False))
staff.append(Staff('3','1','Nauja Lynge','211282-4159','Qunguleq 3759, 3905, Nuuk, Greenland','+299 31 21 64','+354 777 1363','nauja.lynge@nanair.is','NauLyn2','Starfsmaður',False))

facilities.append(Facility('1','64-3901','Snjóhús 1',''))
facilities.append(Facility('1','64-3902','Snjóhús 2',''))
facilities.append(Facility('1','64-3903','Snjóhús 3',''))
facilities.append(Facility('1','64-3904','Snjóhús 4',''))
facilities.append(Facility('1','64-3905','Snjóhús 5',''))
facilities.append(Facility('1','64-3906','Snjóhús 6',''))
facilities.append(Facility('1','64-3907','Snjóhús 7',''))
facilities.append(Facility('1','64-3908','Snjóhús 8',''))
facilities.append(Facility('1','64-3909','Snjóhús 9',''))
facilities.append(Facility('1','64-3910','Snjóhús 10',''))

destination_storage.save_to_file(destinations)
property_storage.save_to_file(properties)
staff_storage.save_to_file(staff)
facility_storage.save_to_file(facilities)
