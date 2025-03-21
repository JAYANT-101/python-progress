class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
            print(f"The name is {self.name}")
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show2(self):
        print(f'The dance is {self.dance}')
class Both(Employee,Dancer):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance
o=Both("lalu","nachaniya")
print(o.name)
print(o.dance)