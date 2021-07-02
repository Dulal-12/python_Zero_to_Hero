f = open('sample.txt') # By default read
data = f.readline()
print(data , end="")

data = f.readline()
print(data)
f.close()