import json
dict={"a":{"a":4,"b":3,"c":4}}

with open("nothing.json","w") as write:
    json.dump(dict,write)
    
with open("nothing.json.","r") as read:
    print (json.load(read))   