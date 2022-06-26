class test:
    a =0;
    b =0;
    def __init__(self,x,y):
        self.a = x
        self.b = y
    def eq(self ,obj):
        if(obj.a>obj.b):
            return "A is greater"
        else:
            return "B is greater"
obj = test(3,5)
print("result",obj.eq(obj))