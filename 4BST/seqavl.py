from avl import Binary_Node
from bst import Binary_Tree

class Size_Node(Binary_Node):

    def subtree_update(A):
        super().subtree_update()
        A.size = 1            # here we created a size parameter on the go. HOW??
        if A.left: A.size += A.left.size
        if A.right: A.size += A.right.size
    
    def printTree(node, level=0):
        if node != None:
            if node.right is not None: node.right.printTree(level + 1)
            print(' ' * 4 * level + '-> ' + str(node.item))
            if node.left is not None:   node.left.printTree(level + 1)

    #the only function missing for sequence implementation
    def subtree_at(A, i):
        assert i >= 0
        if A.left: L_size  = A.left.size   #nL is notes
        else: L_size = 0

        if L_size<i: return A.right.subtree_at(i-L_size-1)
        elif L_size>i: return A.left.subtree_at(i)
        else: return A
    
class Seq_Binary_Tree(Binary_Tree):

    def __init__(self): super().__init__(Size_Node)   #using size node instead of default


    def build(self, X):   #this function does not call any insert delete function, so it also 
        #does not use MAINTAIN to rebalance BCOZ it does not need any REBALANCING. IT IS ALREADY 
        #BALANCED WHEN CREATING.
        def build_subtree(X, i, j):
            c = (i + j) // 2
            root = self.Node_Type(X[c])
            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root   
            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root
        
        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size


    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item
    
    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root: 
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1
    
    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        print('Before Deletion')
        self.root.printTree()
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        print('After Deletion')
        self.root.printTree()
        return ext.item

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)




#tests
if __name__=='__main__':
    
    '''
  Q1.  Make a Sequence AVL Tree or Set AVL Tree (Balanced Binary Search Tree) by inserting 
    student chosen items one by one. If any node becomes height-imbalanced, rebalance its ancestors 
    going up the tree. Here's a Sequence AVL Tree example that may be instructive (remember to 
    update subtree heights and sizes as you modify the tree!).
    '''
    
    
    # T = Seq_Binary_Tree()
    # T.build([10,6,8,5,1,3])
    # T.get_at(4)
    # T.set_at(4, -4)
    # T.insert_at(4, 18)
    # T.insert_at(4, 12)
    # T.delete_at(2)

    """
    Exercise: Maintain a sequence of n bits that supports two operations, each in O(log n) time: 
        • flip(i): flip the bit at index i
        • count ones upto(i): return the number of bits in the prefix up to index i that are one 
        
        Solution: Maintain a Sequence Tree storing the bits as items, augmenting each node A with 
        A.subtree ones, the number of 1 bits in its subtree. We can maintain this augmentation in 
        O(1) time from the augmentations stored at its children. 

        def one_update(A):
            A.subtree_ones = A.item
            if A.left:
                A.subtree_ones += A.left.subtree_ones
            if A.right:
                A.subtree_ones += A.right.subtree_ones
        
        To implement flip(i), find the ith node A using subtree node at(i)
        and flip the bit stored at A.item. Then update the augmentation at 
        A and every ancestor of A by walking up the tree in O(log n) time

        def flip(self, i):
            A = self.root.subtree_at(i)
            A.item = (A.item + 1)%2
            A.one_update()

        To implement count ones upto(i), we will first define the subtree-based 
        recursive function 'subtree_count_ones_upto(A, i)' which returns the 
        number of 1 bits in the subtree of node A that are at most index i 
        within A's subtree. Then count ones upto(i) is symantically equivailent 
        to subtree count ones upto(T.root, i). Since each recursive call makes at most 
        one recursive call on a child, operation takes O(log n) time. 
          
        def subtree_count_ones_upto(A,i):
            assert 0<=i<A.size:
            out = 0
            if A.left:
                if i < A.left.size:
                    return subtree_count_ones_upto(A.left, i)
                else:
                    out += A.left.subtree_ones
                    i-= A.left.size
            out += A.item
            if i>0:   #if still i is remaining after taking into account left subtree
                      # and self.item then we need to go to the right
                assert A.right
                out += subtree_count_ones_upto(A.right, i-1)
            return out
    """
