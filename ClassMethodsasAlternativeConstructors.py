class Emoloyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("_")[0],int(string.split("_")[1]))
a=Emoloyee("jayant",10000000)
print(a.name)
print(a.salary)
string="jaya_100000"
b=Emoloyee.fromStr(string)
print(b.name)
print(b.salary)