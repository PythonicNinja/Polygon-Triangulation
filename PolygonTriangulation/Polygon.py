# -*- coding: utf-8 -*-
# CREATED ON DATE: 06.04.15

from Line import Line
from Point import Point

__author__ = 'vojtek.nowak@gmail.com'


class Polygon(object):
    """
    Polygon class
    """

    def __init__(self, points):
        """
        >>> p = Polygon(points=[Point(), Point(1,1), Point(2,2)])
        """
        self.points = points
        self.lines = []

        for i, point in enumerate(self.points):
            try:
                self.lines.append(Line(point, self.points[i+1]))
            except IndexError:
                self.lines.append(Line(point, self.points[0]))

    def __repr__(self):
        """
        >>> p=Polygon(points=[Point(), Point(1,1), Point(2,2)])
        >>> p.__repr__()
        'Polygon({Line(Point(0,0) <-> Point(1,1)), Line(Point(1,1) <-> Point(2,2)), Line(Point(2,2) <-> Point(0,0))})'
        """
        return 'Polygon({%s})' % ", ".join(str(line) for line in self.lines)