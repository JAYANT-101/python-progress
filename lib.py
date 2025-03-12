class book:
    def bookchek(self):
        allbook=["jonbububla","chitifur noland","kaju kateli","dandadan"]
        print(len(allbook))
        if len(allbook) <= 3:
            print("All books are not present")
        else:print("every book is present")
a=book()
a.bookchek()