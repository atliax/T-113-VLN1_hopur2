from UILayer.base_screen import BaseScreen
from UILayer import ui_consts

class FacilityScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)

    def render(self):
        self.clear_screen()

        print("Main Menu > Properties > Facilities")
        print(ui_consts.SEPERATOR)
        print("|")
        print("|	[A] Add a facility		[E] Edit a facility			[B] Go back")
        print("|	[R] Remove a facility		[S] Search for")
        print("|	[V] View details")
        print("|")
        print(ui_consts.SEPERATOR)

        cmd = input("Command: ").lower()

        # Add a facility
        if cmd == "a":
            new_facility = input("New facility name: ")
            new_description = input("New facility description: ")

        # Remove a facility
        if cmd == "r":
            remove = input("Remove facility that has the ID: ") # Klára þegar skjalakerfi er klárt
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command

                
        if cmd == "s":
                # Example gamer, Nuuk
                # Finnur allar línur tengdar gamer, nuuk
            search = input("Search for: ") # Sama search allstaðar nema á tickets

        # View details
        if cmd == "v":
            view = input("View the details of facility with the ID: ")
                # If ID does not exist in property list, raise error "No facility found with that ID!"
                # If ID does not exist, cancel command	
            print(f"Facility name: {new_facility}")
            print(f"Facility description: {new_description}")

        if cmd == "b":
            return ui_consts.BACK
