bio = int(input("Enter your marks in bio"))
chem = int(input("Enter your marks in chem"))
phy = int(input("Enter your marks in in phy"))
his = int(input("Enter your marks in in his"))
geo = int(input("Enter your marks in geo"))

average = (bio + chem + phy + his + geo)/5
print(average)
if(average >= 90 and average <= 100):
    print("You got an A+")

elif(average >= 75 and average < 90):
    print("You got an A")

elif(average >= 60 and average < 75):
    print("You got a B")

elif(average >= 50 and average < 60):
    print("You got a C")

elif(average >= 40 and average < 50):
    print("You got a D")

else:
    print("You got a F")