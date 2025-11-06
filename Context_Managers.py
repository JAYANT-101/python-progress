class File:
    def __init__(self, filename, mode):

        self.file = open(filename, mode)
    def __enter__(self):
        print("enter")
        return self.file #this will be return to when a file is open
    def __exit__(self, type, value, traceback):
        print("exit")
        self.file.close()
# this return from the __enter__ will be stored in the file ok
with File("test.txt", "w") as file:
    print("writing")
    file.write("hello")