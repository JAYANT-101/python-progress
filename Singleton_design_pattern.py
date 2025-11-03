class ppap:
    _instance=None
    print(_instance,"out side")
    def __init__(self, name):
        self.name=name
        print(name)
    def __new__(cls, *args, **kwargs):
        print(cls._instance,"inside")
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance


a=ppap("jayant")
b=ppap("jaya")
print(a is b)