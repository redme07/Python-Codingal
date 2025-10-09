def second_largest(a):
    b = sorted(a)
    return b[-2]

a = [1,4,2,7,5,0,8,9,3]
print(second_largest(a))
