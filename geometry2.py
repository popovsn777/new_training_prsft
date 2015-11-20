__author__ = 'popov.sn'

from geom2d.point import *

l = []

"""
for i in range(-5, 6):
    l.append(Point(i, i*i))

l2 = []
for el in l:
    l2.append(Point(el.x,  -el.y))
    print(el)
"""

l = [Point(i, i*i) for i in range(-5, 6)]

l2 = [Point(el.x,  -el.y) for el in l ]


print(l)
print (l2)
