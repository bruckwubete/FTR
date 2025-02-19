# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def find_node(self, root, node, path_so_far):
        if root is None:
            return None
        elif root.val == node.val:
            path_so_far.append(root.val)
            return path_so_far

        left_path = self.find_node(root.left, node, path_so_far + [root.val])
        right_path = self.find_node(root.right, node, path_so_far + [root.val])

        return left_path if left_path else right_path

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_a = self.find_node(root, p, [])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.find_node(root, root.right.right, []))
