class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def ShowDetails(self):
        print(f"The name of the Employee is {self.name} and the id is {self.id}")
class Programmer(Employee):
    def ShowLang(self):
        print("Python")
a=Employee("jayant",123)
a.ShowDetails()
b=Programmer("jaya",123)
b.ShowLang()
b.ShowDetails()