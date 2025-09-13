import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

chars = ""
i = 0
letters2 = ""
while i < 12:
    randomized = random.choice(letters)
    letters2 += randomized
    i += 1

print(letters2)