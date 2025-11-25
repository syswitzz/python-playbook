from collections import namedtuple

# DECLARATION
Point = namedtuple('Point', 'x y z')    # automatically breaks up xyz into three different parameters
Point = namedtuple('Point', ['x', 'y', 'z'])    # we can give any iterable data and itll take it as parameters
Point = namedtuple('Point', {'x': 0, 'y': 0, 'z':1})    # it takes key as parameters and ignores their values
point = Point(3,4,5)

# METHODS
point.x, point.y, point.z    # 3 4 5
point._asdict()  # {'x': 3, 'y': 4, 'z': 5}
point[0]     # 3
point._fields    # ('x', 'y', 'z')

# FUNCTIONS
p1 = point._replace(x=6, y=6)    # Point(x=6, y=6, z=5)
p2 = point._make(['a', 3, '8'])    # Point(x='a', y=3, z='8')


