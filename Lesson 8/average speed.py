cycle1 = int(input("Enter speed of one cycle"))
cycle2 = int(input("Enter speed of another cycle"))
cycle3 = int(input("Enter speed of one more cycle"))

average = (cycle1 + cycle2 + cycle3)/3

print("The average of the speed of cycles is", average)

if(cycle1 < average):
    print("cycle1 is running slower than the average of the 3")

if(cycle2 < average):
    print("cycle2 is running slower than the average")

if(cycle3 < average):
    print("cycle3 is running slower than the average")
