# create point class
class Point:
    def __init__(self, x, y):
        #assign objects
        self.x = int(x)
        self.y = int(y)


# define distance function
def calc_distance(p1, p2):
    a = p1.x - p2.x #define side 'a' for pythagoran distance calculation
    b = p1.y - p2.y #define side 'b' for pythagoran distance calculation
    return pow((pow(a, 2) + pow(b, 2)), 0.5) #find side 'c', or distance


# take inputs
raw_p1 = input()
raw_p2 = input()

# split input into coordinates
x1, y1 = raw_p1.split(" ")
x2, y2 = raw_p2.split(" ")

# define points
point1 = Point(x1, y1)
point2 = Point(x2, y2)

# get distance
print(f"{calc_distance(point1, point2):.3f}")
