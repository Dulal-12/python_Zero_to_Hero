with open('sample.txt','r') as f:
    data = f.read()
    if 'Twinkle' in data:
        print("Twinkle in file")
    else:
        print('It is not in file')