myDict = {
    'name' : 'Dulal'
}

# print(list(myDict.keys()))
# print(list(myDict.values()))
# print(list(myDict.items()))

print(myDict.get("names" , 'Akash'))
print(myDict['names']) #throw a error if keys not found

updateDict = {
     'age' : 22,
     'bestFriend' : 'Ammu',
      'name': 'Musa'
}
myDict.update(updateDict) # Update the dictionary by adding key-value pairs
print(myDict)