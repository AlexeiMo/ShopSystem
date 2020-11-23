import os
import json


class JsonUtils(object):

    def read_json(self, file) -> dict:
        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(json_file) as f:
            json_obj = json.load(f)
        return json_obj
