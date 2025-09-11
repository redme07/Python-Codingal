class uppercase:

    def __init__(self):
        self.str1 = ""
    
    def get_string(self):
        self.str1 = input("Enter a word")
    
    def print_string(self):
        print("result is :", self.str1.upper())

ob1 = uppercase()

ob1.get_string()
ob1.print_string()