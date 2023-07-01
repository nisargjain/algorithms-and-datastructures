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
        return None
    k = special_index+1
    i,j = 0,k
    while((i<k) and (j<len(A))):
        if A[i]>A[j]:
            d[i] += 1
            j += 1
        else: 
            i+=1
            d[i] += d[i-1] - 1
    
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
                if (j >= len(R)) or (i < len(L) and L[i][0] <= R[j][0]):
                    D[L[i][1]] += j
                    A[a] = L[i]
                    i += 1
                else:
                    A[a] = R[j]
                    j += 1
                a += 1
    merge_sort(H2)
    return D


# doing problem b

# assume our array is [1,2,3,4,3,4,5,6]   where every element is special except second 3

if __name__=='__main__':

    arr = [34, 77, 87, 2, 6, 11, 19]
   #       5,  5,  5,  1, 1,  1,  1
    sub_problem(arr)

    # H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    # damages = get_damages(H)
    # print(damages)