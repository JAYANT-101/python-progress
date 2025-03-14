from tkinter.font import names


class Parent:
    def parentMethod(self):
        print("I am a parent class")
class Child(Parent):
    def parentMethod(self):
        print("Same method in child class")
        super().parentMethod()
    def ChildMethod(self):
        print("I am a child class")
        super().parentMethod()
Cobj=Child()
Cobj.ChildMethod()
Cobj.parentMethod()
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name=name
        # self.id=id
        super().__init__(name,id)
        self.lang=lang
a=Employee("jaya",1243)
b=Programmer("jayant",15423,"Ever thing")
print(b.name)
print(b.id)
print(b.lang)