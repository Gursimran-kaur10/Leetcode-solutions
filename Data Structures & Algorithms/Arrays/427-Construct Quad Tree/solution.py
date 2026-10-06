"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        def solve(r,c,size):
            same=true

            for i in range(r,r+size):
                for j in range(c,c+size):
                    if grid[i][j]!=grid[r][c]:
                        same=False
                        break
            
            if same:
                return Node(grid[r][c]==1,True)
            #else we divide grid into 4 part then solve each part recursively creating leaf node
            half=size//2
            topLeft = solve(r, c, half)
            topRight = solve(r, c + half, half)
            bottomLeft = solve(r + half, c, half)
            bottomRight = solve(r + half, c + half, half)

            return Node(
                True,
                False, #as no leaf node
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return solve(0, 0, len(grid))
        
