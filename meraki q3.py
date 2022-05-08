# Q.3 Python object ko json string mai convert karne ka program likho?
# Edit on Github

import json
python_obj = {"name": "David","class":"I","age": 6  }
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)