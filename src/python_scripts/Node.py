from typing import List


class Node:
    def __init__(self, id: int, x: float, y: float, neighbors: List[int]):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = neighbors
