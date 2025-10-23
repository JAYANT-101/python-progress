import time
def execution_time(func):
    def warpper(*args, **kargs):
        print("this is a costume decorator ")
        start = time.time()
        print(start)
        result = func(*args, **kargs)
        end = time.time()
        print(end)
        return result
    return warpper
@execution_time
def add(a,b):
    print(a+b)

add([34],[2])