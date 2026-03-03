'''

Gal Ore is a scientist who studies climate. As part of her research, she often needs to query the 
maximum temperature the earth has observed within a particular date range in history, based on a 
growing set of measurements which she collects and adds to frequently. Assume that temperatures 
and dates are integers representing values at some consistent resolution. Help Gal evaluate such 
range queries efficiently by implementing a database supporting the following operations. 

record temp(t, d) |   record a measurement of temperature t on date d
max in range(d1,d2) | return max temperature observed between dates d1 and d2 inclusive


To solve this problem, we will store temperature mesurements in an AVL tree with binary search 
tree symantics keyed by date, where each node A stores a measurement 
A.item with a date property A.item.key and temperature property A.item.temp.


see notes


'''
import os, sys
# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
# Add 4BST directory to path
sys.path.append(os.path.join(parent_dir, '4BST'))
from set_avl import AVL_Set_Node, Set_AVL_Tree

class Measurement: ## basically a keyvaluepair but with more descriptive name and properties
    def __init__(self, temp, date): 
        self.key = date 
        self.temp = temp 
    def __str__(self): return "%s,%s" % (self.key, self.temp)


class Temperature_DB_Node(AVL_Set_Node):
    def __init__(A, temp, date):
        super().__init__(Measurement(temp, date))
        A.subtree_update()  # this will create max_temp, min_date and max_date attributes for the node
    def subtree_max_in_range(A, d1, d2):
        current_date = A.item.key
        if A.min_date > d2 or A.max_date < d1: return float('-inf')  #if the whole subtree is out of range, return -inf so it does not affect max
        elif A.min_date >= d1 and A.max_date <= d2: return A.max_temp  #if the whole subtree is in range, return max temp of subtree
        else:   #if the subtree is partially in range, we need to check the current node and both subtrees
            current_temp = A.item.temp if d1 <= current_date <= d2 else float('-inf')  #if current node is in range, consider its temp, else -inf
            left_max = A.left.subtree_max_in_range(d1, d2) if A.left else float('-inf')
            right_max = A.right.subtree_max_in_range(d1, d2) if A.right else float('-inf')
            return max(current_temp, left_max, right_max)
    
    def subtree_update(A):
        super().subtree_update()
        A.max_temp = max(A.item.temp, A.left.max_temp if A.left else A.item.temp, A.right.max_temp if A.right else A.item.temp)
        A.min_date  = min(A.item.key, A.left.min_date if A.left else A.item.key)
        A.max_date  = max(A.item.key, A.right.max_date if A.right else A.item.key)

class Temperature_DB(Set_AVL_Tree):
    def __init__(T):
        super().__init__(Temperature_DB_Node)
    
    def record_temp(T, t, d):
        new_node = T.Node_Type(t, d)
        if T.root:
            T.root.subtree_insert(new_node)
        else:
            T.root = new_node
            T.size = 1
    
    def max_in_range(T, d1, d2):
        if T.root:
            return T.root.subtree_max_in_range(d1, d2)
        else:
            return None

if __name__ == "__main__":
    db = Temperature_DB()
    db.record_temp(30, 1)
    db.record_temp(25, 2)
    db.record_temp(35, 3)
    db.record_temp(20, 4)
    
    print("=== Tree Structure ===")
    if db.root:
        db.root.printTree()
    else:
        print("Tree is empty!")
    
    print("\n=== Range Queries ===")
    print(f"max_in_range(1, 3) = {db.max_in_range(1, 3)}")  # should print 35
    print(f"max_in_range(2, 4) = {db.max_in_range(2, 4)}")  # should print 35
    print(f"max_in_range(1, 4) = {db.max_in_range(1, 4)}")  # should print 35
    print(f"max_in_range(5, 6) = {db.max_in_range(5, 6)}")  # should print None or -inf
