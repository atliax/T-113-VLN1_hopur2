from StorageLayer.base_storage import BaseStorage

from Model import Staff

class StaffStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def staff_add(self, new_staff : Staff) -> None:
        current_staff = self.load_from_file()
        current_staff.append(new_staff)
        self.save_to_file(current_staff)

    def staff_remove(self, staffID : str) -> None:
        current_staff : list[Staff] = self.load_from_file()

        updated_staff = []
        for staff in current_staff:
            if staff.staffID != staffID:
                updated_staff.append(staff)

        self.save_to_file(updated_staff)
    
    def staff_edit(self, edited_staff : Staff) -> None:
        current_staff : list[Staff] = self.load_from_file()

        updated_staff = []
        for staff in current_staff:
            if staff.staffID == edited_staff.staffID:
                updated_staff.append(edited_staff)
            else:
                updated_staff.append(staff)

        self.save_to_file(updated_staff)

    def staff_get_all(self) -> list[Staff]:
        return self.load_from_file()

    def staff_get_by_ID(self, staffID : str) -> Staff:
        current_staff : list[Staff] = self.load_from_file()

        for staff in current_staff:
            if staff.staffID == staffID:
                return staff

    def staff_search(self, search_string : str) -> list[Staff]:
        return []
