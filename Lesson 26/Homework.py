import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

chars = ""
i = 0

while i < 12:
    randomized = random.choice(letters)
    i += 1

print(randomized)