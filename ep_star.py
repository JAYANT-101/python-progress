a = input("enter a numbers of rows ")
b=int(a)
c=1
for i in range(1,b+1):
    print(" " * b, "*" * c)
    b-=1;c+=2