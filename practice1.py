import json
dict={"a":3,"f":6,"t":3}


out_file = open("pinki.json", "w")
json.dump(dict, out_file, indent = 6)
out_file.close()