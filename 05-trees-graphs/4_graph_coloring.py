# Graph coloring
# Given an undirected graph with maximum degree D, find a graph coloring using
# at most D+1 colors.

from typing import List
import unittest


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.color = None


class Graph:
    def __init__(self, n: int):
        self.nodes = [GraphNode(i) for i in range(n)]


def color_graph(G: Graph, colors: List[str]) -> None:
    """Color graph"""
    for n in G.nodes:
        if n in n.neighbors:
            raise Exception(f"No coloring possible, loop at {n.val}")

        # find illegal colors (neighbors')
        illegal = set(
            [neighbor.color for neighbor in n.neighbors if neighbor.color]
        )

        # assign first legal color
        for color in colors:
            if color not in illegal:
                n.color = color
                break


class TestGraphColoring(unittest.TestCase):
    def test_color_graph(self):
        pass


if __name__ == "__main__":
    unittest.main()
