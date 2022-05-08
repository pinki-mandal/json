# Q.1 Json data ko python object main convert karne ka program likho?.

import json
data = {
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
with open( "data_file.json" , "w" ) as write:
    json.dump( data , write )
    
with open("data_file.json", "r") as read_content:
    print(json.load(read_content))    