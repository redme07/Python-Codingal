

for i in range(20):
# The pass statement does not do anything it just skips the specific statement
    if i%20 == 0:
        print(f'The number {i} is divisible by 20')
    elif i%15 == 0:
        pass
    elif i%5 == 0:
        print(f"The number {i} is divisible by 5")
    elif i%3 == 0:
        print(f"The number {i} is divisbile by 3")
    else:
        print("This number is not divible by 20, 5, 3", i)