from pq_inplace import PriorityQueue

def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i

def max_heapify_up(A, n, c):
    p = parent(c)
    if A[p] < A[c]:
        A[c], A[p] = A[p], A[c]
        max_heapify_up(A, n, p)
    else: return

def max_heapify_down(A, n, p):
    l = left(p, n)
    r = right(p, n)
    c  = l if A[l] > A[r] else r
    if A[p] < A[c]:
        A[p], A[c] = A[c], A[p]
        max_heapify_down(A, n, c)

class PQ_Heap(PriorityQueue):

    def insert(self,*args):
        super().insert(*args)
        n,A = self.n, self.A
        max_heapify_up(A, n, n-1)

    def delete_max(self):
        n,A = self.n, self.A
        A[n-1], A[0] = A[0], A[n-1]
        max_heapify_down(A, n-1, 0)
        return super().delete_max()


def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, -1, -1):
        max_heapify_down(A, n, i)


if __name__ == "__main__":

    A = [7, 3, 5, 6, 2, 0, 3, 1]
    build_max_heap(A)
    print(A)
    print("PriorityQueue sort:", PriorityQueue.sort(A))
    print("Heap PQ sort:", PQ_Heap.sort(A))