class base:
    def show(self):
        print("base class")
class derived(base):
    def showinfo(self):
        print("derived class")
obj = derived()
obj.show()