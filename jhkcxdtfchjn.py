import json
import os
import re
if os.path.exists("my.json"):
    print("already exists")
    number=int(input("if you want sign in"))
    if number==1:
        print("sign in")
        character=input("enter the first name:-")
        if character>="a to z":
            surname=input("enter the surname:-")
        if surname>="a to z":
            gender=input("enter the gender")
        if gender=="female":
            password=input("enter the password:-")
            if not(re.search("[a-z A-Z]",password,)  and re.search('[0-9]',password) and re.search('[@#$]',password)):
                print("invalid password")
            else:
                com_password=input("comfirm your password")
                print("login successfully")
            login={"firsname":character,"surname":surname,"gender":gender,"password":password}                  
            out_file = open("login.json", "w")
            json.dump(login, out_file, indent = 4)
            out_file.close()
    else:
        print("nothing")
else:
    os.mkdir("my.json")    