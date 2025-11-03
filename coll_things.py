def class_maker(number):
    class innClass:
        def __init__(self, name):
            self.name = name
        def printNumber(self):
            print(number)
    return innClass
a=class_maker(1)
b=a("jayant")
print(b.name)
b.printNumber()