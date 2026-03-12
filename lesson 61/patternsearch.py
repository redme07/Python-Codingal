d = 10

def searchpattern(pattern,text,q):
    m = len(pattern)
    n = len(text)
    p = 0 
    t = 0 
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d)%q

    for i in range(m):
        p = (p*d+ord(pattern[i]))%q
        t = (t*d+ord(text[i]))%q

    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j+=1
            if j == m:
                print("pattern is found",str(i+1))
        if i < n-m:    
            t = (d*(t-ord(text[i])*h)+ord(text[i+m]))%q
            if t < 0 :
                t = t+q

text = "ababcababc"
pattern = "bab"
q = 101
searchpattern(pattern,text,q)      
