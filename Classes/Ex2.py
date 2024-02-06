class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length
    def AreaOfSquare(self):
        return self.length**2

def main():
    length=float(input("Enter a length of the square: "))
    square=Square(length)
    print("Area of the square: ", square.AreaOfSquare())
if __name__=="__main__":
    main()
    