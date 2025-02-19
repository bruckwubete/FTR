from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        left_valid = True
        if root.left:
            left_valid = root.left.val < root.val and self.isValidBST(root.left)
        right_valid = True
        if root.right:
            right_valid = root.right.val > root.val and self.isValidBST(root.right)
        return left_valid and right_valid

if __name__ == '__main__':
    answer = Solution().isValidBST()