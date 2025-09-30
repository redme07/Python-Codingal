import random
class fruits:

    def __init__(self):
        self.fruits = {"apple":"red", "orange":"orange","banana":"yellow","blueberry":"blue"}
    
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            print("what is the color of", fruit)

            answer = input()
            if answer.lower() == color:
                print("correct answer")
            else:
                print("wrong")

            option = int(input("if continue enter 0 and if not enter 1"))

            if option:
                break 

ob1 = fruits()
ob1.quiz()
           

