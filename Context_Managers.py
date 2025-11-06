class File:
    def __init__(self, filename, mode):

        self.file = open(filename, mode)
    def __enter__(self):
        print("enter")
        return self.file #this will be return to when a file is open
    def __exit__(self, type, value, traceback):
        print("exit")
        self.file.close()
        # return True this can be done to make the programme to still work even after an exception is raised it but use
        # carefully only when the exception is handled
# this return from the __enter__ will be stored in the file ok
with File("test.txt", "w") as file:
    print("writing")
    file.write ("hello")
    # raise Exception() simulating an exception
#--------------------------------------------------------------------------------------------------------------------------------------
from contextlib import contextmanager
@contextmanager
def file(fielname, method):
    print("enter")
    file = open(fielname, method)
    yield file
    file.close()
    print("exit")
with file("test.txt", "w") as f:
    print("writing")
    f.write ("hello")