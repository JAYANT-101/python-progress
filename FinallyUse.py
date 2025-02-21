def func1():
 try:
    l=[1,2,3,4]
    i=int(input("Enter number"))
    print(l[i])
    return 1
 except:
    print("Something went wrong")
    return 0
 finally:
    print("the program is done with")
x=func1()
print(x)