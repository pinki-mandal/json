dict1={"shopping_list":{ "chaco":15,"Biscuits":50,"Diary_milk":30,"ice_cream":20,} }
s=input("enter the key ")
num=int(input("enter the number"))
add=0
dict2={}
dic={}
for i in dict1:
    for j in dict1[i]:
        print(dict1[i][s])
        if s in j:
            add=dict1[i][s]+num
        dic.update({dict1[s]:add})
        
        
print(dic)
        