class bird:
    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")

class penguin(bird):
    def __init__(self):

        super().__init__()
        print("penguin is ready")
    
    def whoisthis(self):
        super().whoisthis()
        print("This is penguin")
    def run(self):
        print("run faster")

obj = penguin()
obj.whoisthis()
obj.run()
obj.swim()