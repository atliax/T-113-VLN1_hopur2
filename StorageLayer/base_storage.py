import json
import os

from Model import BaseModel

class BaseStorage:
    def __init__(self, filename, model_class : BaseModel):
        self.filename = filename
        self.model_class = model_class

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