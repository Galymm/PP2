class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width
    def AreaOfRectangle(self):
        return self.length*self.width
def main():
    length=float(input("Enter a length: "))
    width=float(input("Enter a width: "))
    rec=Rectangle(length, width)
    print ("Area of a rectangle: ", rec.AreaOfRectangle())

if __name__=="__main__":
    main()