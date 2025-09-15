def palindrome(r):
    e = len(r)-1
    s = 0

    while s < e:
        if r[s] != r[e]:
            return False
        s+=1
        e-=1

    return True

r = (2,3,4,4,3,2)

if palindrome(r):
    print(f"The tuple {r} is a palindrome")

else:
    print(f"The tuple {r} is not a palindrome")