class book:
    def __init__(self):
        self.nobook=0
        self.allbook=[]

    def addbook(self,book):
        self.allbook.append(book)
        self.nobook=len(self.allbook)
    def ShowInfo(self):
        print(f"The count of the books are {self.nobook} and the books are")
        for i in self.allbook:
            print(i)
a=book()
a.addbook("tipu")
a.addbook("tipu2")
a.addbook("daadaddna")
a.ShowInfo()