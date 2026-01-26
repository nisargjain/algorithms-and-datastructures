'''

Gal Ore is a scientist who studies climate. As part of her research, she often needs to query the 
maximum temperature the earth has observed within a particular date range in history, based on a 
growing set of measurements which she collects and adds to frequently. Assume that temperatures 
and dates are integers representing values at some consistent resolution. Help Gal evaluate such 
range queries efficiently by implementing a database supporting the following operations. 

record temp(t, d) |   record a measurement of temperature t on date d
max in range(d1,d2) | return max temperature observed between dates d1 and d2 inclusive


To solve this problem, we will store temperature mesurements in an AVL tree with binary search 
tree symantics keyed by date, where each node A stores a measurement 
A.item with a date property A.item.key and temperature property A.item.temp.


'''

from set_avl import AVL_Set_Node, Set_AVL_Tree


class Measurement:
    def __init__(self, temp, date):
        self.key = date
        self.temp = temp
    def __str__(self): return "%s,%s" % (self.key, self.temp)

class Temperature_DB_Node(AVL_Set_Node):

    def subtree_update(A):
        super().subtree_update()
        A.max_temp = A.item.temp
        A.min_date = A.max_date = A.item.key   #we kept it key because our code runs on key
        A.max_temp = A.item.temp
        if A.left:
            A.min_date = A.left.min_date
            A.max_temp = max(A.max_temp, A.left.max_temp)
            
        if A.right:
            A.max_date = A.right.max_date
            A.max_temp = max(A.max_temp, A.right.max_temp)

    def subtree_max_in_range(A, d1, d2):
        if (A.max_date < d1) or (d2 < A.min_date): return None
        if (d1 <= A.min_date) and (A.max_date <= d2): return A.max_temp
        t = None
        if d1 <= A.item.key <= d2:
            t = A.item.temp
        if A.left:
            t_left = A.left.subtree_max_in_range(d1, d2)
            if t_left:
                if t: t = max(t, t_left)
                else: t = t_left
        if A.right:
            t_right = A.right.subtree_max_in_range(d1, d2)
            if t_right:
                if t: t = max(t, t_right)
                else: t = t_right
        return t
    

class Temperature_DB(Set_Binary_Tree):
    def __init__(self):
        super().__init__(Temperature_DB_Node)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except: pass
        self.insert(Measurement(t, d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)


if __name__=="__main__":
    db = Temperature_DB(Measurement(37,0))
    db.record_temp(Measurement(34, 1))
    db.record_temp(Measurement(43, 2))
    db.record_temp(Measurement(36, 3))
    db.record_temp(Measurement(46, 4))
    db.record_temp(Measurement(28, 5))
    db.record_temp(Measurement(31, 6))
    print(db.max_in_range(2,5))