class greet:
    def greeting(self,name=None):
        if name!=None:
            print("Welcome",name)
        else:
            print("welcome")
obj = greet()
print("first call")
obj.greeting()
print("Second call")
obj.greeting('joban')