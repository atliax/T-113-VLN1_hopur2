import json

from Model import BaseModel

class BaseStorage:
    def __init__(self, filename):
        self.filename = filename

    def load_from_file(self, model_class : BaseModel) -> list[BaseModel]:
        ret = []

        with open(self.filename, "r") as file:
            lines = file.readlines()

        for line in lines:
            line_json = json.loads(line)
            tmp_model = model_class(**line_json)
            if tmp_model is not None:
                ret.append(tmp_model)

        return ret

    def save_to_file(self, data : list[BaseModel]) -> None:
        pass
