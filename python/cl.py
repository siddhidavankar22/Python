class Point:
    def draw(self):
        print("drew a point in the program")


point = Point()
print(point.draw())
print(type(point))
print(isinstance(point, Point))
