'''
1)
Insert integer keys A = [67, 13, 49, 24, 40, 33, 58] in order into a hash table of size 
9 using the hash function h(k) = (11k + 4) mod 9. Collisions should be resolved via chaining, 
where collisions are stored at the end of a chain. Draw a picture of the hash table after all keys 
have been inserted. 

'''

def hashfunction(num):
    res = 11*num+4
    res = res%9
    return res

def problem1(A):

    D = [[] for _ in range(9)]
    
    for num in A:
        hashingindex = hashfunction(num)
        D[hashingindex].append(num)

    for chain in D:
        print('->', end='')
        for num in chain:
            print(num , end='->')
        print()

def problem4(A, S):
    n = len(A)
    i = 0
    j = n-1
    maxsum = 0
    index= [0,0]
    while(i<j):
        sum = A[i] + A[j]
        if sum <= S:
            if sum > maxsum:
                index[0], index[1] = i , j
                maxsum = sum
            i += 1
        else:
            j -=1
    return index

if __name__ == '__main__':
    A = [67, 13, 49, 24, 40, 33, 58]
    B = [1, 2, 7, 19, 57, 64, 79, 91, 124, 139]
    sumneeded = 151
    
    #test for the sum problem
    # n = len(B)
    # maxsum = 0
    # index = [0,0]
    # for i in range(n):
    #     for j in range(i, n):
    #         temp = B[i]+B[j]
    #         if (temp <= sumneeded) and temp>maxsum:
    #             maxsum = temp
    #             index[0], index[1] = i , j
    # print(index, maxsum, sep='    ')


    #problem1(A)
    #res = problem4(B, sumneeded)    #code for the two finger algorithm where we pass in sorted array to find
                    #pair with max two sum.

    #print(res)


'''
MIT has employed Gank Frehry to build a new wing of the Stata Center to house the new College 
of Computing. MIT wants the new building be as tall as possible, but Cambridge zoning laws limit 
all new buildings to be no higher than positive integer height h. As an innovative architect, Frehry 
has decided to build the new wing by stacking two giant aluminum cubes on top of each other, into 
which rooms will be carved. However, Frehry's supplier of aluminum cubes can only make cubes 
with a limited set of positive integer side lengths S = {s0, . . . , sn-1}. Help Frehry purchase cubes 
for the new building.

Problem 4
Unfortunately for Frehry, there is no pair of side lengths in S that sum exactly to h. 
Assuming that h = 600n6, describe a worst-case O(n)-time algorithm to return a pair 
of side lengths in S whose sum is closest to h without going over.

'''