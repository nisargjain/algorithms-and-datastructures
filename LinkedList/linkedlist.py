class node:
    #initializes single node data structure of linked list
    def __init__(self, data):
        self.data = data
        self.next = None

    #returns the ith node next to first node. will follow the general 0 indexing convention like arrays
    def later_node(self, i):
        if i == 0 : return self
        assert self.next
        return self.next.later_node(i-1)

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def getheadandtails(self):
        print(self.head.data)
        print(self.tail.data)

    def getlen(self):
        return self.len
    
    #or you can use the later_node function for this
    def geti(self, i):
        temp = self.head
        while(i>0):
            temp = temp.next
            i-=1
        return temp
        
    def set_at(self, i, x):
        temp = self.head.later_node(i)
        temp.data = x

    def insert_first(self,x):
        temp = node(x)
        temp.next = self.head
        self.head = temp
        self.len += 1    

    def insert_at(self,i ,x):
        if i==0:
            self.insert_first(x)
            return
        temp = node(x)
        previousnode = self.geti(i-1)
        temp.next = previousnode.next
        previousnode.next = temp
        self.len+=1

    def delete_at(self, i):
        if i==0:
            x = self.delete_first()
            return x
        previousnode = self.geti(i-1)
        x = previousnode.next.data
        previousnode.next = previousnode.next.next
        self.len -= 1
        return x

    def delete_first(self):
        x = self.head.data
        self.head = self.head.next
        self.len -= 1
        return x
    
    def delete_last(self):    #O(n) no matter what you do it will stay like this only. 
        return self.delete_at(self.len -1 )
    
    def insert_last(self, x): #O(1) because we kept tail pointer
        temp = node(x)
        self.tail.next = temp
        self.tail = temp
        self.len += 1

    def printList(self):
        itr = self.head
        while(itr):
            print(itr.data, end=" ")
            itr = itr.next
        print()
        

    def build(self, arr):
        for data in arr:
            if(not self.head):
                self.head = node(data)
                self.len += 1
                self.tail = self.head
                continue
            self.tail.next = node(data)
            self.tail = self.tail.next
            self.len += 1

    def reorder_students(self):   #reverses the second half of the linked list
        n = self.len // 2 # find the n-th node
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
    linkd = linkedList()
    linkd.build(arr)
    # linkd.printList()    
    # print('length is: ', linkd.getlen())
    # print("ith element is: " ,linkd.geti(5).data)
    # print('ith node data is: ', linkd.head.later_node(5).data)
    # linkd.insert_first(0)
    # linkd.printList()
    # linkd.getheadandtails()
    # linkd.delete_first()
    # print(linkd.getlen())
    linkd.reorder_students()
    linkd.printList()


