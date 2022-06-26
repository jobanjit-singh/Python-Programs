class demo:
    x=5
    def info(self,x):
        print("Local",x)
        print("Instance",self.x)
obj =  demo()
obj.info(30)