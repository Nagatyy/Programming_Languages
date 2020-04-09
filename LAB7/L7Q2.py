import collections

Point = collections.namedtuple('Point',['name', 'x', 'y'])

class ExistingPointError(Exception):

    def __init__(self):
        self.message = "ExistingPointError Exception Thrown"

    def __str__(self):
        return self.message


class PointNotFoundError(Exception):
    def __init__(self):
        self.message = "PointNotFoundError Exception Thrown"

    def __str__(self):
        return self.message


class Polygon:
    def __init__(self, p1, p2, p3, *args):
        self.points = []        # to store the points of the polygon

        self.points.append(Point(p1[0], p1[1], p1[2])) if isinstance(p1, tuple) and len(p1) is 3\
            else print("Incompatible constructor argument")
        self.points.append(Point(p2[0], p2[1], p2[2])) if isinstance(p2, tuple) and len(p2) is 3\
            else print("Incompatible constructor argument")
        self.points.append(Point(p3[0], p3[1], p3[2])) if isinstance(p3, tuple) and len(p3) is 3\
            else print("Incompatible constructor argument")

        # if there are more than 3 points
        for extraArgument in args:
            self.points.append(Point(extraArgument[0], extraArgument[1], extraArgument[2]))\
                if isinstance(extraArgument, tuple) and len(extraArgument) is 3 \
                else print("Incompatible constructor argument")

    ####################### Making a Polygon Iterable #######################
    def __iter__(self):
        return iter(self.points)

    def addPoint(self, p):
        if isinstance(p, tuple) and len(p) is 3:    # first we check if p is a valid point
            if Point(p[0], p[1], p[2]) in self.points:  # then we check for exact duplicate
                raise ExistingPointError()

            for point in self.points:
                if (point.name == p[0]) or (point.x == p[1] and point.y == p[2]):  # here we check for name and coords
                    raise ExistingPointError()

            self.points.append(Point(p[0], p[1], p[2]))     # if no exception raised, add the point
        else:
            print("Incompatible argument in addPoint")

    def getPoint(self, name):
        for point in self.points:
            if name is point.name:
                return point

        raise PointNotFoundError    # Exception thrown if no matching point found

    def deletePoint(self, name):
        for point in self.points:
            if name is point.name:
                self.points.remove(point)

        raise PointNotFoundError

    def __len__(self):
        return len(self.points)

    def __eq__(self, other):
        # we check that other is polygon
        if not isinstance(other, Polygon):
            return False
        # we check for equal number of points
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.points[i].x != other.points[i].x or self.points[i].y != other.points[i].y:
                return False
        return True

    def __str__(self):
        stringList = []
        for point in self.points:
            stringList.append(point.name)
            stringList.append(": ")
            stringList.append("(")
            stringList.append(repr(point.x))
            stringList.append(",")
            stringList.append(repr(point.y))
            stringList.append(")")
            stringList.append(" -> ")

        return "".join(stringList[:-1])


p= Polygon(Point('A',0,50), Point('B',300,150), Point('C',200,100))

for x in p: print(x)
