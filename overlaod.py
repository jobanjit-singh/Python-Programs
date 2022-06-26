class demo:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!= None:
            print("Three parameters addition:")
            print(a+b+c)
        elif a!=None and b!=None:
            print("Two parameters addition:")
            print(a+b)
        else:
            print("One parameters addition")
obj = demo()
obj.add(8,9,3)
obj.add(8,9)
obj.add()
