"""rock paper scissor"""

import random 
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="R":
        if you== "P":
            return True
        elif you=="S":
            return False
    elif comp=="S":
        if you=="R":
            return True
        if you=="p":
            return False
    elif comp=="P":
        if you=="S":
            return True
        if you=="R":
            return False
print("comp Turn : rock(R) paper(P) scisser(S) ?")
randNo= random.randint(1,3)
if randNo == 1:
    comp="R"
elif randNo == 2:
    comp="P"
elif randNo == 3:
    comp="S"
    
    
you = input("your turn : rock(R) papee(P) scisser(S)?")
a = gameWin(comp ,you)

print(f"computer chose {comp}")
print(f"you chose {you}")


if a == None:
    print("the game is a tie !")
elif a:
    print("you Win !") 
else :
    print("you Lose!") 
    