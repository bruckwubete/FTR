from __future__ import annotations
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class GraphNode(Generic[T]):
    def __init__(self, value: T, left_child: Optional[GraphNode] = None, right_child: Optional[GraphNode] = None) -> None:
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


class Graph(Generic[T]):
    def __init__(self, root: Optional[GraphNode[T]] = None) -> None:
        self.root = root

