# Tumhare pass four employes ki details hai list mai:-
import json
keys=["name","degignation","age","salary"]
a=["neelam","programmer","24","2400"]
emp1={}
emp2={}
emp3={}
emp4={}
dict={}
for i in range(len(keys)):
    emp1[keys[i]]=a[i]
    dict["employee1"]=emp1
    b=["komal","trainer","24","20000"]
    for i in range(len(keys)):
        emp2[keys[i]]=b[i]
        dict["employee2"]=emp2
        c=["anuradha","hr","25","4000"]
        for i in range(len(keys)):
            emp3[keys[i]]=c[i]
            dict["employees3"]=emp3
            d=["abhishek","manager","29","63000"]
            for i in range(len(keys)):
                emp4[keys[i]]=d[i]
                dict["employees4"]=emp4

out_file = open("employees.json", "w")
json.dump(dict, out_file, indent = 6)
out_file.close()                
           
