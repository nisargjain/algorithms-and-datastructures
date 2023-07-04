'''
A = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
D = [5,   3   3   3   1  1   4  1   1   1]

Porkland is a community of pigs who live in n houses lined up along one side of a long, straight
street running east to west. Every house in Porkland was built from straw and bricks, but some
houses were built with more bricks than others. One day, a wolf arrives in Porkland and all the
pigs run inside their homes to hide. Unfortunately for the pigs, this wolf is extremely skilled at
blowing down pig houses, aided by a strong wind already blowing from west to east. If the wolf
blows in an easterly direction on a house containing b bricks, that house will fall down, along with
every house east of it containing strictly fewer than b bricks. For every house in Porkland, the wolf
wants to know its damage, i.e., the number of houses that would fall were he to blow on it in an
easterly direction

(a) Suppose n = 10 and the number of bricks in each house in Porkland from west to east 
is [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]. Compute for this instance the 
damage for every house in Porkland. 
Ans:                [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
damages for this:   [4,   5,  6,  3,  3, 1,  4, 1,  1,  1]


(b) A house in Porkland is special if it either 
    (1) has no easterly neighbor or 
    (2) its adjacent neighbor to the east contains at least as many bricks as it does. Given an array 
        containing the number of bricks in each house of Porkland, describe an O(n)-time 
        algorithm to return the damage for every house in Porkland when all but one house
        in Porkland is special. 

Ans:  for ex: let an array (which will be increasing decrease for one element then increasing again) 
      be [2, 5, 7, 11, 37, 9, 19, 42]

      here array will be [1, 1, 1, 2, 3, 1, 1, 1]

       we can note that all the numbers after special index will be 1

(c) Given an array containing the number of bricks in each house of Porkland, describe 
an O(n log n)-time algorithm to return the damage for every house in Porkland. 

(d) Write a Python function get damages that implements your algorithm. 

'''

#part b

def sub_problem(A):

    d = [1]*len(A)

    #finding special index
    special_index = -1
    for i in range(len(A)-1):
        if A[i]>A[i+1]:
            special_index = i
            break
    if special_index == -1:
        print(d)
        return None
    a = special_index+1
    b = len(A) - a
    i, j = 0,0
    while i<a:
        if j<b and A[i]>=A[j+a]:
            j+=1
        else: 
            d[i] += j
            i+=1
    print(d)

# problem c and d

def get_damages(H):
    D = [1 for _ in H]
    H2 = [(H[i], i) for i in range(len(H))]

    def merge_sort(A, a = 0, b = None):

        if b is None: b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            i, j, L, R = 0, 0, A[a:c], A[c:b]

            while a < b:

                #understand this.  We are bringing an element from the right array down. When we do that?
                # well we can only do that if j<len(R) that is the first important condition
                #second, either right element is smaller than 
                # (or eqaul to because we consider that blown in question) left element or the left elements are finished 
                #and we have to bring down the right elements. Those are the only two cases.
                if (j < len(R)) and (i >= len(L) or L[i][0] >= R[j][0]):
                    A[a] = R[j]
                    j += 1
                    
                else:
                    #this the sole reason we created H2 array because since we shifted the elements, we wanted to 
                    #know their original location to update the damages array.
                    D[L[i][1]] += j
                    A[a] = L[i]
                    i += 1
                    
                a += 1
    merge_sort(H2)
    return D

def test_get_damages():
    # Test case 1: Empty list
    H = []
    expected = []
    assert get_damages(H) == expected, "Test case 1 failed"

    # Test case 2: Single element
    H = [5]
    expected = [1]
    assert get_damages(H) == expected, "Test case 2 failed"

    # Test case 3: Sorted in ascending order
    H = [1, 2, 3, 4, 5]
    expected = [1, 1, 1, 1, 1]
    assert get_damages(H) == expected, "Test case 3 failed"

    # Test case 4: Sorted in descending order
    H = [5, 4, 3, 2, 1]
    expected = [5, 4, 3, 2, 1]
    assert get_damages(H) == expected, "Test case 4 failed"

    # Test case 5: Random order
    H = [4, 2, 5, 1, 3]
    expected = [4, 2, 3, 1, 1]
    assert get_damages(H) == expected, "Test case 5 failed"


    # Test case 6: Duplicate values
    H = [3, 2, 2, 4, 3]
    expected = [4, 2, 1, 2, 1]
    assert get_damages(H) == expected, "Test case 6 failed"

    # Test case 7: Random Order of Question
    H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    expected = [4,   5,  6,  3,  3, 1,  4, 1,  1,  1]
    assert get_damages(H) == expected, "Test case 7 failed"

    print("All test cases passed!")


# doing problem b

# assume our array is [1,2,3,4,3,4,5,6]   where every element is special except second 3

if __name__=='__main__':

    arr = [1,2,3,4,3,4,5,6]
    sub_problem(arr)
    #main problem
    test_get_damages()
    # H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    # damages = get_damages(H)
    # print(damages)