name = input("Enter a word")

string = ""

for i in name:
    string = i + string

print(f"The original string is {name}")
print(f"The reversed string is {string}")
# for line 6 the logic is, example = word
# i = 0, str = w + ""
# i = 1, str = o + w + ""
# i = 2, str = r + o + w + ""
# i = 3, str = d + r + o + w + ""  