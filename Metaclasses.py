#making a class with using the class syntax

#making this class to make inheritance
class Foo:
    def show(self,name):
        print("foo",name)

#making a method in the class
def add_attribute(self,z):
    self.z=z
Test=type("Test", (Foo,), {"a":4, "add_attribute":add_attribute})
test=Test()
print(test.a)
test.show("test")
test.add_attribute(43)
print(test.z)
#--------------------------------------------------------------------------------------------------------------
#Making a metaclass
class Meta(type):
    def __new__(self, name, bases, attrs):
        a={key if key.startswith("__") else key.upper():value for key, value in attrs.items()}
        print(a)
        return type(name, bases, a)
class test(metaclass=Meta):
    x=5
    b="jayant"
    def hello(self):
        print("hi")
