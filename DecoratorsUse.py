import time
def execution_time(func):
    def warpper(*args, **kargs):
        print("this is a costume decorator ")
        start = time.time()
        print(start)
        result = func(*args, **kargs)
        end = time.time()
        print(end)
        return result
    return warpper
@execution_time
def add(a,b):
    print(a+b)

add([34],[2])

#-------------------------------------------------------------------------------------------------------------------
class Dc:
    def __init__(self, num: int)->None:
        self._num = num
    @property
    def num(self)-> int:
        return self._num
    @num.setter
    def num(self, num)-> None:
        self._num = num
    @num.deleter
    def num(self)-> None:
        print("deleted")
        del self._num
c=Dc(2)
print(c.num)
c.num=3
print(c.num)
del c.num