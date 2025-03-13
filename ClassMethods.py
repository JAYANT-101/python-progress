class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod#This is used for making the first instance in to a class instance not a method instance
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)