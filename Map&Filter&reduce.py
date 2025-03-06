#Map
def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,3,4,5]
# n=[]
# # for item in l:
# #     n.append(cube(item))
# # print(n)
n=list(map(cube,l))
print(n)
#Filter
def filter_function(a):
    return a>4
newn=list(filter(lambda x: x<4,l))
print(newn)
#Reduce
from functools import reduce
number = [1,2,3,4,5]
s = reduce(lambda x , y:x+y, number)
print(s)