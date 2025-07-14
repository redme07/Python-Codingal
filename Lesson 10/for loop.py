n = int(input("Enter a number"))

sum = 0
# The range operation is like slicing
for i in range(1,n+1):
    sum = sum + i
    print(sum)
#if you keep the print statement inside the for 
 # loop it will print every time the loop runs