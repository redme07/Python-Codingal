import random
while True:
    options = ["rock", "paper", "scissors"]

    comp_choice = random.choice(options)
    user = input("Enter rock or paper or scissors")


    if comp_choice == user:
        print("Its a tie of", comp_choice)

    elif comp_choice == "paper" and user == "scissors":
        print("You win using", user)

    elif comp_choice == "rock" and user == "paper":
        print("You won using paper")

    elif comp_choice == "scissors" and user == "rock":
        print("You won using rock")

    else:
        print("You lost")

    inp = input("Do you want to play again 'Y' for yes and 'N' for no")

    if inp.upper() == "N":
        break
    