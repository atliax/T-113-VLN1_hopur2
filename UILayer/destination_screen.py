import math

from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Destination

class DestinationScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)
        self.current_page = -1

    def run(self):
        self.clear_screen()

        print("Main Menu > Destinations")

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        print("|")
        print(ui_consts.SEPERATOR)

        destinations = self.ui.logic_api.destination_get_all()

        destination_table = PrettyTable()
        destination_table.field_names = ["ID","managerID","Destination","Airport", "Phone", "Opening"]

        for destination in destinations:
            destination_table.add_row([destination.destinationID, destination.managerID, destination.country, destination.airport, destination.phone, destination.opening_hours])

        destination_table._min_table_width = ui_consts.TABLE_WIDTH

        total_pages = math.ceil(len(destinations) / 10)

        if self.current_page < 0:
            self.current_page = 0

        if self.current_page > (total_pages - 1):
            self.current_page = (total_pages - 1)

        print(f"|  Destination list (Page {self.current_page+1}/{total_pages}):")
        print("|  [N] Next page    [P] Previous page")
        print(destination_table.get_string(start=self.current_page*10, end=(self.current_page+1)*10))

        print("")
        cmd = input("Command: ").lower()

        if cmd == "n":
            self.current_page += 1

        if cmd == "p":
            self.current_page -= 1

        # Add a destination
        if cmd == "a":
            destination_attributes = ["managerID", "country", "airport", "phone", "opening_hours"]
            new_destination = []
            for attribute in destination_attributes:
                new_value = input(f"New {attribute}: ")
                new_destination.append(new_value)
            tmp = Destination(None,new_destination[0],new_destination[1],new_destination[2],new_destination[3],new_destination[4])
            self.ui.logic_api.destination_add(tmp)

        # Edit destination
        if cmd == "e":
            # 
            destination_edit = None
            destination_attributes = ["managerID", "country", "airport", "phone", "opening_hours"]
            pick_destination = input("Type in the id of the destination you want to edit: ").upper()
            for destination in destinations:
                if destination.destinationID == pick_destination:
                    destination_edit = destination
            if destination_edit is None:
                print("Destination not found")
                input("Press enter to continue")
            else:
                for attribute in destination_attributes:
                    current_value = getattr(destination_edit, attribute)
                    new_value = input(f"New {attribute} (current: {current_value}): ").strip()
                    if new_value:
                        setattr(destination_edit, attribute, new_value)
                self.ui.logic_api.destination_edit(destination_edit)

        if cmd == "b":
            return ui_consts.CMD_BACK

        return self
