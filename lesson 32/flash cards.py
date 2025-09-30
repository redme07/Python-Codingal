class flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + "(" + self.meaning + ")"
    
flash = []
print('welcome to flashcard applictaion')

while True:
    word = input("enter a word: ")
    meaning = input("enter the meaning of the word:")

    flash.append(flashcards(word,meaning))

    option = int(input("enter 0 if you want to continue or if you want to end enter 1: "))
    if (option):
        break

print("your flashcard are: ")

for i in flash:
    print(">", i)