# import numpy as np
# """
# # Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight
# """

# import numpy as np
# """
# # Definition for a QuadTree node.

# """
# # class Node:
# #     def __init__(self, val, isLeaf=1, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
# #         self.val = val
# #         self.isLeaf = isLeaf
# #         self.topLeft = topLeft
# #         self.topRight = topRight
# #         self.bottomLeft = bottomLeft
# #         self.bottomRight = bottomRight

# class Solution:
#     def construct(self, grid: List[List[int]]) -> 'Node':
#         grid = np.array(grid)
#         print(grid)
#         if len(grid) < 2:
#             print(grid)
#             grid = grid.tolist()
#             n = Node(grid[0][0], 1)
#             return n
#         elif len(grid) == 2 and len(grid[0]) == 2:
#             grid = grid.tolist()
#             n = Node(1, )
#             n.topLeft = Node(grid[0][0], 1)
#             n.topRight = Node(grid[0][1], 1)
#             n.bottomLeft = Node(grid[1][0], 1)
#             n.bottomRight = Node(grid[1][1], 1)
#         else:
#             c_i, c_j = (len(grid) // 2, len(grid[-1]) // 2)
#             n = Node(1)
#             n.topLeft = self.construct(grid[:c_i, :c_j])
#             n.topRight = self.construct(grid[:c_i, c_j:])
#             n.bottomLeft = self.construct(grid[c_i:, :c_j])
#             n.bottomRight = self.construct(grid[c_i:, c_j:])

#         if (n.topLeft.val == n.topRight.val == n.bottomLeft.val == n.bottomRight.val):
#             print('here')
#             n.isLeaf = 1
#             n.val = n.bottomRight.val
#             n.bottomRight = n.bottomLeft = n.topRight = n.topLeft = None
#         return n



# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.build(grid, 0, 0, len(grid))


    def sameValue(self, grid, x, y, sideLength):
        value = grid[x][y]
        for i in range(x, x + sideLength):
            for j in range(y, y + sideLength):
                if grid[i][j] != value:
                    return False

        return True


    def build(self, grid, x, y, sideLength):
        if self.sameValue(grid, x, y, sideLength):
            return Node(grid[x][y], True)

        root = Node(0, False)
        newSideLength = sideLength // 2
        root.topLeft = self.build(grid, x, y, newSideLength)
        root.topRight = self.build(grid, x, y + newSideLength, newSideLength)
        root.bottomLeft = self.build(grid, x + newSideLength, y, newSideLength)
        root.bottomRight = self.build(grid, x + newSideLength, y + newSideLength, newSideLength)

        return root