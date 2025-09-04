import time
import random

num = random.randint(1,200)

def intro():
    print("What is your name")
    global name 
    name = input()
    print("We are going to play a game pick a number between one to hundred")

    if num%2 == 0:
        x = "even"
    else:
        x = "odd"
    
    print(f"The number is {x}")
    time.sleep(.5)
    print("Guess the number")

def pick():
    guesstaken = 0

    while guesstaken<6:
        time.sleep(.25)
        enter = input("Enter the guess")
        try:
            guess = int(enter)
            if guess <= 200 and guess >= 1:
                guesstaken+=1
                if guesstaken < 6:
                    if guess < num:
                        print("Go higher")
                    if guess>num:
                        print("go lower")
                    if guess!=num:
                        print("Try again")
                    if guess == num:
                        print("You got it right")
                        break
            if guess>200 or guess<1:
                print("Invalid please enter below 200 and above 1")
            
        except:
            print("Its not that number")
    
    if guess == num:
        print(f"Good job you got the answer{guess}")
    if guess != num:
        print(f"You have not got the answer try again later; the correct answer is {num}")

playagain = "yes"

while playagain == "yes" or playagain == "y":
    intro()
    pick()

    print("do you want to play again")
    playagain = input()
    

