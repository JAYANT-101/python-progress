#Hybrid inheritance
class BaseClass:
    def __init__(self,name):
        self.name = name

    def base1(self):
        print(f"This is base class {self.name}")    
    def test(self):
        print(f"bula {self.name}")
class DriveClass(BaseClass):
    def d1(self):
        print(self.name)
    def test(self):
        print("puna over")
class DriveClass2(BaseClass):
    def d2(self):
        print("lula")
    def test(self):
        print("puna2 over")
class DriveClass3(DriveClass2,DriveClass):
    def __init__(self,name):
        super().__init__(name)
a=DriveClass3("jayant")
a.test()
a.base1()
a.d1()
a.d2()
# Hierarchical inheritance
class b1:
    pass
class d1(b1):
    pass
class d2(b1):
    pass
class c1(d1):
    pass
class c2(d2):
    pass