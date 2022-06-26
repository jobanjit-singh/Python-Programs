from re import L


class base:
    def show(self):
        print("base")
class derived1(base):
    def show1(self):
        print("derived1")
class derived2(base):
    def show2(self):
        print("derived2")
class combo(derived1,derived2):
    def sow4(self):
        print("Combo")
obj = combo()
obj.show()
obj.sow4()