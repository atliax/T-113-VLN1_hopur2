

class Amenity:
    def __init__(self,id: str ,schedule: str , description: str, condition: str):
        self.id = id
        self.schedule = schedule
        self.description = description
        self.condition = condition

    def __str__(self):
        return f"{self.id}: {self.description}"
#TODO klára fallið







