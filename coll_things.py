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
import inspect
from queue import Queue
#can get the source code of any THING
print(inspect.getsource(Queue))