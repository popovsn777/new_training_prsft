__author__ = 'popov.sn'


from geom2d.point import *

l = [Point(i, i*i) for i in range(-5,6)]
print(l)

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
print(l)


l2 = list(map (lambda p: Point(p.x, -p.y), l))
print(l2)