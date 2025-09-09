class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = parrot("blu", 10)
woo = parrot("woo", 14)

print(f"blue is a {blu.species}")
print(f"woo is a {blu.species}")
#This is how u call a class variable 
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")