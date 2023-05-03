'''
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
(b) A house in Porkland is special if it either (1) has no easterly neighbor or 
(2) its adjacent neighbor to the east contains at least as many bricks as it does. Given an array 
containing the number of bricks in each house of Porkland, describe an O(n)-time 
algorithm to return the damage for every house in Porkland when all but one house
in Porkland is special. 
(c) Given an array containing the number of bricks in each house of Porkland, describe 
an O(n log n)-time algorithm to return the damage for every house in Porkland. 
(d) Write a Python function get damages that implements your algorithm. 

'''

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

    arr = [1, 2, 3, 4, 3, 4, 5, 6, 7]
   #       1, 1, 1, 2, 1, 1, 1, 1, 1
    #finding special element index
    l = len(arr)
    sp = 0
    for i in range(l-1):
        if arr[i+1]<arr[i]:
            sp = i+1
            break
    
    #computing damages using two finger algorithm :)

    damages = [1]*l
    second = sp

    for first in range(i+1):
        while((arr[first]>arr[second]) and (second<=l-1)):
            second += 1
        damages[first] += second - sp

    print(damages)

    H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    damages = get_damages(H)
    print(damages)