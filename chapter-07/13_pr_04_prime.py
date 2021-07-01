num = int(input('Enter the number : '))

prime = False

for i in range(2 , num):
    if(num%2 != 0 ):
        prime = True


if(prime):
    print("The number is prime")
else:
    print("The number is not prime")
