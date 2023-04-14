import unittest

def mergesort(A, i , j): 
    if i < j:
        m = (i+j)//2
        mergesort(A, i, m)
        mergesort(A, m+1, j)
        L = A[i:m+1]
        R = A[m+1:j+1]
        merge(A, L , R, i , j , m)


def merge(A, L, R, i, j, m):
    k = i
    l = 0
    r = 0
    while((l < m+1-i) and (r < j-m) ):
        if(L[l] <= R[r]):
            A[k] = L[l]
            k += 1
            l += 1
        else:
            A[k] = R[r]
            k += 1
            r += 1
    if( l == m+1-i):
        while(r<j-m):
            A[k] = R[r]
            k += 1
            r += 1
    else:
        while(l< m+1 -i):
            A[k] = L[l]
            k += 1
            l += 1


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        expected_result = []
        mergesort(arr, 0, len(arr)-1)
        self.assertEqual(arr, expected_result)

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        mergesort(arr, 0, len(arr)-1)
        self.assertEqual(arr, expected_result)

    def test_unsorted_list(self):
        arr = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]
        mergesort(arr, 0, len(arr)-1)
        self.assertEqual(arr, expected_result)

    def test_list_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_result = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        mergesort(arr, 0, len(arr)-1)
        self.assertEqual(arr, expected_result)

if __name__ == '__main__':
    unittest.main()
