from StorageLayer.base_storage import BaseStorage

from Model import Staff

class StaffStorage(BaseStorage):
    def __init__(self, filename, model_class):
        super().__init__(filename, model_class)

    def add_new_staff(self,new_staff : Staff):
        current_staff = self.load_from_file()
        current_staff.append(new_staff)
        self.save_to_file(current_staff)

    def remove_staff(self, remove_id: str):
        current_staff: list[Staff] = self.load_from_file()
        new_staff_list = []
        for staff in current_staff:
            if staff.staffID != remove_id:
                new_staff_list.append(staff)
        self.save_to_file(new_staff_list)
    
    def edit_staff(self, edit_staff):
        self.save_to_file(edit_staff)
        
        

    
