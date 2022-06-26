class demo:
    def show1(self):
        print("Hello")
    def show2(self):
        print("This is jit code")
        self.show1()
obj = demo()
obj.show2()
# obj.read()
# obj__dict__

