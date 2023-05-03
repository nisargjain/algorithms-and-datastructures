class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        nd = Doubly_Linked_List_Node(x)
        if self.head:
            nd.next = self.head
            self.head.prev = nd
            self.head = nd
        else:
            self.head = nd
            self.tail = nd

        

    def insert_last(self, x):
        nd = Doubly_Linked_List_Node(x)
        if self.tail:
            self.tail.next = nd
            nd.prev = self.tail
            self.tail = nd
        else:
            self.head = nd
            self.tail = nd

    def delete_first(self):
        if self.head:
            temp = self.head
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
                temp.next = None
                return temp.item
            self.head = None
            self.tail = None
            return temp.item    
        return None
        

    def delete_last(self):
        if self.tail:
            temp = self.tail
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next= None
                temp.prev = None
                return temp.item
            self.head = None
            self.tail = None
            return temp.item
        return None

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2 
        x1.prev.next = x2.next
        x2.next.prev = x1
        L2.head.prev = None
        L2.tail.next = None
        return L2

    def splice(self, x, L2):
        temp = x.next
        x.next = L2.head
        temp.prev = L2.tail
        L2.head.prev = x
        L2.tail.next = temp

