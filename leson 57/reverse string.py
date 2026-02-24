inp = input("enter string:")

def reverse(inp):
    
    n = len(inp)
    li = list(inp)
    for i in range(n//2):
        li[i],li[n-i-1] = li[n-i-1],li[i]
        return "".join(li)

print(reverse(inp))