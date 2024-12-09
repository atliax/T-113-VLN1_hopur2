from StorageLayer.facility_storage import FacilityStorage
from StorageLayer.contractor_storage import ContractorStorage
from StorageLayer.destination_storage import DestinationStorage
from StorageLayer.property_storage import PropertyStorage
from StorageLayer.report_storage import ReportStorage
from StorageLayer.staff_storage import StaffStorage
from StorageLayer.ticket_storage import TicketStorage

from Model import *

facility_storage = FacilityStorage("data/facilities.json", Facility)
contractor_storage = ContractorStorage("data/contractors.json", Contractor)
destination_storage = DestinationStorage("data/destinations.json", Destination)
property_storage = PropertyStorage("data/properties.json", Property)
report_storage = ReportStorage("data/reports.json", Report)
staff_storage = StaffStorage("data/staff.json", Staff)
ticket_storage = TicketStorage("data/tickets.json", Ticket)

destinations = []
properties = []
staff = []
facilities = []
contractors = []

# ------------------------------- Nuuk, Grænland: ------------------------------

destinations.append(Destination('D1','S1','Grænland','Nuuk','+299 33 21 65','06:00 - 23:30 alla daga'))

#64-3900 -> P1
properties.append(Property('P1','D1','iGloo-Ville móttökubygging','Aalisartut Aqqutaa 47, Nuuk 3900',0,0,'Móttaka'))

#64-3901 -> P2
#64-3910 -> P11
properties.append(Property('P2','D1','iGloo-Ville 1','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P3','D1','iGloo-Ville 2','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P4','D1','iGloo-Ville 3','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P5','D1','iGloo-Ville 4','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P6','D1','iGloo-Ville 5','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P7','D1','iGloo-Ville 6','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P8','D1','iGloo-Ville 7','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P9','D1','iGloo-Ville 8','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P10','D1','iGloo-Ville 9','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))
properties.append(Property('P11','D1','iGloo-Ville 10','Aalisartut Aqqutaa 47, Nuuk 3900',35,1,'Snjóhús'))

staff.append(Staff('S1','D1','Minik Wallace','120369-1119','Isaajap Aqqutaa 1, 3900, Nuuk, Greenland','+299 34 24 67','+354 777 1361','minik.wallace@nanair.is','MiniSo1!','Yfirmaður Rekstrarsviðs',True))
staff.append(Staff('S2','D1','Aqqaluk Lynge','150675-2139','Qattaaq 44, 3905, Nuuk, Greenland','+299 35 24 66','+354 777 1362','aqqaluk.lynge@nanair.is','LyngAq44!','Starfsmaður',False))
staff.append(Staff('S3','D1','Nauja Lynge','211282-4159','Qunguleq 3759, 3905, Nuuk, Greenland','+299 31 21 64','+354 777 1363','nauja.lynge@nanair.is','NauLyn2','Starfsmaður',False))

facilities.append(Facility('F1','P2','Snjóhús 1',''))
facilities.append(Facility('F2','P3','Snjóhús 2',''))
facilities.append(Facility('F3','P4','Snjóhús 3',''))
facilities.append(Facility('F4','P5','Snjóhús 4',''))
facilities.append(Facility('F5','P6','Snjóhús 5',''))
facilities.append(Facility('F6','P7','Snjóhús 6',''))
facilities.append(Facility('F7','P8','Snjóhús 7',''))
facilities.append(Facility('F8','P9','Snjóhús 8',''))
facilities.append(Facility('F9','P10','Snjóhús 9',''))
facilities.append(Facility('F10','P11','Snjóhús 10',''))

contractors.append(Contractor('C1','D1','4.4','Börnunarþjónusta Ísmannsins', 'Mamma ísmannsins', '+299 85 45 58', 'Inuit 3', '21:00 - 23:00 alla daga','Penetrator'))

# ----------------------------- Þórshöfn, Færeyjar: ----------------------------
################################################################################

destinations.append(Destination('D2','S4','Færeyjar','Tórshavn','+298 31 45 44','24/7'))

#ix-9331 -> P12
#ix-9332 -> P13
#ix-9333 -> P14
properties.append(Property("P12",'D2',"Skákið","Skákið 15, 100, Tórshavn","100","3","Raðhús"))
properties.append(Property("P13",'D2',"Skákið","Skákið 15, 100, Tórshavn","100","3","Raðhús"))
properties.append(Property("P14",'D2',"Skákið","Skákið 15, 100, Tórshavn","100","3","Raðhús"))

#ix-2239 -> P15
properties.append(Property("P15",'D2',"Svalbarðsvegur guesthouse","Svalbarðsvegur 22, 100, Tórshavn","200","5","Einbýlishús"))

#ix-9492 -> P16
#ix-9501 -> P25
properties.append(Property("P16",'D2',"DirtGlooVille 1","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P17",'D2',"DirtGlooVille 2","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P18",'D2',"DirtGlooVille 3","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P19",'D2',"DirtGlooVille 4","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P20",'D2',"DirtGlooVille 5","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P21",'D2',"DirtGlooVille 6","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P22",'D2',"DirtGlooVille 7","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P23",'D2',"DirtGlooVille 8","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P24",'D2',"DirtGlooVille 9","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))
properties.append(Property("P25",'D2',"DirtGlooVille 10","Nýggivegur 1, 100, Tórshavn","15","1","Moldarhús"))

staff.append(Staff('S4','D2','Annette Djurhuus','250976-3149','Tjarnardeild 8, 100, Tórshavn, Faroe Islands','+298 77 20 00','+354 777 1381','annette.djurhuus@nanair.is','AnnDjur1!','Yfirmaður Rekstrarsviðs',True))
staff.append(Staff('S5','D2','Áki Knudsen','311281-3239','Traðartún 3, 108, Argir, Faroe Islands','+298 61 72 10','+354 777 1381','aki.knudsen@nanair.is','Aknuds3112!','Starfsmaður',False))
staff.append(Staff('S6','D2','André Hjaltalín','150189-8179','Í Lágni 19, 100, Tórshavn, Faroe Islands','+298 66 14 41','+354 777 1382','Andre.hjaltalin@nanair.is','AndHjal31!','Starfsmaður',False))

facilities.append(Facility('F11','P16','Moldarhús 1',''))
facilities.append(Facility('F12','P17','Moldarhús 2',''))
facilities.append(Facility('F13','P18','Moldarhús 3',''))
facilities.append(Facility('F14','P19','Moldarhús 4',''))
facilities.append(Facility('F15','P20','Moldarhús 5',''))
facilities.append(Facility('F16','P21','Moldarhús 6',''))
facilities.append(Facility('F17','P22','Moldarhús 7',''))
facilities.append(Facility('F18','P23','Moldarhús 8',''))
facilities.append(Facility('F19','P24','Moldarhús 9',''))
facilities.append(Facility('F20','P25','Moldarhús 10',''))
facilities.append(Facility('F21','P12','Skákið hús 1',''))
facilities.append(Facility('F22','P13','Skákið hús 2',''))
facilities.append(Facility('F23','P14','Skákið hús 3',''))
facilities.append(Facility('F24','P15','Svalbarðsvegur guesthouse',''))

# ------------------------------- Nuuk, Grænland: ------------------------------
################################################################################

#somethingmore

# -------------------------- write to the actual files -------------------------

destination_storage.save_to_file(destinations)
property_storage.save_to_file(properties)
staff_storage.save_to_file(staff)
facility_storage.save_to_file(facilities)
contractor_storage.save_to_file(contractors)
