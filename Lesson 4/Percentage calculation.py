bio = int(input("Enter your biology marks:"))
chem = int(input("Enter your chemistry marks:"))
phy = int(input("Enter your physics marks:"))
maths = int(input("Enter your math marks:"))
english = int(input("Enter your english marks:"))
second_language = int(input("Enter your second_language marks:"))
history = int(input("Enter your history marks:"))
geography = int(input("Enter your geography marks:"))
computers = int(input("Enter your computer marks:"))
robotics = int(input("Enter your robotics marks:"))

sum = bio + chem + phy + maths + english + second_language + history + geography + computers + robotics

percentage = (sum / 800)*100
print ("The percentage of all your marks in the subjects are", percentage)



