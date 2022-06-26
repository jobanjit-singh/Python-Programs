class a:
    def print1(self):
        print("Supr Class")
class b(a):
    def print2(self):
        print("Subclas")
obj = b()
obj.print1()