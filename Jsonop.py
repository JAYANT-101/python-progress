import json

data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"]
}

json_string = json.dumps(data, indent=4)  # indent for pretty-printing
print(json_string)

import json

json_string = '{"name": "Charlie", "age": 40, "occupation": "Engineer"}'
python_dict = json.loads(json_string)
print(python_dict["name"])