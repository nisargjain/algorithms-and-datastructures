import unittest
from dfs import dfs, full_dfs

class TestDFS(unittest.TestCase):
    def test_dfs_simple(self):
        # Graph: 0 - 1 - 2
        Adj = [[1], [0,2], [1]]
        parent, order = dfs(Adj, 0)
        self.assertEqual(parent, [0, 0, 1])
        self.assertCountEqual(order, [2, 1, 0])

    def test_dfs_disconnected(self):
        # Graph: 0 - 1   2
        Adj = [[1], [0], []]
        parent, order = full_dfs(Adj)
        self.assertEqual(parent, [0, 0, 2])
        self.assertCountEqual(order, [1, 0, 2])

    def test_dfs_cycle(self):
        # Graph: 0 - 1 - 2 - 0 (cycle)
        Adj = [[1,2], [0,2], [1,0]]
        parent, order = dfs(Adj, 0)
        self.assertEqual(parent[0], 0)
        self.assertIn(1, parent)
        self.assertIn(2, parent)
        self.assertEqual(set(order), {0,1,2})

    def test_full_dfs_multiple_components(self):
        # Graph: 0-1  2-3
        Adj = [[1], [0], [3], [2]]
        parent, order = full_dfs(Adj)
        self.assertEqual(sorted(parent), [0,0,2,2])
        self.assertEqual(set(order), {0,1,2,3})

if __name__ == "__main__":
    unittest.main()
