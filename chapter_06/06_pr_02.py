txt = input('Enter The Text : ')
spam  = False

if('make a lot of money' in txt):
    spam = True
elif('buy now' in txt):
    spam = True
elif('click this' in txt):
    spam = True
elif('subscribe this' in txt):
    spam = True
else:
    spam = False
    
if(spam):
    print('This txt is spam')
else:
    print('This txt is not spam')