# point.py
import sys

class Point:
    """创建一个非常简单的类来描述图中的点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = sys.maxsize