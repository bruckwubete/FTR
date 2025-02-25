# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:
        if len(arr) == 0:
            return None
        idx = len(arr) // 2
        root = TreeNode(arr[idx])
        root.left = self.sortedArrayToBST(arr[0:idx])
        root.right = self.sortedArrayToBST(arr[idx+1:])
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.sortedArrayToBST([-10,-3,0,5,9]))
    print(s.sortedArrayToBST([1,3]))