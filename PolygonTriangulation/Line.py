# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.04.15
__author__ = 'wnowak@idego.pl'

from PolygonTriangulation.Point import Point


class Line(object):
    """
    Class of line which consists of p1, p2
    """

    def __init__(self, p1=Point(0, 0), p2=Point(1, 1)):
        """
        >>> l = Line()
        >>> l.p1
        Point(0,0)
        >>> l.p2
        Point(1,1)
        """
        self.p1 = p1
        self.p2 = p2

    def dist(self):
        """
        >>> l = Line(p1=Point(), p2=Point(1,1))
        >>> l.dist()
        1.4142135623730951

        :return: Distance between p1 and p2
        """
        return self.p1.dist(self.p2)

    def __repr__(self):
        """
        >>> l = Line(p1=Point(), p2=Point(1,1))
        >>> l.__repr__()
        'Line(Point(0,0) <-> Point(1,1))'
        """
        return 'Line(%s <-> %s)' % (self.p1, self.p2)

    def equation(self):
        """
        >>> l = Line(p1=Point(), p2=Point(1,1))
        >>> l.equation()
        (1, 0)
        >>> l = Line(p1=Point(-1,1), p2=Point(0,0))
        >>> l.equation()
        (-1, 0)
        """
        if self.p1.x != self.p2.x:
            a = (self.p1.y - self.p2.y)/(self.p1.x - self.p2.x)
        else:
            a = 0
        b = self.p1.y - a * self.p1.x
        return a, b

    def intersects(self, line2, in_range=False):
        """
        >>> l1 = Line(p1=Point(-1,1), p2=Point(1,-1))
        >>> l2 = Line(p1=Point(-1,-1), p2=Point(1,1))
        >>> l1.intersects(l2)
        (True, 0)
        >>> l3 = Line(p1=Point(-1,-1), p2=Point(-1,-1))
        >>> l4 = Line(p1=Point(-2,-2), p2=Point(-2,-2))
        >>> l3.intersects(l4)
        (False, None)
        >>> l4 = Line(p1=Point(-1,2), p2=Point(-3,6))
        >>> l5 = Line(p1=Point(-1,2), p2=Point(-3,6))
        >>> l4.intersects(l5, in_range=True)
        True
        """
        a1, b1 = self.equation()
        a2, b2 = line2.equation()
        if not in_range:
            if a1 == a2 and b1 != b2:
                return False, None
            else:
                x = (b2-b1)/(a1-b2)
                return True, x
        else:
            if a1+a2 == 0:
                return False
            x = -(b2+b1)/(a1+a2)
            return (line2.p1.x <= x) and (x <= line2.p2.x)