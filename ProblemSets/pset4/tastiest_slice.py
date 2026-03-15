from numpy import argmax

from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.sum = 0
        self.prefix_sum = None
        self.max_prefix_key = None

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        neg_inf = float('-inf')
        k = None
        s = None
        if A:
            curr = A.item.val
            if A.left:
                l_pre = A.left.item.prefix_sum
                l_sum = A.left.item.sum
                l_key = A.left.item.max_prefix_key
            else : 
                l_pre, l_sum, l_key = neg_inf, 0, None
            if A.right:
                r_pre = A.right.item.prefix_sum
                r_sum = A.right.item.sum
                r_key = A.right.item.max_prefix_key
            else : 
                r_pre, r_sum, r_key = neg_inf, 0, None
            s = max(l_pre,l_sum+curr, l_sum + curr + r_pre)
            k = argmax([l_pre,l_sum+curr, l_sum + curr + r_pre])
            if k == 0:
                k = l_key
            elif k==1:
                k = A.item.key
            else: k = r_key

        A.item.max_prefix_key = k
        A.item.prefix_sum = s
        A.item.sum = l_sum + curr + r_sum
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        # YOUR CODE HERE #
        k = self.root.item.max_prefix_key
        s = self.root.item.prefix_sum
        ##################
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    sorted_list = sorted(toppings, key=lambda t: t[0])
    # print(sorted_list)
    for xi, yi, ti in sorted_list:
        B.insert(Key_Val_Item(yi, ti))
        ystar, tstar = B.max_prefix()
        if tstar>T:
            X,Y,T = xi, ystar,tstar
        # B.root.printTree()
    ##################
    return (X, Y, T)
