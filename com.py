class overload:
    def __init__(self,x):
        self.x = x
    def __eq__(self,other):
        print("The value of 1 object is",self.x)
        print("The value of 2 object is",other.x)
        return self.x == other.x
obj = overload(30)
obj2 = overload(30)
ob3 = obj == obj2
print(ob3)