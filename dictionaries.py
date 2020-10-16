#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "Year": 1984
}
print(thisdict)

#accessing items 
x=thisdict["model"]
print(x)

#another method of accessing items
x = thisdict.get("brand")
print(x)

#changing item values
thisdict["Year"]=1190
print(thisdict)

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

#Loop through both keys and values, by using the items() function
for x,y in thisdict.items():
    print(x,y)

#adding items in list
thisdict["colour"]="red"
print(thisdict)

#remove items from list
thisdict.pop("model")
print(thisdict)

#popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

#del keyword removes the item with the specified key name
del thisdict["brand"]
print(thisdict)

#copy of a dictionary with the copy() method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() method
mydict = dict(thisdict)
print(mydict)

#Create a dictionary that contain three dictionaries
myfamily = {
    "child1":{
        "name":"Harshil",
        "year":1998
    },
    "child2":{
        "name":"Ansh",
        "year":1111
    },
    "child3":{
        "name":"Linus",
        "year":1987
    }
}
print(myfamily)

#Create three dictionaries, than create one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#dict() constructor to make a new dictionary
thisdict = dict(brand="Ford", model="Mustang", year=1998)
print(thisdict)