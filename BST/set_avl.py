from avl import Binary_Node
from bst_set import keyvaluepair

class AVL_Set_Node(Binary_Node):


    #finding a given key in our tree
    def subtree_find(A, k):
        if A.item.key > k:
            if A.left: return A.left.subtree_find(k)
        elif A.item.key < k:
            if A.right: return A.right.subtree_find(k)
        else: return A

        return None
    
    #finding next key to a given key, if given key does not exist then find the next smallest number
    # greater then given key.   #revisit this
    def subtree_find_next(A,k):
        
        if A.item.key <= k:
            if A.right: A.right.subtree_find_next(k)
            else: return None
        elif A.left:
            B= A.left.subtree_find_next(k)
            if B: return B
        return A
    
    def subtree_find_prev(A,k):
        
        if A.item.key >=k:
            if A.left: A.left.subtree_find_prev(k)
            else: return None

        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B: return B

        return A

    def subtree_insert(A,B):
        if B.item.key < A.item.key:
            if A.left:
                A.left.subtree_insert(B)
            else:
                B.parent = A
                A.left = B
                A.maintain()
        elif B.item.key > A.item.key:
            if A.right:
                A.right.subtree_insert(B)
            else:
                A.right = B
                B.parent = A
                A.maintain()
        else:   A.item = B.item



class Set_AVL_Tree(): # Binary AVL Search Tree

    def __init__(T, Node_Type = AVL_Set_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type
    
    def __len__(T): return T.size
    
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

    def iter_order(self): yield from iter(self)

    def build(self,X):
        for x in X: self.insert(x)

    def find_min(self):
        if self.root: return self.root.subtree_first().item

    def find_max(self):
        if self.root: return self.root.subtree_last().item

    
    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node: return node.item

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node: return node.item

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node: return node.item

    def insert(self, x):
        new_node = self.Node_Type(x)   #here nodetype Set AVL Node
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node
        self.size +=1 
        return True

    def delete(self,k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()   #called parent class function of binary node
        if ext.parent is None: self.root = None
        self.size -=1
        return ext.item


if __name__ == "__main__":
    tree = Set_AVL_Tree()
    tree.build([keyvaluepair(1,0), keyvaluepair(2,0),keyvaluepair(3,0),keyvaluepair(4,0), keyvaluepair(5,0), keyvaluepair(6,0) ])
    tree.root.printTree()
    for n in tree.iter_order():
        print(str(n.key) + " "+ str(n.value))