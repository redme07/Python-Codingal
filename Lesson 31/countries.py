class India():
    def capital(self):
        print("the capital of india is New Delhi")
    def language(self):
        print("the language of india is hindi")
    def type(self):
        print("India is a developing country")

class russia():
    def capital(self):
        print("The capital of Russia is Moscow")
    def language(self):
        print("The language of Russia is Russian")
    def type(self):
        print("Russsia is developed country")

objI = India()
objR = russia()

for country in (objI, objR):
    country.capital()
    country.language()
    country.type()