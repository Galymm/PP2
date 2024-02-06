import math

class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def show(self):
        print(f"Coordinates of point: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x=new_x
        self.y=new_y
    def dist(self, other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)
def main():
    x1=float(input("Enter 1st value of x: "))
    y1=float(input("Enter 1st value of y: "))
    point1=Point(x1, y1)

    x2=float(input("Enter 2nd value of x: "))
    y2=float(input("Enter 2bd valuer of y: "))
    point2=Point(x2, y2)

    point1.show()
    point2.show()

    distance=point1.dist(point2)
    print ("Distance between 1st and 2nd point: ", distance)

    new_x=float(input("Enter value for move x: "))
    new_y=float(input("Enter value for move y: "))
    point1.move(new_x, new_y)
    point1.show()

if __name__=="__main__":
    main()
