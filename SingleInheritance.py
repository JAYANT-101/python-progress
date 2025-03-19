class God:
    def __int__(self,name,num):
        self.name=name
        self.num=num
    def Demo(self):
        print(f'{self.name} is the only true god emperor in {self.num} years')
class GODv2(God):
    def demo2(self):
        print(f'In {self.num} years the only god emperor is {self.name}')
a=GODv2("jayant",1000000)
