__author__ = 'Sergey'


from geom2d import point

x_y_Point = point.Point

L1 = [x_y_Point(7, 2), x_y_Point(0, 6),  x_y_Point(3, 1) ]

"""
def x(p):
    return p.x

L2 = sorted(L1, key=x)
"""

#L2 = sorted(L1, key=lambda p: p.y)


L2 = sorted(L1, key=lambda p: p.distance(x_y_Point(0, 0)))

print("OK")

print(L1)
print(L2)