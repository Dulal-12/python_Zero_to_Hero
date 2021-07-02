def sumOfNaturalNum(n):
    if(n == 1):
        return 1
    else:
        return n + sumOfNaturalNum(n-1)

print(sumOfNaturalNum(10))