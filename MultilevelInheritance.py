class f1:
    def __init__(self,name):
        self.name=name
        print(f'this is f1 {self.name}')
    def meth1(self):
        print("this is meth1")
class f2(f1):
    def __init__(self,name,id):
        super().__init__(name)
        self.id=id
        print(f'This is f2 {self.id}')
class f3(f2):
    def __init__(self,name,id,num):
        super().__init__(name,id)
        self.num=num
        print(f"This is f3 {self.num}")
a=f3("Jayant","566","5656")
a.meth1()