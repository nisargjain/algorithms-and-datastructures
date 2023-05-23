import bst

class BST_set(bst.Binary_Node()):

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
        elif B.item.key > A.item.key:
            if A.right:
                A.right.subtree_insert(B)
            else:
                A.right = B
                B.parent = A
        else:   A.item = B.item



class Set_Binary_Tree(bst.Binary_Tree): # Binary Search Tree

    #initializing parent class initializer
    def __init__(self): super().__init__(bst.Binary_Node)

    def iter_order(self): yield from self.__iter__()
    
    def build(self,X):
        for x in X: self.subtree_insert(x)

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
        new_node = self.Node_Type(x)   #here nodetype is binary node
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

