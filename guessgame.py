# NO GUESSING GAME BETWEEN 1 TO 100

import random
num = random.randint(1,10)
guess = int(input("enter the number to be gussed between 1 to 100 :"))
attempts=0
while num != guess:
    if (guess>num):
        print("TOO HIGH")
    else:
        print("LOW HIGH")

    guess=int(input("guess again :"))    
    attempts=attempts+1
     

print("CONGRATULATION !! your guess is right ")  
print("YOUR TOTAL ATTEMPTS : ",attempts)   