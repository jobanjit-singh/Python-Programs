class demo:
        name = "Show"
        __name1 = "show1"
        def show(self):
            print(self.name)
            print(self.__name1)
obj = demo()
obj.__name1 = "a"
obj.show()
            