from math import hypot

class Vector:
  def __init__(self,x=0,y=0):
   self.x=x
   self.y=y
  # overloads print method and __str__
  # default returns object location
  def __repr__(self):
  # %r returns numerics and not strings
    return 'Vector(%r, %r)' % (self.x, self.y)
  def __abs__(self):
    return hypot(self.x, self.y)
  # any context where you need to determine true vs false
  def __bool__(self):
    return bool(abs(self))
  # overloads + operator
  def __add__(self, other):
    x=self.x + other.x
    y=self.y + other.y
    return Vector(x,y)
  # overload * operator
  def __mul__(self, scalar):
    return Vector(self.x*scalar, self.y*scalar)

# call __init__
v1 = Vector(2,4)
v2 = Vector(2,1)
# call __add__ & __repr__
print('__add__: ', v1+v2)
v = Vector(3,4)
# call __abs__ & __repr__
print('__abs__: ', abs(v))
# call __mul__ & __repr__
print('__mul__: ', v*3)
# call __abs__, __mul__, & __repr__
print('__abs__: ', abs(v*3))
