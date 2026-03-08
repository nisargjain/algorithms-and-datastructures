class PriorityQueue:
    def __init__(self, A):
        self.A = A
        self.n= 0 

    def insert(self):
        if not self.n < len(self.A):
            raise IndexError('insert into full priority queue')
        self.n += 1

    def delete_max(self):
        if self.n < 1:
            raise IndexError('pop from empty priority queue')
        self.n -= 1  ### not correct on its own

    @classmethod
    def sort(Queue, A):
        pq = Queue(A)
        for _ in range(len(A)):
            pq.insert()
        for _ in range(len(A)):
            pq.delete_max()
        return pq.A