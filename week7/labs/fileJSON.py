# a file that writes a dictionary to a JSON file

import json

def storage(dictTest):
    with open(filename, "wt") as f:
        json.dump(dictTest, f)

filename = "first.json"

dict = {
        "name": "iafeta",
        "dob": "11/11/1922",
        "weight": 235,
    }

storage(dict)