# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.04.15

import matplotlib.pyplot as plt

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
        self.unsorted_points = points
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
        >>> SweepTriangulation.same_chain(Point(0,0,1), Point(1,1,1))
        True
        >>> SweepTriangulation.same_chain(Point(1,1,1), Point(0,0,0))
        False
        """
        return point_cmp.orientation == found_point.orientation

    def triangulation(self):
        """
        >>> t = SweepTriangulation(points=[Point(-5,2), Point(-3,6), Point(-1,2), Point(1,3), Point(2,6), Point(3,4), Point(4,6), Point(5,1), Point(-1,1), Point(-2,0), Point(-4,0)])
        >>> t.triangulation()
        [Line(Point(-3,6) <-> Point(-4,0)), Line(Point(-1,2) <-> Point(-2,0)), Line(Point(1,3) <-> Point(-1,1)), Line(Point(2,6) <-> Point(1,3)), Line(Point(3,4) <-> Point(1,3)), Line(Point(4,6) <-> Point(3,4)), Line(Point(4,6) <-> Point(1,3)), Line(Point(5,1) <-> Point(3,4)), Line(Point(5,1) <-> Point(4,6))]
        """
        lines = []

        stack = [self.points[0], self.points[1]]
        # print stack
        for i, vi in enumerate(self.points[2:-1]):
            # print vi
            if not SweepTriangulation.same_chain(vi, stack[-1]):
                vk = stack[-1]
                while len(stack) != 0:
                    item = stack.pop()
                    lines.append(Line(vi, item, color='y'))

                stack.append(vk)
                stack.append(vi)
            else:
                vk = stack.pop()
                while len(stack) != 0:
                    vj = stack.pop()
                    if 0 <= vj.angle_tree_points(vk, vi) <= 180:
                        lines.append(Line(vi, vj, color='b'))
                    else:
                        break

                stack.append(vj)
                stack.append(vi)

        vn = self.points[i+2+1]
        for i, item in enumerate(stack):
            if i not in [0, len(stack)]:
                lines.append(Line(vn, item, color='g'))
        return lines

    def plot(self):
        '''
        plots graph of triangulation
        '''

        lines = self.triangulation()

        x_s, y_s = [point.x for point in self.unsorted_points], [point.y for point in self.unsorted_points]
        additional = 0
        while self.unsorted_points[0].x != x_s[-1]:
            point = self.unsorted_points[additional]
            x_s.append(point.x)
            y_s.append(point.y)
            additional += 1

        plt.plot(x_s, y_s, marker='o', linestyle='-', color='r', label='Points')

        for line in lines:
            plt.plot([line.p1.x, line.p2.x], [line.p1.y, line.p2.y], linestyle='-', color=line.color)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Triangulation')
        plt.legend()
        plt.show()
