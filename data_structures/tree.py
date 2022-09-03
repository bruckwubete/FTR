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

    @staticmethod
    def _dig_right(node):
        if node.right_child is None:
            return node
        else:
            return BinarySearchTree._dig_right(node.right_child)

    def add(self, value: T):
        self.root = self._add(value, self.root)

    def contains(self, item):
        return self._contains(item, self.root)

    def remove(self, value: T):
        self._remove(value, self.root)

    def _add(self, value, node: TreeNode[T]) -> TreeNode[T]:
        if node is None:
            node = TreeNode(value)
        elif value >= node.value:
            node.right_child = self._add(value, node.right_child)
        else:
            node.left_child = self._add(value, node.left_child)
        return node

    def _remove(self, value: T, node: TreeNode[T]):
        if node is None:
            return None
        elif value > node.value:
            node.right_child = self._remove(value, node.right_child)
        elif value < node.value:
            node.left_child = self._remove(value, node.left_child)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                tmp_node = BinarySearchTree._dig_right(node.left_child)
                node.value = tmp_node.value
                node.left_child = self._remove(node.value, node.left_child)

        return node

    def _contains(self, item, node):
        if node is None:
            return False
        elif item == node.value:
            return True
        elif item < node.value:
            return self._contains(item, node.left_child)
        else:
            return self._contains(item, node.right_child)


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

    print("After removing 3", tree)
