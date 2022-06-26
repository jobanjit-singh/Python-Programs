class base:
    def show(self):
        print("base")
class der(base):
    def show(self):
        super().show()
obj = der()
obj.show()