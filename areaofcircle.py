import math
class area:
    def calculate(self,radius):
        return math.pi*radius**2
obj = area()
print("The area is ",obj.calculate(5))