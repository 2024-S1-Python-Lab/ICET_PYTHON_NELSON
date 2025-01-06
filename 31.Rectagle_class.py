#Rectange class with attributes length & breath

class Rect:
    def __init__(self, length, breath):
        self.l = length
        self.b = breath
    def area(self):
        ar=self.l * self.b
        return ar
    def perimeter (self):
        p=2 * (self.l + self.b)
        return p
x1 = int(input("Enter length of 1st rectangle : "))
y1 = int(input("Enter breath of 1st rectangle : "))
r1 = Rect(x1,y1)
print("Area of rectangle1:",r1.area())
print("Perimeter of rectangle: ",r1.perimeter())
x2 = int(input("\nEnter length of 2nd rectangle:: "))
y2 = int(input("\nEnter breath of 2nd rectangle:: "))
r2 = Rect(x2,y2)
print("Area of rectangle2: ",r2.area())
print("Perimeter of rectangle2: ", r2.perimeter())
if r1.area() == r2.area():
    print("\n Area of both rectangle are equal.")
else:
    print("\n Area of both rectangle are not equal.")
