"""rock paper scissor"""

import random 
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="r":
        if you== "p":
            return True
        elif you=="s":
            return False
    elif comp=="s":
        if you=="r":
            return True
        if you=="p":
            return False
    elif comp=="p":
        if you=="s":
            return True
        if you=="r":
            return False
print("comp Turn : Rock(s) Paper(p) Scisser(s) ?")
randNo= random.randint(1,3)
if randNo == 1:
    comp="r"
elif randNo == 2:
    comp="p"
elif randNo == 3:
    comp="s"
    
    
you = input("your turn : Rock(r) Papee(p) Scisser(s)?")
a = gameWin(comp ,you)

print(f"computer chose {comp}")
print(f"you chose {you}")


if a==None:
    print("tie !")
elif a:
    print("you Win !") 
else :
    print("you Lose!") 