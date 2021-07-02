with open('string.txt') as f:
    data = f.read()

data = data.replace("Donkey" , "######")
with open('string.txt' , 'wt') as f:
    f.write(data)

