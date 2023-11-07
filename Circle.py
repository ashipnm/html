class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def  circumference(self):
        return self.radius*2*3.14
C=Circle(8)
print("area of circle is",C.area())
print("Circumference  of circle is ",C.circumference())         