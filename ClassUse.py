class Person:
    name="Jayant"
    occupation="Software developer"
    networth=10
    def info(self):#sefl will run for the given instance of the object
        print(f"{self.name} is a {self.occupation}")
a=Person()
a.name="jaya"
a.info()