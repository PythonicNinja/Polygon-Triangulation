# -*- coding: utf-8 -*-
from PolygonTriangulation.Point import Point
from PolygonTriangulation.SweepTriangulation import SweepTriangulation

__author__ = 'Wojciech Nowak'
__email__ = 'vojtek.nowak@gmail.com'
__version__ = '0.1.0'


if __name__ == '__main__':
    t = SweepTriangulation(points=[Point(-5,2), Point(-3,6), Point(-1,2), Point(1,3), Point(2,6), Point(3,4), Point(4,6), Point(5,1), Point(-1,1), Point(-2,0), Point(-4,0)])
    t.plot()