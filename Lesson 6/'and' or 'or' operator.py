a = 0
b = 78
c = 23

if(a and b and c):
    print(True)

else:
    print(False)

d = 10
e = -23
f = 0

if(d>0 or e>0):
    print("Either of the number is greater than 0")

else:
    print("no number is greater than 0 ")
#If there is an 'or' opertor then only one statement needs to be true in prder for the if statement to be true
if(e>0 or f>0):
    print("Either of the numbers are greater than zero")

else:
    print("e and f are not greater than 0")