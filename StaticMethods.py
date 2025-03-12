import ast


class Math:
    def __init__(self,num):
        self.num=num
    def ToSum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b
c=Math.add(1,2)
b=Math(5)
print(b.num)
b.ToSum(5)
print(b.num)
print(c)