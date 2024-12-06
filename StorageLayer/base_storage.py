import json

from Model import BaseModel

class BaseStorage:
    def __init__(self, filename, model_class : BaseModel):
        self.filename = filename
        self.model_class = model_class

    def load_from_file(self) -> list[BaseModel]:
        ret = []

        with open(self.filename, "r") as file:
            lines = file.readlines()

        for line in lines:
            line_json = json.loads(line)
            tmp_model = self.model_class(**line_json)
            if tmp_model is not None:
                ret.append(tmp_model)

        return ret

    def save_to_file(self, data : list[BaseModel]) -> None:
        with open(self.filename, "w") as file:
            for item in data:
                file.write(item.toJson()+"\n")
