# selecting max in subarray and swapping with last
def selectionsort(A, i=None):      #T(i)
    '''Sort A[:i + 1]'''
    if i is None: i = len(A)- 1    #O(1)
    if i>0: 
        j = prefix_max(A, i)       #provides us the index of max element     
        A[j], A[i] = A[i], A[j]    #O(1)
        selectionsort(A, i-1)      #T(i - 1)

def prefix_max(A, i):               #S(i)
    if i>0:                         #O(1)
        j = prefix_max(A, i-1)      #S(i-1)
        if(A[j] > A[i]):            #O(1)
            return j
    return i

if __name__=="__main__":
    A = [3,15,657,8,2,34,7, 13 , 4, 7, 1]
    selectionsort(A)
    print(A)
