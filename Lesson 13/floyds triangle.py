print("Floyds triangle")

n =int(input("Enter number of rows"))

number = 1

for i in range(1,n+1):

    for a in range(1,i+1):

        print(number, end=" ")
        number += 1
    
    print()