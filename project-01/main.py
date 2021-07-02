import random
def gameWin(comp , you):
    
    if comp == you :
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False



print('Comps Turn : snake(s) , water(w) or gun(g) : ')
randNo = random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
you = input('Player Turn : snake(s) , water(w) or gun(g) : ')

a = gameWin(comp , you)

print(f"Your choice {you} and comp choice {comp}")

if a == None:
    print("The match tie")
elif a:
    print("You win")
else:
    print('You lose')