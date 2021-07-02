# Use open function to reaad the content of a file !
# f = open('sample.txt' , 'r')
f = open('sample.txt') # By default read
data = f.read()
# data = f.read(5) # Read the first 5 characters
print(data)
f.close()