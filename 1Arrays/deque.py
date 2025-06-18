class Deque_Array_Seq:
# Implements a double-ended queue (deque) using a dynamic array sequence.
    def __init__(self):
        self.A = [None]
        self.size = 0
        self.start = 0
        self._resize(0)

    def build(self, X):
        """ 
        Builds the deque from a sequence X.
        If X is empty, initializes an empty deque.
        """
        l = max(3 * len(X), 3)
        self._resize(l)
        self.size = len(X)
        for i, x in enumerate(X):
            self.A[self.start + i] = x

    def _resize(self, n):
        m = max(3 * n, 3)
        B = [None] * m
        new_start = m // 3
        for i in range(self.size):
            B[new_start + i] = self.A[self.start + i]
        self.A = B
        self.start = new_start

    def _compute_bounds(self):
        return self.size > 0 and (len(self.A) // self.size >= 6)

    # Copies n elements from self.A starting at logical index i to A starting at logical index j (forward)
    def _copy_forward(self, i, n, A, j):  # O(n)
        # i and j are logical indices (0-based, relative to the deque's logical start)
        if (i < 0) or (n < 0) or (i + n > self.size) or (j < 0) or (i + n > len(A) - self.start):
            raise IndexError("Copy range out of bounds")
        for k in range(n):
            A[self.start + j + k] = self.A[self.start + i + k]

    # Copies n elements from self.A starting at logical index i to A starting at logical index j (backward)
    def _copy_backward(self, i, n, A, j):  # O(n)
        # i and j are logical indices (0-based, relative to the deque's logical start)
        if (i < 0) or (n < 0) or (j + n > self.size) or (j < 0) or (j + n > len(A) - self.start):
            raise IndexError("Copy range out of bounds")
        for k in range(n - 1, -1, -1):
            A[self.start + j + k] = self.A[self.start + i + k]

    def __len__(self): return self.size

    def __getitem__(self, i):
        if i < 0 or i >= self.size: raise IndexError()
        return self.A[self.start + i]

    def insert_first(self, x):
        if self.start == 0:
            self._resize(self.size)
        self.start -= 1
        self.A[self.start] = x
        self.size += 1

    def insert_last(self, x):
        if self.start + self.size == len(self.A):
            self._resize(self.size)
        self.A[self.start + self.size] = x
        self.size += 1

    def delete_first(self):
        if self.size == 0: raise IndexError("Deque is empty")
        val = self.A[self.start]
        self.A[self.start] = None
        self.start += 1
        self.size -= 1
        if self._compute_bounds():
            self._resize(self.size)
        return val

    def delete_last(self):
        if self.size == 0: raise IndexError("Deque is empty")
        idx = self.start + self.size - 1
        val = self.A[idx]
        self.A[idx] = None
        self.size -= 1
        if self._compute_bounds():
            self._resize(self.size)
        return val

    def insert_at(self, i, x):
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")

        # If inserting at the front or back, use optimized methods
        if i == 0:
            self.insert_first(x)
        elif i == self.size:
            self.insert_last(x)
        else:
            #self, i, n, A, j
            # Shift elements right to make space
             # Check if we need to resize
            if self.start + self.size == len(self.A):
                self._resize(self.size)
            
            #shift elements to the right
            for i in range(self.size - 1, i - 1, -1):
                self.A[self.start + i + 1] = self.A[self.start + i]
            self.A[self.start + i] = x

            self.size += 1
    
    def delete_at(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        # If deleting at the front or back, use optimized methods
        if i == 0:
            return self.delete_first()
        elif i == self.size - 1:
            return self.delete_last()
        else:
            # Save the value to return
            val = self.A[self.start + i]
            
            # Shift elements left to fill the gap
            for k in range(i, self.size - 1):
                self.A[self.start + k] = self.A[self.start + k + 1]
            
            # Clear the last element and update size
            self.A[self.start + self.size - 1] = None
            self.size -= 1
            # Check if we need to resize
            if self._compute_bounds():
                self._resize(self.size)

            return val

if __name__ == "__main__":
    dq = Deque_Array_Seq()
    print(dq.A)
    print(dq.start)
    dq.insert_first(10)
    print(dq.A)
    print(dq.start)
    dq.insert_first(20)
    print(dq.A)
    print(dq.start)
    dq.insert_first(30)
    print(dq.A)
    print(dq.start)
    dq.insert_last(40)
    print(dq.A)
    print(dq.start)
    dq.insert_last(50)
    print(dq.A) 
    print(dq.start)
    print(dq.__getitem__(2))  # Should print 10
    print("len of array is", len(dq.A))  # Should print 6
    print("size of array is", dq.size)  # Should print 5
    dq.insert_last(60)
    print(dq.A)     
    print(dq.start)
    dq.delete_first()
    print(dq.A) 
    print(dq.start)
    dq.delete_first()
    print(dq.A)
    print(dq.start)
    dq.delete_first()
    print(dq.A)
    print(dq.start)
    dq.delete_first()
    print(dq.A)
    print(dq.start)
    dq.delete_last()
    print(dq.A)
    print(dq.start)
    dq.insert_at(1, 100)
    print(dq.A) 
    print(dq.start)
    dq.insert_at(1, 200)
    print(dq.A) 
    print(dq.start)
    dq.insert_at(2, 10)
    print(dq.A) 
    print(dq.start)
    dq.delete_at(2)
    print(dq.A)
    print(dq.start)