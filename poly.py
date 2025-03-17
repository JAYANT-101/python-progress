class buba:
    name="Jayant"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    # def __str__(self):
    #     return f"The one and only god {self.name}"
    def __repr__(self):
        return f"THe one and only god {self.name} buba"
    def __call__(self):
        print("Hey i am good")