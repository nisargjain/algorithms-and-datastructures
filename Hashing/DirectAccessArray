
class DirectAccessArray:

    def __init__(self, u): self.A = [None] * u # O(u)

    def find(self, k): return self.A[k] # O(1)

    def insert(self, x): self.A[x.key] = x # O(1)

    def delete(self, k): self.A[k] = None # O(1)

    def find_next(self, k):
        for i in range(k, len(self.A)): # O(u)
            if self.A[i] is not None:
                return self.A[i]
            
    def find_max(self):
        for i in range(len(self.A) - 1, -1, -1): # O(u)
            if self.A[i] is not None:
                return self.A[i]
            
    def delete_max(self):
        for i in range(len(self.A) - 1, -1, -1): # O(u)
            x = self.A[i]
            if x is not None:
                self.A[i] = None
                return x