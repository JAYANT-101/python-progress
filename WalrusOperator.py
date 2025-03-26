#example 1
number=[1,2,3,4,5]
while n:= len(number) > 0:
    print(number.pop())
#example 2
# a=True it also works without declaring the "a" ok
print(a:=False)
#example 3
food=list()
# while True: #Without walrus operator
#     foods=input("Entre things")
#     if foods=="quit":
#         break
#     else:
#         food.append(foods)
#         print(food)
while str(foods:=input("Enter any thing")) !="quit":
    food.append(foods)
    print(food)