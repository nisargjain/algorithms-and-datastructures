
def Set_from_Seq(seq):  #seq is any sequence interface class such as Linked list or Array
    class set_from_seq:
        def __init__(self): self.S = seq()       
        def __len__(self): return len(self.S)   
        def __iter__(self): yield from self.S
        def build(self, A):
                self.S.build(A)        
        def insert(self, x):  #O(i) not efficient we'll use hashing to improve performance
            for i in range(len(self)):
                if self.S.get_at(i).key == x.key:
                    self.S.set_at(i, x)
                    return
            self.S.insert_last(x)
                
        def delete(self, k):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == k:
                    return self.S.delete_at(i)
        
        def find(self, k):
            for x in self:
                if x.key == k: return x
            return None
                
        def find_min(self):
            out = None
            for x in self:
                if (out is None) or (x.key < out.key):
                    out = x
            return out
            
        def find_max(self):
            out = None
            for x in self:
                if (out is None) or (x.key > out.key):
                    out = x
            return out
                
        def find_next(self, k):
            out = None
            for x in self:
                if x.key > k:
                    if (out is None) or (x.key < out.key):
                        out = x
            return out
                
        def find_prev(self, k):
            out = None
            for x in self:
                if x.key < k:
                    if (out is None) or (x.key > out.key):
                        out = x
            return out
                
        def iter_ord(self):
            x = self.find_min()
            while x:
                yield x
                x = self.find_next(x.key)
        
    return set_from_seq
