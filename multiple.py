class base1:
    def show1(self):
        print("base1")
class base2:
    def show2(self):
        print("base2")
class derived(base1,base2):
    def show3(self):
        print("Derived")
obj = derived()
obj.show1()
obj.show2()