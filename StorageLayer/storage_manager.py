import json
import os

from Model import BaseModel

from Exceptions import FileWriteError, FileReadError

class StorageManager:
    def __init__(self, filename : str, model_class : BaseModel) -> None:
        self.filename = filename
        self.model_class = model_class

    def get_highest_ID(self) -> str:
        items = self.load_from_file()
        if items:
            return items[len(items)-1].ID
        else:
            return "X0"

    def add(self, new_item) -> None:
        """Takes in an instance of a BaseModel child class and adds it to the system."""
        current_items = self.load_from_file()
        current_items.append(new_item)
        self.save_to_file(current_items)

    def remove(self, ID : str) -> None:
        """Takes in an ID for a BaseModel child class and removes the corresponding item from the system."""
        current_items = self.load_from_file()

        updated_items = []
        for item in current_items:
            if item.ID == ID:
                item.deleted = True
            updated_items.append(item)

        self.save_to_file(updated_items)

    def edit(self, edited_item) -> None:
        """Takes in an instance of a BaseModel child class and replaces the corresponding item (with a matching .ID) in the system."""
        current_items = self.load_from_file()

        updated_items = []
        for item in current_items:
            if item.ID == edited_item.ID:
                updated_items.append(edited_item)
            else:
                updated_items.append(item)

        self.save_to_file(updated_items)

    def get_all(self) -> list[BaseModel]:
        """Returns a list of all the instances of a BaseModel child class that exist in the system."""
        all_items = self.load_from_file()
        existing_items = []
        for item in all_items:
            if not item.deleted:
                existing_items.append(item)
        return existing_items

    def get_by_ID(self, ID : str) -> BaseModel:
        """Takes in an ID and returns an instance of a BaseModel child class that matches that ID if it exists."""
        current_items = self.load_from_file()
        for item in current_items:
            if item.ID == ID and not item.deleted:
                return item

    def load_from_file(self) -> list[BaseModel]:
        """Loads the data file from self.filename and parses each line from it as a separate JSON string, creating an instance of the corresponding BaseModel class for that data file."""
        ret = []

        try:
            # read all the lines from the file
            with open(self.filename, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            # return empty list if the file does not exist
            return []
        except IOError as e:
            raise FileReadError(f"Error reading file '{self.filename}': {e}")

        # go through the lines in the file
        for line in lines:
            # parse the line as json
            try:
                line_json = json.loads(line)
            except json.decoder.JSONDecodeError:
                raise FileReadError(f"Malformed JSON in data file '{self.filename}'.")

            # construct an instance of the appropriate class
            try:
                tmp_model = self.model_class(**line_json)
            except TypeError:
                raise FileReadError(f"JSON data structure in '{self.filename}' didn't match model class.")

            # add the model to the list if it was valid
            if tmp_model is not None:
                ret.append(tmp_model)

        # return all the model instances found in the file
        return ret

    def save_to_file(self, data : list[BaseModel]) -> None:
        """Takes in a list of BaseModel child classes and writes each one to a separate line in self.filename as a JSON string."""
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
            try:
                os.remove(self.filename)
            except FileNotFoundError:
                # original file didn't exist, but no error is needed since it's about to be overwritten
                pass
            os.rename(self.filename+".tmp", self.filename)
        else:
            raise FileWriteError(f"Number of bytes written to '{self.filename}.tmp' does not match expected value.")
