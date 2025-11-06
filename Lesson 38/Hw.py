def flip(a,size,choice):
    flipper = 0
    if choice == 1:
        flipper = 0
    else:
        flipper = 1
    for i in range(size):
        if a[i] == choice:
            a[i] = flipper
    return a

a = [0,0,1,1,0,0,0,1,0,1,0,1,0]
choice = 0
size = len(a)
print(flip(a,size,choice))
#the choice is the type of number u want to replace
