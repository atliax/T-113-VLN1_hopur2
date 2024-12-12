import json
import os

from Model import BaseModel

class StorageManager:
    def __init__(self, filename : str, model_class : BaseModel) -> None:
        self.filename = filename
        self.model_class = model_class

    def add(self, new_item) -> None:
        current_items = self.load_from_file()
        current_items.append(new_item)
        self.save_to_file(current_items)

    def remove(self, ID : str) -> None:
        current_items = self.load_from_file()

        updated_items = []
        for item in current_items:
            if item.ID != ID:
                updated_items.append(item)

        self.save_to_file(updated_items)

    def edit(self, edited_item) -> None:
        current_items = self.load_from_file()

        updated_items = []
        for item in current_items:
            if item.ID == edited_item.ID:
                updated_items.append(edited_item)
            else:
                updated_items.append(item)

        self.save_to_file(updated_items)

    def get_all(self) -> list[BaseModel]:
        return self.load_from_file()

    def get_by_ID(self, ID : str) -> BaseModel:
        current_items = self.load_from_file()
        for item in current_items:
            if item.ID == ID:
                return item
            
    #def search(self, search_string : str) -> list[BaseModel]:
    #    current_items = self.load_from_file()
    #    filtered_items = []
    #    for item in current_items:
    #        for attribute_value in list(item.__dict__.values()):
    #            if search_string.lower() in str(attribute_value).lower():
    #                filtered_items.append(item)
    #                break
    #    return filtered_items

    def load_from_file(self) -> list[BaseModel]:
        ret = []

        # read all the lines from the file
        with open(self.filename, "r") as file:
            lines = file.readlines()

        # go through the lines in the file
        for line in lines:
            # parse the line as json
            line_json = json.loads(line)

            # construct an instance of the appropriate class
            tmp_model = self.model_class(**line_json)

            # add it to the list if it is valid
            if tmp_model is not None:
                ret.append(tmp_model)

        # return all the model instances found in the file
        return ret

    def save_to_file(self, data : list[BaseModel]) -> None:
        # create a buffer with the new contents for the file
        new_file_contents = ""
        for item in data:
            new_file_contents += item.toJson() + "\n"

        # write the new contents to a temporary file
        bytes_written = 0
        with open(self.filename+".tmp", "w") as file:
            bytes_written = file.write(new_file_contents)

        # check if the file was written successfully
        if bytes_written == len(new_file_contents):
            # no error, swap with the temporary file
            os.remove(self.filename)
            os.rename(self.filename+".tmp", self.filename)
        else:
            # error has occurred writing to the file
            # TODO: Throw some error up to the UI layer?
            pass