import random

playing = True

number = random.randint(10,20)

print("Guess a number between 10 and 20\nWhen you get the correct number the game ends")

while playing:
    inp = int(input("Enter a number"))

    if number == inp:
        print("You got the correct number", number)
        break
    else:
        print("Keep guessing")
