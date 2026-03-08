class PriorityQueue:
    def __init__(self):
        self.A = []

    def insert(self, x):
        self.A.append(x)


    ## just a template anyways will be replaced by own method
    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        return self.A.pop()

    @classmethod
    def sort(cls, A):
        pq = cls()
        for x in A:
            pq.insert(x)

        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out