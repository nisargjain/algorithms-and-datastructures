
#defining binary tree with avl balancing
##is defined as a free function so it can 
# safely handle None without needing an object,
#  and to avoid repeating if node is None:

def height(A): 
    if A: return A.height
    else: return -1

class Binary_Node:
    
    def __init__(A,x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None 
        A.subtree_update()  
        ## this actually created height attribute at first time, so we can use it in height function

    def subtree_update(A):
        A.height = 1 + max(height(A.left), height(A.right))

    def skew(A):            #O(1)
        return height(A.right) - height(A.left)
    
    def printTree(self, level=0):
        if self != None:
            if self.right is not None: self.right.printTree(level + 1)
            print(' ' * 4 * level + '-> ' + str(self.item))
            if self.left is not None:   self.left.printTree(level + 1)

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left: return A.left.subtree_first()
        else: return A

    def subtree_last(A): # O(log n)
        if A.right: return A.right.subtree_last()
        else: return A

    def successor(A):
        if A.right: return A.right.subtree_first()
        else: 
            while A.parent and (A is A.parent.right):
                A = A.parent
            return A.parent
    
    def predecessor(A):
        if A.left: return A.left.subtree_last()
        else:
            while A.parent and (A is A.parent.left):
                A = A.parent
            return A.parent
        
    def subtree_insert_before(A, B): # O(log n)
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        A.maintain()

    def subtree_insert_after(A, B): # O(log n)
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        A.maintain()

    def subtree_delete(A): #O(log n)
        if A.left or A.right:
            if A.left:
                B = A.predecessor()
            else: B= A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()

        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
            A.parent.maintain()
        return A
    

        #Now the rotation part
        '''
               _____<D>__       rotate_right(<D>)              __<B>_____
           __<B>__   <E>             =>                     <A>   __<D>__
           <A>   <C>   / \                                    / \  <C>   <E>
           / \   / \  /___\            <=                    /___\ / \   / \
          /___\ /___\            rotate_left(<B>)                 /___\ /___\
       
        '''    


    def subtree_rotate_right(D):

        assert D.left          #because we need that only to rotate right
        #creating pointers to important nodes
        #we will also exchange item values because otherwise we will need to change too many pointers.
        B, E = D.left, D.right
        A, C = B.left, B.right
        D.item, B.item = B.item, D.item  #doing this to prevent checking and changing parent pointers of D
        D,B = B,D                      #changing pointers to correctly represent
        '''
                _____<B>__                                  __<B>_____                                
            __<D>__    <E>                               <A>   __<D>__              
            <A>   <C>   / \            to make            / \  <C>   <E>                                    
            / \   / \  /___\                             /___\ / \   / \             
            /___\ /___\                                        /___\ /___\        

        '''
        B.left, D.left = A,C
        B.right, D.right = D,E       #note that E and A and C might be NULL here
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()


    def subtree_rotate_left(B):
        assert B.right          #because we need that only to rotate left
        #creating pointers to important nodes
        #we will also exchange item values because otherwise we will need to change too many pointers.
        D, A = B.right, B.left
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B,E
        B.left, B.right = A,C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    #function to balance the skew
    #remember the 3 cases from notes
    def rebalance(A):
        if A.skew() == 2:
            if A.right.skew() < 0:  #meaning -1
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()   #will handle the case of skew = 0 or 1 automatically
        elif A.skew() == -2:
            if A.left.skew()>0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

    #maintain function to call for every augment change
    def maintain(A):            # O(log n)
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()


if __name__ == "__main__":
    print("=== right-chain inserts ===")
    root = Binary_Node(10)
    root.printTree()
    print("=======================================")
    root.subtree_insert_after(Binary_Node(20))
    root.printTree()
    print("=======================================")
    root.right.subtree_insert_after(Binary_Node(30))
    root.printTree()
    print("=======================================")
    root.right.subtree_insert_after(Binary_Node(40))
    root.printTree()
    print("=======================================")
    root.right.right.subtree_insert_after(Binary_Node(50))
    root.printTree()
    print("=======================================\n")

    print("=== insert before/after ===")
    root2 = Binary_Node(15)
    root2.subtree_insert_before(Binary_Node(5))
    root2.subtree_insert_after(Binary_Node(25))
    root2.printTree()
    print("successor of 15:", root2.successor().item)
    print("predecessor of 15:", root2.predecessor().item)
    print("first:", root2.subtree_first().item, "last:", root2.subtree_last().item)
    print("=======================================\n")

    print("=== delete leaf then root ===")
    root3 = Binary_Node(10)
    root3.subtree_insert_before(Binary_Node(5))
    root3.subtree_insert_after(Binary_Node(20))
    root3.printTree()
    print("delete leaf (right)")
    root3.right.subtree_delete()
    root3.printTree()
    print("delete current root")
    root3.subtree_delete()
    root3.printTree()
    print("=======================================\n")

    print("=== direct rotate left then right ===")
    rot = Binary_Node(10)
    rot.right = Binary_Node(20); rot.right.parent = rot
    rot.right.right = Binary_Node(30); rot.right.right.parent = rot.right
    rot.subtree_update()
    print("before rotate_left:")
    rot.printTree()
    rot.subtree_rotate_left()
    print("after rotate_left:")
    rot.printTree()
    rot2 = Binary_Node(20)
    rot2.left = Binary_Node(10); rot2.left.parent = rot2
    rot2.left.left = Binary_Node(5); rot2.left.left.parent = rot2.left
    rot2.subtree_update()
    print("before rotate_right:")
    rot2.printTree()
    rot2.subtree_rotate_right()
    print("after rotate_right:")
    rot2.printTree()
    print("=======================================\n")

    print("=== height and skew checks ===")
    node = Binary_Node(1)
    print("height(None):", height(None))
    print("height(node):", height(node))
    print("skew(node):", node.skew())
    node.subtree_insert_after(Binary_Node(2))
    print("after insert, height(node):", height(node), "skew(node):", node.skew())
    print("=======================================\n")