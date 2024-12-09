from StorageLayer.base_storage import BaseStorage

from Model import Staff

class StaffStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)

    def add_new_staff(self,new_staff : Staff):
        current_staff = self.load_from_file()
        current_staff.append(new_staff)
        self.save_to_file(current_staff)

    
