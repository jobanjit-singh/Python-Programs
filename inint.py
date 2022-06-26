import math
class demo:
    def __init__(self,pi):
        self.pi1 =pi
    def circle(self,radius):
        return self.pi1*radius**2
obj = demo(3.14)
print("this is area of circle",obj.circle(5))
    