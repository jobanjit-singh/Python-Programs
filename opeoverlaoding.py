class overload:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        print("the value of object 1 is:",self.x)
        print("the value of object 2 is:",other.x)
        print("Add")
        return self.x + other.x
obj = overload(10)
obj2 = overload(30)
ob3 = obj+obj2
print(ob3)        