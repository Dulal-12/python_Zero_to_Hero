# Creating a empty set
a = set()
print(a)
a.add(5)
a.add(5)
a.add(6)
print(a)
# Important : You can not add list and dict in set
a.add((345,67)) #You can add tuple
print(a)

print(len(a)) # Length of the set

a.remove(5) # Removes the value of 5 from a set
a.remove(15) # Throw a error
a.pop() # Random value remove
print(a)