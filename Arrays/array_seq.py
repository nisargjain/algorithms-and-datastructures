#implements static array sequence interface
#kind of waste to use array to implement array but explains the concepts well
class Array_Seq:
    def __init__(self):
        self.A = []
        self.size = 0
    
    def __len__(self): return self.size   #O(1)

    def __iter__(self): yield from self.A    #O(n) self.A is an array data structure of python which will yield items automatically

    def build(self,X):
        self.A = [a for a in X]             #(O(n))
        self.size = len(self.A)

    def get_at(self,i): return self.A[i]   #O(1)
    
    def set_at(self, i, x): self.A[i] = x

 
    #copies the data (of size n) of self.A starting from ith index to
    # to A starting from jth index.      
    def _copy_forward(self, i, n, A, j): #O(n)
        for k in range(n):
            A[j+k] = self.A[i+k]

    def printseq(self):
        for ele in self.A:
            print(ele, end =' ')
        print()
            
    #does the same as copyforward but starts copying from back
    def _copy_backward(self, i, n, A, j):
        for k in range(n-1, -1, -1):
            A[j+k] = self.A[i+k]

    def insert_at(self, i, x):   #O(n)
        n = len(self)
        A = [None]*(n+1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n-i, A, i+1)
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None]*(n-1)
        self._copy_forward(0, i, A, 0)
        x= self.A[i]
        self._copy_forward(i+1, n-i-1, A, i)
        self.build(A)
        return x

    #O(n)
    def insert_first(self,x): self.insert_at(0, x)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_first(self): return self.delete_at(0)
    def delete_last(self): return self.delete_at(len(self)-1)