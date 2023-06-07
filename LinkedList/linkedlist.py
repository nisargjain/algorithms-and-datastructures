class Linked_List_Node:
    #initializes single node data structure of linked list
    def __init__(self, data):
        self.item = data
        self.next = None

    #returns the ith node next to first node. will follow the general 0 indexing convention like arrays
    def later_node(self, i):
        if i == 0 : return self
        assert self.next
        return self.next.later_node(i-1)

class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getheadandtails(self):
        print("head data is: " , self.head.item, end = ' ____ ')
        print("tails data is : " , self.tail.item)

    def __len__(self): return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a)
            if self.tail is None:
                self.tail = self.head

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item
        
    def set_at(self, i, x):
        temp = self.head.later_node(i)
        temp.data = x

    def insert_first(self,x):
        temp = Linked_List_Node(x)
        temp.next = self.head
        self.head = temp
        self.size += 1    

    def delete_first(self):
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self,i ,x):
        if i==0:
            self.insert_first(x)
            return
        
        if i==len(self)-1:
            self.insert_last(x)
            return 
        
        temp = Linked_List_Node(x)
        previousnode = self.head.later_node(i-1)
        temp.next = previousnode.next
        previousnode.next = temp

        while(self.tail.next):
            self.tail = self.tail.next

        self.size += 1

    def delete_at(self, i):
        if i==0:
            return self.delete_first()
        previousnode = self.later_node(i-1)
        x = previousnode.next.item
        previousnode.next = previousnode.next.next
        if (i == len(self)-1):
            self.tail = previousnode
        self.size -= 1
        return x

    def delete_last(self):    #O(n) no matter what you do it will stay like this only. 
        return self.delete_at(len(self) - 1)
    
    def insert_last(self, x): #O(1) because we kept tail pointer
        temp = Linked_List_Node(x)
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def printList(self):
        itr = self.head
        while(itr):
            print(itr.item, end=" ")
            itr = itr.next
        print()

    def reorder_students(self):   #reverses the second half of the linked list
        n = len(self) // 2 # find the n-th node
        a = self.head
        if not a or not a.next:
            return a
        for _ in range(n - 1):
            a = a.next
        b = a.next # relink next pointers of last half
        c = a.next.next
        while(c):
            temp = c.next
            c.next  = b
            b = c
            c = temp
        a.next.next = None
        a.next = b

        return    


if __name__=='__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    linkd = Linked_List_Seq()
    linkd.build(arr)
    # linkd.printList()    
    # print('length is: ', len(linkd))
    # print("ith element is: " ,linkd.get_at(5))
    # linkd.insert_first(0)
    # linkd.printList()
    # linkd.getheadandtails()
    # linkd.delete_first()
    # print("length now after delete is: ", len(linkd))
    # linkd.printList()
    # linkd.reorder_students()
    linkd.printList()