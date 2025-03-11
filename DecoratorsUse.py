import logging
def hello(a):
    def ab(*args,**kwargs):#*argd conversant in to tuple and **kwargs converts to dictionary
        print("This is th ab def")
        a(*args,**kwargs)
        print("This is ab def end")
    return ab
@hello
def add(a,b):
    print(a+b)
#hello(add)()
add(3,5)
# def log(a):
#     def np(*args,**kwargs):
#        logging.info(f"Calling {a.__name__} with args {args}, kwargs {kwargs}")
#        result=a(*args,**kwargs)
#        logging.info(f"{a.__name__} returned {result}")
#        return result
#     return np
# def my_function(a,b):
#     return a+b
# log(my_function(1,3))