from bst_set import Set_Binary_Tree, keyvaluepair


def build_sample_tree():
    tree = Set_Binary_Tree()
    tree.build(
        [
            keyvaluepair(4, "a"),
            keyvaluepair(2, "b"),
            keyvaluepair(6, "c"),
            keyvaluepair(1, "d"),
            keyvaluepair(3, "e"),
            keyvaluepair(5, "f"),
            keyvaluepair(7, "g"),
        ]
    )
    return tree


def keys_in_order(tree):
    return [kv.key for kv in tree.iter_order()]


def test_build_and_min_max():
    print("=== Test: Build, min, max ===")
    tree = build_sample_tree()
    assert keys_in_order(tree) == [1, 2, 3, 4, 5, 6, 7]
    assert tree.find_min().key == 1
    assert tree.find_max().key == 7
    print("PASS: Build, min, max\n")


def test_find_and_neighbors():
    print("=== Test: find, next, prev ===")
    tree = build_sample_tree()
    assert tree.find(3).value == "e"
    assert tree.find_next(3).key == 4
    assert tree.find_prev(3).key == 2
    assert tree.find(100) is None
    assert tree.find_next(100) is None
    assert tree.find_prev(-1) is None
    print("PASS: find, next, prev\n")


def test_insert_and_delete():
    print("=== Test: insert and delete ===")
    tree = Set_Binary_Tree()
    assert tree.insert(keyvaluepair(10, "root")) is True
    assert keys_in_order(tree) == [10]
    assert len(tree) == 1

    assert tree.insert(keyvaluepair(5, "left")) is True
    assert tree.insert(keyvaluepair(15, "right")) is True
    assert keys_in_order(tree) == [5, 10, 15]
    assert len(tree) == 3

    removed = tree.delete(10)
    assert removed.key == 10
    assert keys_in_order(tree) == [5, 15]
    assert len(tree) == 2

    removed = tree.delete(5)
    assert removed.key == 5
    assert keys_in_order(tree) == [15]
    assert len(tree) == 1
    print("PASS: insert and delete\n")


def test_find_next_when_missing_key():
    print("=== Test: find_next for missing key ===")
    tree = build_sample_tree()
    assert tree.find_next(4).key == 5  # key exists, next is 5
    assert tree.find_next(4.5).key == 5  # missing key, returns next larger
    assert tree.find_next(7) is None  # no larger key
    print("PASS: find_next for missing key\n")


if __name__ == "__main__":
    test_build_and_min_max()
    test_find_and_neighbors()
    test_insert_and_delete()
    test_find_next_when_missing_key()
