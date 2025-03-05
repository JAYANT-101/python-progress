# def double(x):
#     return x*2
# print(double(5))
double=lambda x:x*2
print(double(5))
def appl(fx,value):
    return 6+fx(value)
cube=lambda x:x*x*x
# print(appl(cube,2)) use in function
print(appl(lambda x:x*2,2))