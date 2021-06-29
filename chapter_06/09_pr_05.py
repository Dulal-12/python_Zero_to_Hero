mark = int(input('Enter Your Marks : '))

if mark >= 90:
    grade = 'Ex'
elif mark >=80 : 
    grade = 'A'
elif mark >=70 : 
    grade = 'B'
elif mark >=60 : 
    grade = 'C'
elif mark >=50 : 
    grade = 'D'
else:
    grade = 'F'

print('Your grade is : ',grade)