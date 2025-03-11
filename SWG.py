import random
print("Enter the 1. snake\n2.water\n3.gun")
a=int(input())
b=random.randint(1,3)
if a==b:
    print("tie")
elif a==1 and b==3:
    print("you lose")
elif a==2 and b==1:
    print("you lose")
elif a==3 and b==2:
    print("you lose")
else:print("you win")