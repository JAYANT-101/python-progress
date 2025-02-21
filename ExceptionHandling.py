a=input("enter the number")
print(f"the Mtable of the {a} is")
try:
 for i in range(0,11):
    print(f"{int(a)} X {i} = {int(a*i)}")
except:
    print("Invalid input")
print("End")