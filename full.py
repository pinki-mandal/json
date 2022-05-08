import json
import os
import re
b=[]
file=os.path.exists("pinki.json")
if(file==False):
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
                list1=["character","sername","gender","passward"]
                list2=[character,surname,gender,password]
                list=[]
                dict={}
                dict1={}
                i=0
                while i<len(list1):
                    dict[list1[i]]=list2[i]
                    i=i+1
                list.append(dict)
                dict1[password]=list      
                with open ("pinki.json","a")as p:
                   json.dump(dict1,p,indent=4)
elif file==True:
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
                list1=["character","sername","gender","passward"]
                list2=[character,surname,gender,password]
                list7=[]
                dict={}
                dict1={}
                i=0
                while i<len(list1):
                    dict[list1[i]]=list2[i]
                    i=i+1
                list7.append(dict)
                dict1[password]=list7    
                with open ("pinki.json","a")as p:
                   json.dump(dict1,p,indent=4)
    
