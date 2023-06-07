
#set interface using sorted arrays.
import sys
from array_seq import Array_Seq
sys.path.append('../Sorting')
from mergesort import mergesort

class Sorted_Array_Set:
    def __init__(self): self.A = Array_Seq() # O(1)

    def __len__(self): return len(self.A) # O(1)

    def __iter__(self): yield from self.A # O(n)

    def iter_order(self): yield from self # O(n)

    def printArray(self): 
        for i in iter(self):
            print(i, end="  ")
        print()
    
    def build(self, X): # O(nlogn), this implementation will take duplicate values
        self.A.build(X)
        self._sort()
        #we need to remove duplicate values/keys from the set.
        #either check before hand building or remove after building
        # implement your code here:
        #-----------------------------

        #-----------------------------

    #need to use various sorting algorithms, i'm using merge sort here
    def _sort(self): # O(nlogn)
        mergesort(self.A.A, 0, len(self)-1)

    def _binary_search(self, k, i, j): # O(log n), k is the key to search
        if i >= j: return i

        m = (i + j) // 2
        x = self.A.get_at(m)
        if x > k: return self._binary_search(k, i, m - 1)
        if x < k: return self._binary_search(k, m + 1, j)

        return m
    
    def find_min(self):
        if len(self)>0: return self.A.get_at(0)
        else: return None

    def find_max(self):
        if len(self)>0: return self.A.get_at(len(self)-1)
        else: return None

    def find(self, k):  #returning index of the key k if found
        if len(self) == 0 : return None

        i  = self._binary_search(k, 0, len(self)-1)
        x = self.A.get_at(i)

        if x == k: return i
        else: return None

    def find_next(self, k):
        if len(self) == 0 : return None
        i  = self._binary_search(k, 0, len(self)-1)
        x = self.A.get_at(i)
        if x>k: return x
        #if x is less than k or equal to k, then we anyways return next element
        #we just check whether the next element exists
        if i+1<len(self): return self.A.get_at(i+1)
        else: return None

    def find_prev(self, k):
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) -1)
        x = self.A.get_at(i)

        if x<k: return x
        if i>0: return self.A.get_at(i-1)
        else: return None

    def insert(self,x):
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x,0,len(self)-1)
            k = self.A.get_at(i)

            if k == x:
                self.A.set_at(i, x)
                return False
            if k>x: self.A.insert_at(i, x)
            else: self.A.insert_at(i+1,x)

        return True
    
    def delete(self, k):
        i = self._binary_search(k, 0, len(self)-1)
        assert self.A.get_at(i) == k
        return self.A.delete_at(i)



if __name__=='__main__':
    #testing
    sortedset = Sorted_Array_Set()
    x = [18, 3]
    sortedset.build(x)
    sortedset.printArray()
    sortedset.insert(67)
    sortedset.insert(17)
    sortedset.printArray()
    sortedset.insert(18)
    sortedset.printArray()
    sortedset.delete(18)
    sortedset.printArray()
    sortedset.delete(17)
    sortedset.delete(67)
    sortedset.delete(3)
    print("len of set is: ", len(sortedset))
    sortedset.printArray()
    print(sortedset.find(3))
    sortedset.build([1,13,7])
    sortedset.printArray()
    print("index of element 7 is: ",sortedset.find(7))
    print(sortedset.find_next(7))
    print(sortedset.find_prev(7))
    for i in iter(sortedset):
        print(i, end = " ")
    print()
    print("len of set is: ", len(sortedset))
