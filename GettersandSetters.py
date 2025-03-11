class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"Value id {self._value}")
    @property
    def value(self):
        return 10*self._value
    @value.setter
    def value(self,new):
        self._value=new
obj=MyClass(10)
obj.value=61
print(obj.value)
obj.show()