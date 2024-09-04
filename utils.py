import json


def read_json(json_path):
    with open(json_path) as f:
        return json.load(f)
