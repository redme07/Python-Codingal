print("Enter your choice")
print("\n 1. bike")
print("\n 2. car")

choice = int(input("Enter your choice"))

if(choice == 1):
    print("What type of bike")
 # When using nested if conditions you should put all statements that you want to be a part of the 
    print("1. scooty")
    print("2. scooter")
    choice2 = int(input("Enter your choice between the two"))

    if(choice2 == 1):
        print("You have selected scooty")

    else:
        print("You have chosen scooter")

elif(choice  == 2):
    print('What type of car')

    print("1. Sedan")
    print("2. hatchback")
    print("3. Jeep")

    choice3 = int(input("Enter your choice"))

    if(choice == 1):
        print("You have chosed Sedan")
    
    elif(choice == 2):
        print("You have chosen hatchback")

    else:
        print("You have chosen Jeep")

else:
    print("Wrong choice")


