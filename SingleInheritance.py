class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")
class Cat(Animal):
    def __(self,name,age):
        Animal.__init__(self,name,species="Cat")
        self.age=age
    def make_sound(self):
        print("Meaawww")

d = Dog("Dog", "Doggerman")
d.make_sound()
c = Cat("Caaat",6)
c.make_sound()
a = Animal("Dog", "Dog")
a.make_sound()