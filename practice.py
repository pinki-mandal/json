# import json
# a={"apple":4,"banana":3}
# k=json.dumps(a)
# print(k)


# json.loads() takes in a string and returns a json object.
# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])





# json.dumps() takes in a json object and returns a string.
# import json
# a = {"lalalala": 3}
# myString = json.dumps(a)
# print (myString)


# import json 
     
# # Data to be written 
# dictionary ={ 
#   "id": "04", 
#   "name": "sunil", 
#   "department": "HR"
# } 
     
# # Serializing json  
# json_object = json.dumps(dictionary, indent = 4) 
# print(json_object)




# import json
   
# # Data to be written
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
   
# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)
    
# ret= open("sample.json","r").read()
# deta = json.loads(ret)




n=int(input("enter the numer"))
if n%2==0 and (n>2 and n<5):
    print("not weird")  
elif n%2==0 and (n>6 and n<20):
    print("weird") 
elif n%2==0 and (n>20):
    print("not weird")    
elif n%2!=0:
    print("weird")    
else:
    print("nothing")
    