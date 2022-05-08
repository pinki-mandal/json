# Json string ko check karo ki bo complex object contain karti hai ya nahi?

import json
dict1={"a":3,"b":4,"h":7+7j}
for i in dict1:
    if type(dict1[i])==complex:
        print("complex h ")
    else:
        print("complex nahi h ") 


           
        
