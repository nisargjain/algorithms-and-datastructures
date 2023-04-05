class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def getlen(self):
        return self.len
    
    def geti(self, i):
        temp = self.head
        while(i>0):
            temp = temp.next
            i-=1
        return temp
            

    
    def printList(self):
        itr = self.head
        while(itr):
            print(itr.data, sep=" ", end="")
            itr = itr.next

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

/* nisarg */
if __name__=='__main__':
    arr = [1,2,3,4,5,6,7]
    linkd = linkedList()
    linkd.build(arr)
    linkd.printList()    
    print('length is: ', linkd.getlen())
    print("ith element is: " ,linkd.geti(5).data)