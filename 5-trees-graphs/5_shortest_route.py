# MeshMessage
# Given information about active users on the network, find the shortest route
# for a message from one user (the sender) to another (the recipient). Return
# a list of users that make up this route.
#
# There might be a few shortest delivery routes, all with the same length. For
# now, let's just return any shortest route.
#
# Your network information takes the form of a dictionary mapping username
# strings to a list of other users nearby.
#
# EXAMPLE
# Input:  {
#     'Min'     : ['William', 'Jayden', 'Omar'],
#     'William' : ['Min', 'Noam'],
#     'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
#     'Ren'     : ['Jayden', 'Omar'],
#     'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
#     'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
#     'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
#     'Noam'    : ['Nathan', 'Jayden', 'William'],
#     'Omar'    : ['Ren', 'Min', 'Scott'],
#     ...
# }, 'Jayden', 'Adam'
#
# Output: ['Jayden', 'Amelia', 'Adam']

# BONUS
# 1. In our solution, we assumed that if one user (Min) could transmit a
# message to another (Jayden), then Jayden would also be able to transmit a
# message to Min. Suppose this wasn't guaranteed—maybe Min's cell phone
# transmits over shorter distances than Jayden's. How would our graph change to
# represent this? Could we still use BFS?
#
# 2. What if we wanted to find the shortest path? Assume we're given a GPS
# location for each user. How could we incorporate the distance between users
# into our graph? How would our algorithm change?
#
# 3. In our solution, we assumed that users never moved around. How could we
# extend our algorithm to handle the graph changing over time?

from collections import deque
from typing import Dict, List
import unittest


def shortest_route(G: Dict[str, List[str]], a: str, b: str) -> List[str]:
    """Find shortest route between a and b in undirected graph G"""
    prevnodes = {a: None}
    q = deque([a])
    while q:
        n = q.popleft()
        if n == b:
            return reconstruct_path(prevnodes, a, b)
        if n in G:
            for neighbor in G[n]:
                if neighbor not in prevnodes:
                    prevnodes[neighbor] = n
                    q.append(neighbor)
    return None


def reconstruct_path(prevnodes: Dict[str, str], a: str, b: str):
    n = b
    reversepath = []
    while n:
        reversepath.append(n)
        n = prevnodes[n]
    return list(reversed(reversepath))


class TestShortestRoute(unittest.TestCase):
    def test_shortest_route(self):
        users = {
            'Min': ['William', 'Jayden', 'Omar'],
            'William': ['Min', 'Noam'],
            'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
            'Ren': ['Jayden', 'Omar'],
            'Amelia': ['Jayden', 'Adam', 'Miguel'],
            'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
            'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
            'Noam': ['Nathan', 'Jayden', 'William'],
            'Omar': ['Ren', 'Min', 'Scott'],
            'Nathan': ['Miguel', 'Noam'],
            'Liam': ['Miguel'],
            'Lucas': ['Adam'],
            'Sofia': ['Adam']
        }
        tests = [
            ['Jayden', 'Adam', ['Jayden', 'Amelia', 'Adam']],
            ['Min', 'Adam', ['Min', 'Jayden', 'Amelia', 'Adam']],
            ['Adam', 'Ren', ['Adam', 'Amelia', 'Jayden', 'Ren']],
            ['Lucas', 'Lucas', ['Lucas']],
            ['Miguel', 'Nathan', ['Miguel', 'Nathan']]
        ]
        for a, b, path in tests:
            self.assertEqual(shortest_route(users, a, b), path)


if __name__ == "__main__":
    unittest.main()
