a=int(input("enter number"))
b = input("enter the first number")
c = input("enter the second number")
match a:
    case 1:
        print (int(b)+int(c),"result")
    case 2:
        print(int(b)-int(c),"result")
    case _ if a<3:
        print("not gona work bro")
    case 3 if a<5:
        print("nada")