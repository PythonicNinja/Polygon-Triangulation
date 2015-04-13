# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.04.15

from Point import Point
from Line import Line
from Polygon import Polygon


class SweepTriangulation(object):
    """
    Algorithm of Polygon Sweep Triangulation
    """

    def __init__(self, points, *args, **kwargs):
        """
        >>> t = SweepTriangulation(points = [Point(0,0), Point(1,1), Point(2,2), Point(3,3), Point(1,4)])
        >>> t.points[0]
        Point(0,0)
        >>> t.points[-1]
        Point(3,3)
        """
        self.polygon = Polygon(points)
        self.points = sorted(points, key=lambda key: key.x)

    def __repr__(self):
        """
        >>> t = SweepTriangulation(points = [Point(0,0), Point(1,1), Point(2,2), Point(3,3), Point(1,4)])
        >>> t.__repr__()
        'SweepTriangulation(Points=[Point(0,0), Point(1,1), Point(1,4), Point(2,2), Point(3,3)])'

        """
        return 'SweepTriangulation(Points=[%s])' % (", ".join(str(p) for p in self.points))

    @classmethod
    def same_chain(cls, point_cmp, found_point):
        """
        >>> SweepTriangulation.same_chain(Point(0,0), Point(1,1))
        True
        >>> SweepTriangulation.same_chain(Point(1,1), Point(0,0))
        False
        """
        angle = point_cmp.angle(found_point)
        if 0 <= angle <= 180:
            return True
        else:
            return False

    def triangulation(self):
        """
        >>> t = SweepTriangulation(points=[Point(-5,2), Point(-3,6), Point(-1,2), Point(1,3), Point(2,6), Point(3,4), Point(4,6), Point(5,1), Point(-1,1), Point(-2,0), Point(-4,0)])
        >>> t.triangulation()
        """
        lines = []

        stack = [self.points[0], self.points[1]]
        # print stack
        for i, vi in enumerate(self.points[2:-1]):
            # print vi
            if not SweepTriangulation.same_chain(vi, stack[-1]):
                vk = stack[-1]
                while len(stack) != 1:
                    item = stack.pop()
                    if not Line(vi, item).intersects(Line(self.points[i], vk), in_range=True):
                        # print '1: ', vi, item, vi, vk
                        lines.append(Line(vi, item))
                stack.pop()

                stack.append(vk)
                stack.append(vi)
            else:
                vk = stack.pop()
                vj = None
                for j, vj in enumerate(stack):
                    if not Line(vj, vi).intersects(Line(vj, stack[-1]), in_range=True):
                        # print '2: ', vj, vi, vj, vk
                        lines.append(Line(vi, vj))
                    vj = stack.pop()

                if vj:
                    stack.append(vj)
                stack.append(vi)

        for i, item in enumerate(stack):
            if i != 0 or i != len(stack):
                lines.append(Line(self.points[-1], item))
        return lines

