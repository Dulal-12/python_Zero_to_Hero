letter = ''' Dear |<Name>|
            You are selected.
            
Thanks and Regards,
Md.Dulal Miah
Date : |<Date>|
'''
name = input('Enter your name\n')
date = input('Enter your date\n')
letter = letter.replace("|<Name>|" , name)
letter = letter.replace("|<Date>|" , date)
print(letter)