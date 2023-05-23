class Binary_Node:
    def __init__(A, x): # O(1)
        A.item = x
        A.left = None
        A.right = None
        A.parent = None

    def subtree_iter(self):
        if self.left: yield from self.left.subtree_iter()
        yield self
        if self.right: yield from self.right.subtree_iter()

    #return first node in traversal order 
    def subtree_first(A):
        if A.left: return A.left.subtree_first()
        else: return A

    #return last node in traversal order
    def subtree_last(A):
        if A.right: return A.right.subtree_last()
        else: return A

    #find the next node in inorder traversal order known as a successor
    def successor(A):
        if A.right: return A.right.subtree_first()
        
        #else if right node does not exist, then it might be child of some parent.
        #but we need a parent whose left child is ancestor of this node, so that in 
        # traversal next node will this parent. [a parent whose right child is this node 
        # cannot be successor]
        while A.parent and (A.parent.right is A):
            A = A.parent
        return A.parent
    
    def predeccessor(A):        #similar to successor 
        if A.left: return A.left.subtree_last()

        while A.parent and (A.parent.left is A):
            A = A.parent
        
        return A.parent
    

    def subtree_insert_before(A, B):  #insert node B before A

        if  A.left:
            A = A.left.subtree_last()
            A.left, B.parent = B, A
        else:
            A.left, B.parent = B, A

    def subtree_insert_after(A, B): #insert node B after A

        if A.right:
            A = A.right.subtree_first()
            A.right, B.parent    =   B, A

        else:
            A.right, B.parent = B, A

    def subtree_delete(A):

        #if A is not a leaf node
        if A.left or A.right:
            if A.left:
                temp = A.predeccessor()
            else:
                temp = A.successor()
            temp.item, A.item = A.item, temp.item
            return temp.subtree_delete()

        if A.parent:
            if A.parent.left is A:
                A.parent.left = None
            else: A.parent.right = None
        return A
    

class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type
    
    def __len__(T): return T.size
    
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item





'''
Exercise 1. Given an array of items A = (a0, . . . , an-1), 
describe a O(n)-time algorithm to construct a binary tree T 
containing the items in A such that:
(1) the item stored in the ith node of T's traversal order is item a_i
(2) T has height O(log n). 

Sol 1. Store middle of array as root and build recursively.

    def build(A):
        def build_subtree(A, i, j):
            middle = i+j//2
            root = Binary_Node(A[middle])
            if i<middle:
                root.left = build_subtree(A, i, middle-1)
                root.left.parent = root 
            if middle<j:
                root.right = build_subtree(A, middle+1, j)
                root.right.parent = root
            return root
        self.root = build_subtree(A, 0, len(A)-1)



'''