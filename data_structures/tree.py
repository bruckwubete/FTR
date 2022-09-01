from __future__ import annotations
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: T, left_child: Optional[TreeNode] = None, right_child: Optional[TreeNode] = None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        if self.right_child is not None:
            ret += self.right_child.__str__(level + 1)
        if self.left_child is not None:
            ret += self.left_child.__str__(level + 1)

        return ret


class Tree(Generic[T]):
    def __init__(self, root: Optional[TreeNode[T]] = None) -> None:
        self.root = root

    def __str__(self, level=0):
        if self.root is not None:
            ret = self.root.__str__(level)
            return ret


class BinarySearchTree(Tree[T]):
    def _add(self, value, node: TreeNode[T]):
        if node is None:
            return TreeNode(value)
        elif value >= node.value:
            node.right_child = self._add(value, node.right_child)
        else:
            node.left_child = self._add(value, node.left_child)
        return node

    def add(self, value: T):
        self.root = self._add(value, self.root)

    def _find(self, value: T, node: TreeNode[T], parent: Optional[TreeNode[T]] = None, child_link: str = None):
        if node is None:
            return None, None, None
        else:
            if node.value == value:
                return node, parent, child_link
            elif node.value > value:
                return self._find(value, node.left_child, node, 'left')
            else:
                return self._find(value, node.right_child, node, 'right')

    @staticmethod
    def _dig_right(node):
        if node.right_child is None:
            return node
        else:
            return BinarySearchTree._dig_right(node.right_child)

    def remove(self, value: T):
        node, parent, link = self._find(value, self.root, None)
        if node is None:
            print(f'Node with value {value} not found!')
        else:
            # print(f'Found Node {node} with parent {parent} link {link}')
            if node.left_child and node.right_child is None:
                if parent is None:
                    self.root = node.left_child
                else:
                    if link == 'left':
                        parent.left_child = node.left_child
                    else:
                        parent.right_child = node.left_child
            elif node.right_child and node.left_child is None:
                if parent is None:
                    self.root = node.right_child
                else:
                    if link == 'left':
                        parent.left_child = node.right_child
                    else:
                        parent.right_child = node.right_child
            elif node.right_child is None and node.left_child is None:
                if link == 'left':
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                # both left and right exist
                n = BinarySearchTree._dig_right(node.left_child)
                n.right_child = node.right_child
                self.remove(n.value)
                if link == 'left':
                    parent.left_child = n
                else:
                    parent.right_child = n


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(3)
    tree.add(0)
    tree.add(-1)
    tree.add(14)
    tree.add(2)
    tree.add(4)
    tree.add(50)
    print(tree)

    tree.remove(3)
    print(tree)
