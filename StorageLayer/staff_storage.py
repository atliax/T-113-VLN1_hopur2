from StorageLayer.base_storage import BaseStorage

from Model import Staff

class StaffStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def add_new_staff(self, new_staff : Staff) -> None:
        current_staff = self.load_from_file()
        current_staff.append(new_staff)
        self.save_to_file(current_staff)

    def remove_staff(self, staffID: str) -> None:
        current_staff: list[Staff] = self.load_from_file()

        updated_staff = []
        for staff in current_staff:
            if staff.staffID != staffID:
                updated_staff.append(staff)

        self.save_to_file(updated_staff)
    
    def edit_staff(self, edit_staff):
        self.save_to_file(edit_staff)
