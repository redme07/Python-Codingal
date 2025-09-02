s1 = {1,2,3,4}
s2 = {2,3,4,5}

s3 = list(zip(s1,s2))
print(s3)

l1 = [1,2,3,4,4]
l2 = [2,3,4,5,6]

for x,y in zip(l1,l2[::-1]):
    print(x,y)

d1 = ["reliance", "tata", "warree"]
d2 = [1000, 2000, 3000]

d3 = {d1:d2 for d1,d2 in zip(d1,d2)}

print(d3)