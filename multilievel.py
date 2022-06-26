class base:
    def show(self):
        print("base")
class derived1(base):
    def show2(self):
        print("derived1")
class derived2(derived1):
    def show3(self):
        print("derived2")
obj = derived2()
obj.show()