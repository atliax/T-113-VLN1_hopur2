class DestinationManager:
    def __init__(self) -> None:
        self.properties_by_destination = self.load_properties()

    def load_properties(self):
        """Loads from text file"""

    def get_properties(self, destination: str):
        """Return a list of properties for selected destination"""
        return self.properties_by_destination.get(destination, [])