class base:
    def show1(self):
        print("base")
class drived1(base):
    def show2(self):
        print("derived")
class drived2(base):
    def show3(self):
        print("derived2")
obj = drived2()
obj.show1()