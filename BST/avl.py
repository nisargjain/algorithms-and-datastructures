'''
     _____<D>__       rotate_right(<D>)              __<B>_____
   __<B>__   <E>             =>                     <A>   __<D>__
 <A>   <C>   / \                                    / \  <C>   <E>
 / \   / \  /___\            <=                    /___\ / \   / \
/___\ /___\            rotate_left(<B>)                 /___\ /___\


'''



def subtree_rotate_right(node):
    assert node.left          #because we need that only to rotate right
    #creating pointers to important nodes
    #we will also exchange item values because otherwise we will need to change too many pointers.
    leftchild = node.left
    rightchild = node.right

    leftchild.parent = node.parent
    
    B.parent = D.parent
    D.parent = B
    D.left = B.right
    B.right = D
