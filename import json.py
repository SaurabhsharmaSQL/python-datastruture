import json

myDict = { "records" :   [
{
    "name": "Vijay",
    "age": 44,
    "gender" : "m",
    "cars": ["Maruti"]
},
{
    "name": "Vicky",
    "age": 25,
    "gender" : "m",
    "cars": ["BMW"]
},
{
    "name": "Preeti",
    "age": 22,
    "gender" : "f",
    "cars": ["Honda", "Renault"]
},
{
    "name": "Saurabh",
    "age": 20,
    "gender" : "m",
    "cars": ["Mercedees"]
},

]}

print(myDict["records"])
for records in myDict["records"]:
    print("Name:", records["name"], "Age:" , records["age"])
    for car in records["cars"]:
        if car in ("Mercedees", "BMW") or len(records["cars"])>1:
         if records["gender"] =="m":      
             print('\t Lucky fellow he got ' + car + "Car")
         elif records["gender"] =="f":
             print('\t Lucky fellow she got '+ car + "car")
         else :
             print('\t Luckynfellow s\he got '+ car + "car")
         #if car in ('Maruti'):
            #print('\t Poor fellow')