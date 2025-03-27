def my_generator():
    for i in range(5):
        yield i # will generate values at a time id next is used
g=my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))