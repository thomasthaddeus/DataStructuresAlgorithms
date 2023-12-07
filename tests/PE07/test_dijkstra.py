"""Test for the Dijkstra class in PE07"""

import unittest
from dijkstra import DijkstraClass


class TestDijkstraClass(unittest.TestCase):
    """Test class for Dijkstra"""
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

    def test_shortest_path(self) -> None:
        """
        test_shortest_path _summary_

        _extended_summary_
        """
        dijkstra = DijkstraClass(self.graph)
        self.assertEqual(dijkstra.costs['D'], 4)
        self.assertEqual(dijkstra.parents['D'], 'C')

    def test_no_path(self) -> None:
        """
        test_no_path _summary_

        _extended_summary_
        """
        dijkstra = DijkstraClass(self.graph)
        self.assertNotIn('Z', dijkstra.costs)
        self.assertNotIn('Z', dijkstra.parents)

if __name__ == "__main__":
    unittest.main()
