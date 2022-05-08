# import json
# city=("pinki","sita","sarita","husna")
# print(json.dumps(city,separators=("|",".")))

import os
import json

filepath = os.path.join(os.path.expanduser("~"), "Desktop", "data.json") 
with open(filepath) as file:
    data = json.load(file)
    print(data)

