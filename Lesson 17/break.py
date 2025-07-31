chr = input("Enter a word")
# The break command makes the loop stop
for i in chr:
    if i == "a" or i == "A":
        print("A is found")
        break
    else:
        print('A is not present')
