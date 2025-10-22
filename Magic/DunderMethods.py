class Dun:
    def __init__(self, *number):
        self.number = number
    def __str__(self):
        print(f"This is class Dum {self.number}")
    def __len__(self):
        return len(self.number)
    def __contains__(self, item):
        return item in self.number
    def __add__(self, other):
        return self.number + other.number
    def __repr__(self):
        return f"Dun({self.number})"
    def jj(self):
        print(self.number)
    def __iter__(self):
        return iter(self.number)

dun = Dun(1,2,3)
print(len(dun))
for i in dun:
    print(i)