x=10
print(x)
def mufun():
    global x # will change global venerable
    x=4
    y=3
    print(y)
mufun()
print(x)
# print(y) a local venerable will not work outside