from functools import reduce

def poly_constructor(self, no_sides):
    self.no_of_sides = no_sides

def poly_set_sides(self, *args):
    for side in args:
        self.list_of_sides.append(side)
def poly_find_area(self):
    s = sum(self.list_of_sides)/2
    t = reduce(lambda a,b: a*b, [s-side for side in self.list_of_sides])
    return round((s*t)**0.5)

def strFix(obj):
    if '__str__' not in obj.__dict__:
        setattr(obj, '__str__', lambda x: str(vars(obj)))


Polygon = type ('Polygon',(object,),{'no_of_sides' :0,
                                    '__init__': poly_constructor,
                                    'getSides':(lambda obj: obj.no_of_sides)})

def createSubClass(parent):
    return type('SubPoly',
                (Polygon,),
                {
                    'list_of_sides': [],
                    'setSides': poly_set_sides,
                    'findArea': poly_find_area,
                    'get_sides': lambda x: x.list_of_sides
                })


triangle = createSubClass(Polygon)(3)
triangle.setSides(4,5,6)
print(triangle.findArea())

strFix(type(triangle))

print(triangle)