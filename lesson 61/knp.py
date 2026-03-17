
# 1) Create a function to find the smallest and largest words:

# a) Take a sentence (str1) as input.

# 2) Initialize helpers to build and store words:

# a) Use `word` to build the current word character by character.

# b) Use `all_words` list to store all extracted words.

# c) Add an extra space at the end of the sentence so the last word is captured.

# 3) Extract words from the sentence:

# a) Loop through each character in str1.

# b) If the character is not a space, add it to `word`.

# c) If the character is a space:

# - If `word` is not empty, append it to all_words.

# - Reset `word` to empty for the next word.

# 4) Initialize smallest and largest:

# a) Set both `small` and `large` to the first word in all_words.

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