from prettytable import PrettyTable

from UILayer.base_screen import BaseScreen

from UILayer import ui_consts

from Model import Destination

class DestinationScreen(BaseScreen):
    def __init__(self, ui) -> None:
        super().__init__(ui)

    def run(self):
        self.clear_screen()

        print("Main menu > Destinations")

        destinations = self.ui.logic_api.destination_get_all()

        destination_table = PrettyTable()
        destination_table.field_names = ["ID","managerID","Destination","Airport", "Phone", "Opening"]

        for destination in destinations:
            destination_table.add_row([destination.destinationID, destination.managerID, destination.country, destination.airport, destination.phone, destination.opening_hours])

        print(destination_table)

        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a destination		[E] Edit a destination			[B] Go back")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

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
