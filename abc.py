from abc import ABC,abstractmethod
class abstractclass(ABC):
    pass
    @abstractmethod
    def dosomething(self):
        print("Thiss si")
class abcexample(abstractclass):
    def dosomething(self):
        # super().dosomething()
        print("Thissisiisisisis")
obj = abcexample()
obj.dosomething()