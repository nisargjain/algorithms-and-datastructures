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


def twosum(A, S):
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

    B = [1, 2, 7, 19, 57, 64, 79, 91, 124, 139]
    sumneeded = 151
    
    #test for the sum problem
    n = len(B)
    maxsum = 0
    index = [0,0]
    for i in range(n):
        for j in range(i, n):
            temp = B[i]+B[j]
            if (temp <= sumneeded) and temp>maxsum:
                maxsum = temp
                index[0], index[1] = i , j
    print(index, maxsum, sep='    ')

    #res = problem4(B, sumneeded)    #code for the two finger algorithm where we pass in sorted array to find
                    #pair with max two sum.

    #print(res)


