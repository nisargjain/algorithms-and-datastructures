from array_seq import Array_Seq

#improves insert_last, delete_last operation in O(1) amortized

class Dynamic_Array_Seq(Array_Seq):
    def __init__(self, r=2):   #r here is NOT the same as fill ratio in notes
        super.__init__() #self.A = [] and #self.size (which will be overridden from current class)
        self.size = 0   #size will be the actual array size
        self.r= r
        self._compute_bounds()
        self._resize(0)
    
    def __len__(self): return self.size   #O(1)

    def __iter__(self):     #O(n)
        for i in range(len(self)): yield self.A[i]

    def _compute_bounds(self):
        self.upper = len(self.A)      #self.A is the array initialization from parent
        # note that this len function has nothing to do with our len functions in both the classes
        # this len is standard len of the array given inbuilt by python
        self.lower = len(self.A)//(self.r * self.r)

        #for r=2 , our lower bound is n/4 and upper is n, n is length of allocated array

    def _resize(self, n):  #O(1) or O(n)
        if (self.lower < n < self.upper): return 

        m = max(n,1) * self.r    #multiple to increase the size
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):   #O(1) amortized
        self._resize(self.size+1)  #checking if size is within bounds or not
        self.A[self.size] = x
        self.size+=1

    def delete_last(self): # O(1)a
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i , x):    # O(n)
        self.insert_last(None)     #this will resize our array if needed
        # self._copy_forward(i+1, self.size - i -1, self.A, i)   
        # this will not work as once we start overwriting from front we will lose data
        # for this we need _copy_backwards which does the same thing but start copying from the last part of array
        self._copy_backward(i, self.size - (i+1), self.A, i+1)
        self.A[i] = x
    
    def delete_at(self, i):
        x = self.A[i]
        self._copy_forward(i+1, self.size-i-1, self.A, i)
        self.delete_last()
        return x
    
    def insert_first(self, x): self.insert_at(0,x)

    def delete_first(self): return self.delete_at(0)

    