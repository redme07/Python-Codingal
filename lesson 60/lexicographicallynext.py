def graph(inp):
    if inp == "":
        return "a"
    i = len(inp)-1
    while inp[i] == "z" and i>=0:
        i-=1
    if i == -1:
        inp = inp + "a"
    inp = inp.replace(inp[i],chr(ord(inp[i])+1),1)

    return inp
inp = input("enter a string:")
print(graph(inp))
