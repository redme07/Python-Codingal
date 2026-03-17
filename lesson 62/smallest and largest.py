
def words(str1):
    word = ""
    
    all_words = []
    str1 += " "

    for i in range(len(str1)):
        if str1[i] != " ":
            word += str1[i]
        else:
            if word != "":
                all_words.append(word)
                word = ""
    smallest = all_words[0]
    largest = all_words[0]

    for i in range(all_words):
        if len(all_words[i]) < len(smallest):
            smallest = all_words[i]
        if len(all_words[i]) > len(largest):
            largest = all_words[i]
    return smallest,largest

str1 = input("Enter a sentence: ")
smallest,largest = words(str1)
print(smallest,largest)









# 5) Find the smallest and largest word by length:

# a) Loop through all_words:

# - If current word is shorter than `small`, update `small`.

# - If current word is longer than `large`, update `large`.

# 6) Return the results:

# a) Return (small, large).

# 7) Driver code:

# a) Take a sentence input from the user.

# b) Call smallest_largest_words(s).

# c) Print the smallest and largest words.