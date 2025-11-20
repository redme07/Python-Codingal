def compare(n1,n2):
    return str(n1) + str(n2) > str(n2) +str(n1)
def largest(num):
    for i in range(len(num),0,-1):
        tmp = 0
        for j in range(i):
            if not compare(num[j],num[tmp]):
                tmp = j
        num[tmp],num[i-1] = num[i-1],num[tmp]
    return str(int("".join(map(str,num))))

num = [9,5,2,3,7,1,5,2,8]
print(largest(num))