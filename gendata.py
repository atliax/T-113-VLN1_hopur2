from StorageLayer.storage_manager import StorageManager

from Model import *

facility_storage = StorageManager("data/facilities.json", Facility)
contractor_storage = StorageManager("data/contractors.json", Contractor)
destination_storage = StorageManager("data/destinations.json", Destination)
property_storage = StorageManager("data/properties.json", Property)
staff_storage = StorageManager("data/staff.json", Staff)
ticket_storage = StorageManager("data/tickets.json", Ticket)

destinations = []
properties = []
staff = []
facilities = []
contractors = []
tickets = []

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

facilities.append(Facility('F1','P1','iGloo-Ville móttaka',''))

facilities.append(Facility('F2','P2','Snjóhús 1',''))
facilities.append(Facility('F3','P3','Snjóhús 2',''))
facilities.append(Facility('F4','P4','Snjóhús 3',''))
facilities.append(Facility('F5','P5','Snjóhús 4',''))
facilities.append(Facility('F6','P6','Snjóhús 5',''))
facilities.append(Facility('F7','P7','Snjóhús 6',''))
facilities.append(Facility('F8','P8','Snjóhús 7',''))
facilities.append(Facility('F9','P9','Snjóhús 8',''))
facilities.append(Facility('F10','P10','Snjóhús 9',''))
facilities.append(Facility('F11','P11','Snjóhús 10',''))

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

facilities.append(Facility('F12','P16','Moldarhús 1',''))
facilities.append(Facility('F13','P17','Moldarhús 2',''))
facilities.append(Facility('F14','P18','Moldarhús 3',''))
facilities.append(Facility('F15','P19','Moldarhús 4',''))
facilities.append(Facility('F16','P20','Moldarhús 5',''))
facilities.append(Facility('F17','P21','Moldarhús 6',''))
facilities.append(Facility('F18','P22','Moldarhús 7',''))
facilities.append(Facility('F19','P23','Moldarhús 8',''))
facilities.append(Facility('F20','P24','Moldarhús 9',''))
facilities.append(Facility('F21','P25','Moldarhús 10',''))
facilities.append(Facility('F22','P12','hús 1',''))
facilities.append(Facility('F23','P13','hús 2',''))
facilities.append(Facility('F24','P14','hús 3',''))

facilities.append(Facility('F25','P15','Aðalbygging',''))

# -------------------------- Longyearbyen, Svalbarði: --------------------------

destinations.append(Destination('D3','S7','Svalbarði','Longyearbyen','PHONE','24/7'))

properties.append(Property('P26','D3','Vei BnB','Vei 217, Longyearbyen, Svalbarði', 150, 4, 'Einbýlishús'))
properties.append(Property('P27','D3','Hótel Akúla','Longyearbyen Harbor 1, Svalbarði',5000,80,'Kafbátur'))

staff.append(Staff('S7','D3','Jan Jacobsen','231265-4549','Vei 230 12, Longyearbyen, Svalbard','+47 92 09 77 00','+354 777 1337','jan.jacobsen@nanair.is','JanJac23!','Yfirmaður rekstrarsviðs',True))
staff.append(Staff('S8','D3','Jacob Yxa','190482-7479','Vei 224 3B, Longyearbyen, Svalbard','+47 92 09 77 01','+354 777 1338','jacob.yxa@nanair.is','JacYxa14$','Starfsmaður',False))
staff.append(Staff('S9','D3','Nanna Daema','250185-1239','Ivan Starostin st. 109, Barantsburg, Svalbard','+47 92 09 77 02','+354 777 1339','nanna.daema@nanair.is','NanDae12$','Starfsmaður',False))

facilities.append(Facility('F26','P26','herbergi 1',''))
facilities.append(Facility('F27','P26','herbergi 2',''))
facilities.append(Facility('F28','P26','herbergi 3',''))
facilities.append(Facility('F29','P26','herbergi 4',''))

facilities.append(Facility('F30','P27','herbergi 1',''))
facilities.append(Facility('F31','P27','herbergi 2',''))
facilities.append(Facility('F32','P27','herbergi 3',''))
facilities.append(Facility('F33','P27','herbergi 4',''))
facilities.append(Facility('F34','P27','herbergi 5',''))
facilities.append(Facility('F35','P27','herbergi 6',''))
facilities.append(Facility('F36','P27','herbergi 7',''))
facilities.append(Facility('F37','P27','herbergi 8',''))
facilities.append(Facility('F38','P27','herbergi 9',''))
facilities.append(Facility('F39','P27','herbergi 10',''))
facilities.append(Facility('F40','P27','herbergi 11',''))
facilities.append(Facility('F41','P27','herbergi 12',''))
facilities.append(Facility('F42','P27','herbergi 13',''))
facilities.append(Facility('F43','P27','herbergi 14',''))
facilities.append(Facility('F44','P27','herbergi 15',''))
facilities.append(Facility('F45','P27','herbergi 16',''))
facilities.append(Facility('F46','P27','herbergi 17',''))
facilities.append(Facility('F47','P27','herbergi 18',''))
facilities.append(Facility('F48','P27','herbergi 19',''))
facilities.append(Facility('F49','P27','herbergi 20',''))
facilities.append(Facility('F50','P27','herbergi 21',''))
facilities.append(Facility('F51','P27','herbergi 22',''))
facilities.append(Facility('F52','P27','herbergi 23',''))
facilities.append(Facility('F53','P27','herbergi 24',''))
facilities.append(Facility('F54','P27','herbergi 25',''))
facilities.append(Facility('F55','P27','herbergi 26',''))
facilities.append(Facility('F56','P27','herbergi 27',''))
facilities.append(Facility('F57','P27','herbergi 28',''))
facilities.append(Facility('F58','P27','herbergi 29',''))
facilities.append(Facility('F59','P27','herbergi 30',''))
facilities.append(Facility('F60','P27','herbergi 31',''))
facilities.append(Facility('F61','P27','herbergi 32',''))
facilities.append(Facility('F62','P27','herbergi 33',''))
facilities.append(Facility('F63','P27','herbergi 34',''))
facilities.append(Facility('F64','P27','herbergi 35',''))
facilities.append(Facility('F65','P27','herbergi 36',''))
facilities.append(Facility('F66','P27','herbergi 37',''))
facilities.append(Facility('F67','P27','herbergi 38',''))
facilities.append(Facility('F68','P27','herbergi 39',''))
facilities.append(Facility('F69','P27','herbergi 40',''))
facilities.append(Facility('F70','P27','herbergi 41',''))
facilities.append(Facility('F71','P27','herbergi 42',''))
facilities.append(Facility('F72','P27','herbergi 43',''))
facilities.append(Facility('F73','P27','herbergi 44',''))
facilities.append(Facility('F74','P27','herbergi 45',''))
facilities.append(Facility('F75','P27','herbergi 46',''))
facilities.append(Facility('F76','P27','herbergi 47',''))
facilities.append(Facility('F77','P27','herbergi 48',''))
facilities.append(Facility('F78','P27','herbergi 49',''))
facilities.append(Facility('F79','P27','herbergi 50',''))
facilities.append(Facility('F80','P27','herbergi 51',''))
facilities.append(Facility('F81','P27','herbergi 52',''))
facilities.append(Facility('F82','P27','herbergi 53',''))
facilities.append(Facility('F83','P27','herbergi 54',''))
facilities.append(Facility('F84','P27','herbergi 55',''))
facilities.append(Facility('F85','P27','herbergi 56',''))
facilities.append(Facility('F86','P27','herbergi 57',''))
facilities.append(Facility('F87','P27','herbergi 58',''))
facilities.append(Facility('F88','P27','herbergi 59',''))
facilities.append(Facility('F89','P27','herbergi 60',''))
facilities.append(Facility('F90','P27','herbergi 61',''))
facilities.append(Facility('F91','P27','herbergi 62',''))
facilities.append(Facility('F92','P27','herbergi 63',''))
facilities.append(Facility('F93','P27','herbergi 64',''))
facilities.append(Facility('F94','P27','herbergi 65',''))
facilities.append(Facility('F95','P27','herbergi 66',''))
facilities.append(Facility('F96','P27','herbergi 67',''))
facilities.append(Facility('F97','P27','herbergi 68',''))
facilities.append(Facility('F98','P27','herbergi 69',''))
facilities.append(Facility('F99','P27','herbergi 70',''))
facilities.append(Facility('F100','P27','herbergi 71',''))
facilities.append(Facility('F101','P27','herbergi 72',''))
facilities.append(Facility('F102','P27','herbergi 73',''))
facilities.append(Facility('F103','P27','herbergi 74',''))
facilities.append(Facility('F104','P27','herbergi 75',''))
facilities.append(Facility('F105','P27','herbergi 76',''))
facilities.append(Facility('F106','P27','herbergi 77',''))
facilities.append(Facility('F107','P27','herbergi 78',''))
facilities.append(Facility('F108','P27','herbergi 79',''))
facilities.append(Facility('F109','P27','herbergi 80',''))

facilities.append(Facility('F110','P27','Leik/æfingasalur og gufubað',''))
facilities.append(Facility('F111','P27','Móttaka',''))
facilities.append(Facility('F112','P27','Kjarnakljúfur',''))

tickets.append(Ticket('T1','F2','P2','High','Ticket title','Ticket description','Closed',False,0,'10-12-2024','13-12-2024',None,None,0,None,None,None,0))
tickets.append(Ticket('T2','F2','P2','Low','Ticket title','Ticket description','Open',False,0,'11-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T3','F2','P2','High','Ticket title','Ticket description','Done',False,0,'12-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T4','F2','P2','High','Ticket title','Ticket description','Done',False,0,'13-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T5','F2','P2','Medium','Ticket title','Ticket description','Open',False,0,'14-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T6','F2','P2','Medium','Ticket title','Ticket description','Open',False,0,'15-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T7','F2','P2','High','Ticket title','Ticket description','Open',False,0,'16-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T8','F2','P2','High','Ticket title','Ticket description','Open',False,0,'17-12-2024',None,None,None,0,None,None,None,0))

tickets.append(Ticket('T9','F12','P16','High','Ticket title','Ticket description','Closed',False,0,'10-12-2024','13-12-2024',None,None,0,None,None,None,0))
tickets.append(Ticket('T10','F12','P16','Low','Ticket title','Ticket description','Open',False,0,'11-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T11','F12','P16','High','Ticket title','Ticket description','Done',False,0,'12-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T12','F12','P16','High','Ticket title','Ticket description','Done',False,0,'13-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T13','F12','P16','Medium','Ticket title','Ticket description','Open',False,0,'14-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T14','F12','P16','Medium','Ticket title','Ticket description','Open',False,0,'15-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T15','F12','P16','High','Ticket title','Ticket description','Open',False,0,'16-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T16','F12','P16','High','Ticket title','Ticket description','Open',False,0,'17-12-2024',None,None,None,0,None,None,None,0))

tickets.append(Ticket('T17','F30','P27','High','Ticket title','Ticket description','Closed',False,0,'10-12-2024','13-12-2024',None,None,0,None,None,None,0))
tickets.append(Ticket('T18','F30','P27','Low','Ticket title','Ticket description','Open',False,0,'11-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T19','F30','P27','High','Ticket title','Ticket description','Done',False,0,'12-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T20','F30','P27','High','Ticket title','Ticket description','Done',False,0,'13-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T21','F30','P27','Medium','Ticket title','Ticket description','Open',False,0,'14-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T22','F30','P27','Medium','Ticket title','Ticket description','Open',False,0,'15-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T23','F30','P27','High','Ticket title','Ticket description','Open',False,0,'16-12-2024',None,None,None,0,None,None,None,0))
tickets.append(Ticket('T24','F30','P27','High','Ticket title','Ticket description','Open',False,0,'17-12-2024',None,None,None,0,None,None,None,0))

contractors.append(Contractor('C1','D1',0.0,'Píparaþjónusta Sigurjóns','Sigurjón Þórðarson','+354 777-8888', 'Húsavegur 1, Bær', '10:30-15:30 virka daga','Pípari'))
contractors.append(Contractor('C2','D2',0.0,'Guðmundur Sigfinnsson','','+354 555-1212', 'Gata 14, Borg', '24/7','Þúsundþjalasmiður'))
contractors.append(Contractor('C3','D3',0.0,'Actavis','','+354 525-1515', 'Götugata 19, Borgarbær', '9-17 um helgar','Lyfjasala'))

# -------------------------- write to the actual files -------------------------

destination_storage.save_to_file(destinations)
property_storage.save_to_file(properties)
staff_storage.save_to_file(staff)
facility_storage.save_to_file(facilities)
contractor_storage.save_to_file(contractors)
ticket_storage.save_to_file(tickets)
