import unittest
from array_seq import Array_Seq
from dynamic_array_seq import Dynamic_Array_Seq

class TestDynamicArraySeq(unittest.TestCase):
    
    def test_insert_last_and_len(self):
        arr = Dynamic_Array_Seq()
        self.assertEqual(len(arr), 0)
        arr.insert_last(10)
        self.assertEqual(len(arr), 1)
        self.assertEqual(arr.A[0], 10)
    
    def test_delete_last(self):
        arr = Dynamic_Array_Seq()
        arr.insert_last(1)
        arr.insert_last(2)
        arr.insert_last(3)
        self.assertEqual(len(arr), 3)
        arr.delete_last()
        self.assertEqual(len(arr), 2)
        self.assertEqual(arr.A[1], 2)  # 3 is removed

    def test_insert_at_middle(self):
        arr = Dynamic_Array_Seq()
        arr.insert_last(1)
        arr.insert_last(3)
        arr.insert_at(1, 2)
        self.assertEqual([x for x in arr], [1, 2, 3])

    def test_insert_first_and_delete_first(self):
        arr = Dynamic_Array_Seq()
        arr.insert_first(10)
        arr.insert_first(20)
        self.assertEqual([x for x in arr], [20, 10])
        val = arr.delete_first()
        self.assertEqual(val, 20)
        self.assertEqual([x for x in arr], [10])

    def test_delete_at(self):
        arr = Dynamic_Array_Seq()
        for i in range(5):
            arr.insert_last(i)  # [0, 1, 2, 3, 4]
        removed = arr.delete_at(2)
        self.assertEqual(removed, 2)
        self.assertEqual([x for x in arr], [0, 1, 3, 4])
    
    def test_resize_behavior(self):
        arr = Dynamic_Array_Seq(r=2)
        for i in range(100):
            arr.insert_last(i)
        self.assertEqual(len(arr), 100)
        for _ in range(90):
            arr.delete_last()
        self.assertEqual(len(arr), 10)

    def test_iterator(self):
        arr = Dynamic_Array_Seq()
        for i in range(5):
            arr.insert_last(i)
        self.assertEqual(list(iter(arr)), [0, 1, 2, 3, 4])

    def test_insert_delete_mix(self):
        arr = Dynamic_Array_Seq()
        for i in range(10): arr.insert_last(i)
        self.assertEqual(len(arr), 10)
        for _ in range(5): arr.delete_first()
        self.assertEqual([x for x in arr], [5, 6, 7, 8, 9])
        arr.insert_first(100)
        self.assertEqual([x for x in arr], [100, 5, 6, 7, 8, 9])

    def test_edge_empty_deletes(self):
        arr = Dynamic_Array_Seq()
        with self.assertRaises(IndexError):
            arr.delete_last()  # Will raise IndexError if not handled
        with self.assertRaises(IndexError):
            arr.delete_first()
        with self.assertRaises(IndexError):
            arr.delete_at(0)

if __name__ == "__main__":
    unittest.main()
