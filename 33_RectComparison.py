class Rectangle:
    def __init__(self,l,b):
        self.__length = l
        self.__breath = b
    def getDimentions(self):
        return self.__length,self.__breath
    def getArea(self):
        return self.__length*self.__breath
    def __it__(self, other):
        if self.getArea() < other.getArea():
            return "1st rectangle is smaller"
        else:
            return "2nd rectangle is smaller"
length1= int(input("Enter the 1st rectangle length: "))
breath1 = int(input("Enter the 1st rectangle breath: "))
ar1 = Rectangle(length1,breath1)
length2 = int(input("Enter the 2nd rectangle length: "))
breath2 = int(input("Enter the 2nd rectangle breath: "))
ar2 = Rectangle(length2,breath2)
print(f"Area of 1st rectangle= {ar1.getArea()} & Area of 2nd rectangle= {ar2.getArea()}")
print(ar1<ar2)
               
