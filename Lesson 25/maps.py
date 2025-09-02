num1 = [1,2,3]
num2 = [2,3,4]

result = map(lambda x,y:x+y, num1, num2)
#lambda is a shortcut you can use for simple operations instead of functions
#you have to use map function first keyword lambda space arguments then : operation 
# you want to do and then the variables you are using 

print(list(result))
#This helps us convert the answer in to a list using the list keyword

num3 = [3,4,5]

def sq(n):
    return n*n

square = list(map(sq,num3))
#This helps us to map num3 values to n

print(square)