num = int(input("Enter a number that has more than 4 digits"))

temp = num

numLen = 0

while temp>0:
    numLen = numLen + 1

    temp = temp//10

if numLen>=4:
    numLen = int(numLen/2)
    chk = 0

    while num>0:
        rem = num%10

        if chk == numLen:
            midOne = rem

        elif chk == (numLen-1):
            midTwo = rem

        num = int(num/10)
        
        chk = chk + 1
    
    prod = midOne * midTwo

    print("The product of the middle numbers is = ",prod)

else:
    print("The number you have entered is not greater than or equal to 4")