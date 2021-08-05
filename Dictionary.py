# Dictionary: Key-value pairs, unordered, mutable
mudict = {
    "tester": "completed",
    "New": "Done",
    "Fire": "Power"
}

print(mudict)


mydict = dict(name="Hamzah", age=22, city="World")
print(mydict)

# Converting Dictionary to List
newlist = list(mydict.values())
print(newlist)

# Accessing keys
value = mydict["name"]
print(value)

# adding new item to dictionary
mydict["email"] = "hamzah@hotmail.com"
print(mydict)

# Delete dictionary item
# del mydict["name"]
# print(mydict)


# if statements for dictionary
if "name" in mydict:
    print(mydict["name"])


# Run code without it breaking your whole program
try:
    print(mydict["namee"])
except:
    print("error")


# loops through all items
for key in mydict.items():
    print(key)

# copy dictionary without it affecting the original
mydict_cpy = mydict.copy()
print(mydict)

mydict_cpy["email"] = "helrjerel"
print(mydict)
print(mydict_cpy)


dict1 = {
    1: 50,
    2: 100,
    3: 150,
    "name": "adam"
}

# join and update 2 dictionary together
dict2 = dict(name="hamzah", tester="New")

dict1.update(dict2)
print(dict1)


dict_num = {
    1: 50,
    2: 100,
    3: 150,
    "name": "adam"
}


value = dict_num[1]
print(value)


samytuple= (8, 7)
newdict = {samytuple: 15}

print(newdict)