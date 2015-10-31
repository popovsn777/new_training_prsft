__author__ = 'Sergey'


from geom2d import point

Point = point.Point

l1 = [Point(0, 0), Point(1, 2), Point(2, 1) ]
l2 = [Point(0, 0), Point(1, 2), Point(2, 1) ]


print (l1 == l2)
