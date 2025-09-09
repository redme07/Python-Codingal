class dog:
    animal = "dog"
    def __init__(self,name,breed):
        self.breed = breed
        self.name = name

dog1 = dog("Tom","chitzu")
dog2 = dog("Kate","golden_retriever")

print(f"{dog1.name} is a {dog1.animal} who is a {dog1.breed}")
print(f"{dog2.name} is a {dog2.animal} who is a {dog2.breed}")