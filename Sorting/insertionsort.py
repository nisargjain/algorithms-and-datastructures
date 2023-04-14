

def insertionsort(A, i=None):      #T(i)
    '''Sort A[:i]'''
    if i is None: i = len(A)- 1    #O(1)
    if i>0: 
        #sorting the first i-1 elements and then inserting the ith.
        insertionsort(A, i-1)       #T(i-1)
        insert(A,i)

def insert(A, i):               #S(i)
    if i>0:             
        # if i^th element is less than i-1 (which by the way is sorted)
        if(A[i]<A[i-1]):
            A[i], A[i-1] = A[i-1] , A[i]
            insert(A, i-1)            #S(i-1)

if __name__=="__main__":
    A = [3,15,657,8,2,34,7, 13 , 4, 7, 1]
    insertionsort(A)
    print(A)
