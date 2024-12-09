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

# -------------------------- Longyearbyen, Svalbarði: --------------------------

destinations.append(Destination('D3','S7','Svalbarði','Longyearbyen','PHONE','24/7'))

properties.append(Property('P26','D3','Vei BnB','Vei 217, Longyearbyen, Svalbarði', 150, 4, 'Einbýlishús'))
properties.append(Property('P27','D3','Hótel Akúla','Longyearbyen Harbor 1, Longyearbyen, Svalbarði',5000,80,'Kafbátur'))

staff.append(Staff('sID','dID','name','ssn','address','phone','gsm','email','passw','job_title','ismanager'))
staff.append(Staff('S7','D3','Jan Jacobsen','231265-4549','Vei 230 12, Longyearbyen, Svalbard','+47 92 09 77 00','+354 777 1337','jan.jacobsen@nanair.is','JanJac23!','Yfirmaður rekstrarsviðs',True))
staff.append(Staff('S8','D3','Jacob Yxa','190482-7479','Vei 224 3B, Longyearbyen, Svalbard','+47 92 09 77 01','+354 777 1338','jacob.yxa@nanair.is','JacYxa14$','Starfsmaður',False))
staff.append(Staff('S9','D3','Nanna Daema','250185-1239','Ivan Starostin st. 109, Barantsburg, Svalbard','+47 92 09 77 02','+354 777 1339','nanna.daema@nanair.is','NanDae12$','Starfsmaður',False))

facilities.append(Facility('F24','P26','Vei BnB herbergi 1',''))
facilities.append(Facility('F25','P26','Vei BnB herbergi 2',''))
facilities.append(Facility('F26','P26','Vei BnB herbergi 3',''))
facilities.append(Facility('F27','P26','Vei BnB herbergi 4',''))

facilities.append(Facility('F28','P27','Hótel Akúla herbergi 1',''))
facilities.append(Facility('F29','P27','Hótel Akúla herbergi 2',''))
facilities.append(Facility('F30','P27','Hótel Akúla herbergi 3',''))
facilities.append(Facility('F31','P27','Hótel Akúla herbergi 4',''))
facilities.append(Facility('F32','P27','Hótel Akúla herbergi 5',''))
facilities.append(Facility('F33','P27','Hótel Akúla herbergi 6',''))
facilities.append(Facility('F34','P27','Hótel Akúla herbergi 7',''))
facilities.append(Facility('F35','P27','Hótel Akúla herbergi 8',''))
facilities.append(Facility('F36','P27','Hótel Akúla herbergi 9',''))
facilities.append(Facility('F37','P27','Hótel Akúla herbergi 10',''))
facilities.append(Facility('F38','P27','Hótel Akúla herbergi 11',''))
facilities.append(Facility('F39','P27','Hótel Akúla herbergi 12',''))
facilities.append(Facility('F40','P27','Hótel Akúla herbergi 13',''))
facilities.append(Facility('F41','P27','Hótel Akúla herbergi 14',''))
facilities.append(Facility('F42','P27','Hótel Akúla herbergi 15',''))
facilities.append(Facility('F43','P27','Hótel Akúla herbergi 16',''))
facilities.append(Facility('F44','P27','Hótel Akúla herbergi 17',''))
facilities.append(Facility('F45','P27','Hótel Akúla herbergi 18',''))
facilities.append(Facility('F46','P27','Hótel Akúla herbergi 19',''))
facilities.append(Facility('F47','P27','Hótel Akúla herbergi 20',''))
facilities.append(Facility('F48','P27','Hótel Akúla herbergi 21',''))
facilities.append(Facility('F49','P27','Hótel Akúla herbergi 22',''))
facilities.append(Facility('F50','P27','Hótel Akúla herbergi 23',''))
facilities.append(Facility('F51','P27','Hótel Akúla herbergi 24',''))
facilities.append(Facility('F52','P27','Hótel Akúla herbergi 25',''))
facilities.append(Facility('F53','P27','Hótel Akúla herbergi 26',''))
facilities.append(Facility('F54','P27','Hótel Akúla herbergi 27',''))
facilities.append(Facility('F55','P27','Hótel Akúla herbergi 28',''))
facilities.append(Facility('F56','P27','Hótel Akúla herbergi 29',''))
facilities.append(Facility('F57','P27','Hótel Akúla herbergi 30',''))
facilities.append(Facility('F58','P27','Hótel Akúla herbergi 31',''))
facilities.append(Facility('F59','P27','Hótel Akúla herbergi 32',''))
facilities.append(Facility('F60','P27','Hótel Akúla herbergi 33',''))
facilities.append(Facility('F61','P27','Hótel Akúla herbergi 34',''))
facilities.append(Facility('F62','P27','Hótel Akúla herbergi 35',''))
facilities.append(Facility('F63','P27','Hótel Akúla herbergi 36',''))
facilities.append(Facility('F64','P27','Hótel Akúla herbergi 37',''))
facilities.append(Facility('F65','P27','Hótel Akúla herbergi 38',''))
facilities.append(Facility('F66','P27','Hótel Akúla herbergi 39',''))
facilities.append(Facility('F67','P27','Hótel Akúla herbergi 40',''))
facilities.append(Facility('F68','P27','Hótel Akúla herbergi 41',''))
facilities.append(Facility('F69','P27','Hótel Akúla herbergi 42',''))
facilities.append(Facility('F70','P27','Hótel Akúla herbergi 43',''))
facilities.append(Facility('F71','P27','Hótel Akúla herbergi 44',''))
facilities.append(Facility('F72','P27','Hótel Akúla herbergi 45',''))
facilities.append(Facility('F73','P27','Hótel Akúla herbergi 46',''))
facilities.append(Facility('F74','P27','Hótel Akúla herbergi 47',''))
facilities.append(Facility('F75','P27','Hótel Akúla herbergi 48',''))
facilities.append(Facility('F76','P27','Hótel Akúla herbergi 49',''))
facilities.append(Facility('F77','P27','Hótel Akúla herbergi 50',''))
facilities.append(Facility('F78','P27','Hótel Akúla herbergi 51',''))
facilities.append(Facility('F79','P27','Hótel Akúla herbergi 52',''))
facilities.append(Facility('F80','P27','Hótel Akúla herbergi 53',''))
facilities.append(Facility('F81','P27','Hótel Akúla herbergi 54',''))
facilities.append(Facility('F82','P27','Hótel Akúla herbergi 55',''))
facilities.append(Facility('F83','P27','Hótel Akúla herbergi 56',''))
facilities.append(Facility('F84','P27','Hótel Akúla herbergi 57',''))
facilities.append(Facility('F85','P27','Hótel Akúla herbergi 58',''))
facilities.append(Facility('F86','P27','Hótel Akúla herbergi 59',''))
facilities.append(Facility('F87','P27','Hótel Akúla herbergi 60',''))
facilities.append(Facility('F88','P27','Hótel Akúla herbergi 61',''))
facilities.append(Facility('F89','P27','Hótel Akúla herbergi 62',''))
facilities.append(Facility('F90','P27','Hótel Akúla herbergi 63',''))
facilities.append(Facility('F91','P27','Hótel Akúla herbergi 64',''))
facilities.append(Facility('F92','P27','Hótel Akúla herbergi 65',''))
facilities.append(Facility('F93','P27','Hótel Akúla herbergi 66',''))
facilities.append(Facility('F94','P27','Hótel Akúla herbergi 67',''))
facilities.append(Facility('F95','P27','Hótel Akúla herbergi 68',''))
facilities.append(Facility('F96','P27','Hótel Akúla herbergi 69',''))
facilities.append(Facility('F97','P27','Hótel Akúla herbergi 70',''))
facilities.append(Facility('F98','P27','Hótel Akúla herbergi 71',''))
facilities.append(Facility('F99','P27','Hótel Akúla herbergi 72',''))
facilities.append(Facility('F100','P27','Hótel Akúla herbergi 73',''))
facilities.append(Facility('F101','P27','Hótel Akúla herbergi 74',''))
facilities.append(Facility('F102','P27','Hótel Akúla herbergi 75',''))
facilities.append(Facility('F103','P27','Hótel Akúla herbergi 76',''))
facilities.append(Facility('F104','P27','Hótel Akúla herbergi 77',''))
facilities.append(Facility('F105','P27','Hótel Akúla herbergi 78',''))
facilities.append(Facility('F106','P27','Hótel Akúla herbergi 79',''))
facilities.append(Facility('F107','P27','Hótel Akúla herbergi 80',''))

facilities.append(Facility('F108','P27','Hótel Akúla Leik/æfingasalur og gufubað',''))
facilities.append(Facility('F109','P27','Hótel Akúla Móttaka',''))
facilities.append(Facility('F110','P27','Hótel Akúla Kjarnakljúfur',''))

# -------------------------- write to the actual files -------------------------

destination_storage.save_to_file(destinations)
property_storage.save_to_file(properties)
staff_storage.save_to_file(staff)
facility_storage.save_to_file(facilities)
contractor_storage.save_to_file(contractors)
