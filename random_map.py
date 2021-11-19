# random_map.py
# 为了简化算法的描述:
# 我们选定左下角坐标[0, 0]的点是算法起点，右上角坐标[size - 1, size - 1]的点为要找的终点。
# 在地图的中间设置了一个障碍，并且地图中还会包含一些随机的障碍。
import numpy as np

import point

class RandomMap:
    """实现一个描述地图结构的类"""
    def __init__(self, size=50):
        """构造函数，地图的默认大小是50x50；
        设置障碍物的数量为地图大小除以8；
        调用GenerateObstacle生成随机障碍物；"""
        self.size = size
        self.obstacle = size//8
        self.GenerateObstacle()

    def GenerateObstacle(self):
        """在地图的中间生成一个斜着的障碍物；
        随机生成其他几个障碍物；
        障碍物的方向也是随机的；
        """
        self.obstacle_point = []
        self.obstacle_point.append(point.Point(self.size//2, self.size//2))
        self.obstacle_point.append(point.Point(self.size//2, self.size//2-1))


        # Generate an obstacle in the middle
        for i in range(self.size//2-4, self.size//2):
            self.obstacle_point.append(point.Point(i, self.size-i))
            self.obstacle_point.append(point.Point(i, self.size-i-1))
            self.obstacle_point.append(point.Point(self.size-i, i))
            self.obstacle_point.append(point.Point(self.size-i, i-1))

        for i in range(self.obstacle-1):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(point.Point(x, y))

            if (np.random.rand() > 0.5): # Random boolean
                for l in range(self.size//4):
                    self.obstacle_point.append(point.Point(x, y+l))
                    pass
            else:
                for l in range(self.size//4):
                    self.obstacle_point.append(point.Point(x+l, y))
                    pass

    def IsObstacle(self, i ,j):
        """定义一个方法来判断某个节点是否是障碍物；"""
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False