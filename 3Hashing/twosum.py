'''
MIT has employed Gank Frehry to build a new wing of the Stata Center to house the new College 
of Computing. MIT wants the new building be as tall as possible, but Cambridge zoning laws limit 
all new buildings to be no higher than positive integer height h. As an innovative architect, Frehry 
has decided to build the new wing by stacking two giant aluminum cubes on top of each other, into 
which rooms will be carved. However, Frehry's supplier of aluminum cubes can only make cubes 
with a limited set of positive integer side lengths S = {s0, . . . , sn-1}. Help Frehry purchase cubes 
for the new building.

Problem 4

(a) Assuming the input S fits within Θ(n) machine words, describe an expected O(n)-
time algorithm to determine whether there exist a pair of side lengths in S that exactly 
sum to h. 
(b) Unfortunately for Frehry, there is no pair of side lengths in S that sum exactly to h. 
Assuming that h = 600n^6, describe a worst-case O(n)-time algorithm to return a pair 
of side lengths in S whose sum is closest to h without going over.

'''

# we do part a) first

def twosum(S, h):
    #let H be empty hash set
    H = set()
    for num in S:
        remainder = h-num
        if remainder in H:
            print("The required sum can be formed by ({}, {})".format(num, remainder))
            return
        else: 
            H.add(num)
    print("No such sum is possible")
    return False
    
import sys
sys.path.append('../Sorting')
from linearsorting import radix_sort
def maxtwosum(S, h):

    #since h = O(n^6) we remove all the elements greater than h in S. Then the remaining
    #set S' will now have elements of order n^6 only. which is good since we can use radix sort
    #on it.

    newS = []
    for num in S:
        if num<h:
            newS.append(num)
    
    radix_sort(newS)

    #now since our array is sorted now, we can use two finger algorithm starting from both ends of 
    #our array to find maximum sum less than h
    n = len(newS)
    i = 0  #first pointer
    j = n-1

    maxsum = 0
    indexes = [0,0]
    while(i<j):
        currentsum = newS[i] + newS[j]
        if (currentsum < h):  #we go in if less than h
            if (currentsum>maxsum):  #change indeces only if our max sum is less than current sum
                maxsum = currentsum
                indexes[0], indexes[1] = i, j
            #if current sum is less than maxsum then we need not change anything, we need to increase the
            #total sum which anyways we happen when we increment i. i is changing regardless.
            i+=1
        else:
            j -= 1
    if indexes == [0,0]:
        return False
    else:
        return (newS[indexes[0]], newS[indexes[1]])


if __name__ == '__main__':

    B = [1, 2, 7, 19, 57, 64, 79, 91, 124, 139]
    h = 125
    #test for the sum problem
    twosum(B,h)
    print("maxsum possible is from: ", maxtwosum(B, 122)) #output should be 57 and 64 as they sum to 121.


