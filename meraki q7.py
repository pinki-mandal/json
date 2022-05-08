# Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
dict1={"Text.txt":{"Name": "Abhishek","Designation": "CEO of navgurukul","Gender": "male","Age":"29"}}
print(json.dumps(dict1,indent=10))


