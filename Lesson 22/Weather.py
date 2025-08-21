tuple1 = (1,0,0,1,0,1,1)

sunny = 0
rainy = 0

for i in tuple1:
    if tuple1[i] == 1:
        sunny += 1
    else:
        rainy+=1

print("The value of sunny is", sunny)
print("The value of rainy is", rainy)

if sunny > rainy:
    print("The weather will be sunny")

elif rainy > sunny:
    print("The weather will be rainy")

else:
    print("The weather will not be sunny or rainy")