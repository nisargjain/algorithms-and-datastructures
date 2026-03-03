from avl import Binary_Node, height

def is_avl_balanced(node):
    if node is None:
        return True
    lh = height(node.left)
    rh = height(node.right)
    if abs(lh - rh) > 1:
        return False
    return is_avl_balanced(node.left) and is_avl_balanced(node.right)

def test_right_chain():
    print("=== Test: Right-chain inserts ===")
    root = Binary_Node(10)
    for v in [20, 30, 40, 50]:
        root.subtree_insert_after(Binary_Node(v))
        root.printTree()
        print()
        assert is_avl_balanced(root)
    print("PASS: Right-chain inserts\n")

def test_left_chain():
    print("=== Test: Left-chain inserts ===")
    root = Binary_Node(50)
    for v in [40, 30, 20, 10]:
        root.subtree_insert_before(Binary_Node(v))
        root.printTree()
        print()
        assert is_avl_balanced(root)
    print("PASS: Left-chain inserts\n")

def test_mixed_inserts():
    print("=== Test: Mixed inserts ===")
    root = Binary_Node(30)
    for v in [10, 50, 20, 40, 60, 5, 25]:
        if v < root.item:
            root.subtree_insert_before(Binary_Node(v))
        else:
            root.subtree_insert_after(Binary_Node(v))
        root.printTree()
        print()
        assert is_avl_balanced(root)
    print("PASS: Mixed inserts\n")

def test_deletions():
    print("=== Test: Deletions ===")
    root = Binary_Node(30)
    for v in [10, 50, 20, 40, 60, 5, 25]:
        if v < root.item:
            root.subtree_insert_before(Binary_Node(v))
        else:
            root.subtree_insert_after(Binary_Node(v))
    root.printTree()
    print("Deleting 10, 50, 30 (root), 5")
    for v in [10, 50, 30, 5]:
        if root is None:
            break
        node = next((x for x in root.subtree_iter() if x.item == v), None)
        if node:
            node.subtree_delete()
            root = node.parent or root  # handle root replacement
            if root:
                root.printTree()
                print()
                assert is_avl_balanced(root)
    print("PASS: Deletions\n")

def test_successor_predecessor():
    print("=== Test: Successor/Predecessor ===")
    root = Binary_Node(20)
    for v in [10, 30, 5, 15, 25, 35]:
        if v < root.item:
            root.subtree_insert_before(Binary_Node(v))
        else:
            root.subtree_insert_after(Binary_Node(v))
    for node in root.subtree_iter():
        succ = node.successor()
        pred = node.predecessor()
        print(f"Node {node.item}: Successor = {succ.item if succ else None}, Predecessor = {pred.item if pred else None}")
    print("PASS: Successor/Predecessor\n")

def test_explicit_placement():
    print("=== Test: Explicit Placement ===")
    root = Binary_Node(10)
    n20 = Binary_Node(20)
    n30 = Binary_Node(30)
    n5 = Binary_Node(5)
    n15 = Binary_Node(15)

    root.subtree_insert_after(n20)
    assert n20 in list(root.subtree_iter())

    n20.subtree_insert_after(n30)
    assert n30 in list(root.subtree_iter())

    root.subtree_insert_before(n5)
    assert n5 in list(root.subtree_iter())

    n5.subtree_insert_after(n15)
    assert n15 in list(root.subtree_iter())

    # Verify parent pointers are non-broken
    for node in root.subtree_iter():
        if node.left:
            assert node.left.parent is node
        if node.right:
            assert node.right.parent is node

    root.printTree()
    print()
    assert is_avl_balanced(root)
    print("PASS: Explicit placement\n")

if __name__ == "__main__":
    test_right_chain()
    test_left_chain()
    test_mixed_inserts()
    test_deletions()
    test_successor_predecessor()
    test_explicit_placement()