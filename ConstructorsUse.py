class Person:
    # name="Jayant"
    # occ="Developer"
    def __init__(self,n,o):# it is a Constructors
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("jayant","Developer")
b=Person("jaya","Developer")
a.info()
b.info()