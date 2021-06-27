myDict = {
     'name':'Mohammad Dulal Miah',
     'address':'Gazipur',
     'marks':[1,2,3,4],
     'anotherDict':{'Laboni' : 'Sorifa'}
}

# print(list(myDict.keys()))
# print(list(myDict.values()))
# print(list(myDict.items()))
print(myDict.get("names" , 'Akash'))
updateDict = {
     'age' : 22,
     'bestFriend' : 'Ammu'
}
myDict.update(updateDict) # Update the dictionary by adding key-value pairs
print(myDict)