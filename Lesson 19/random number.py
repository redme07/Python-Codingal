import random

playing = True

number = random.randint(10,20)#.randint lets you chose what integers you want to randomize

print("Guess a number between 10 and 20\nWhen you get the correct number the game ends")

while playing:
    inp = int(input("Enter a number"))

    if number == inp:
        print("You got the correct number", number)
        break
    else:
        print("Keep guessing")
