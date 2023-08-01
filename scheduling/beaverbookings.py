'''
Tim the Beaver is arranging Tim Talks, a lecture series that allows anyone in the MIT community 
to schedule a time to talk publicly. A talk request is a tuple (s,t), where s and t are the starting 
and ending times of the talk respectively with s < t (times are positive integers representing the 
number of time units since some fixed time). 

Tim must make room reservations to hold the talks. 
A room booking is a triple (k, s,t), corresponding to reserving k > 0 rooms between the 
times s and t where s < t. Two room bookings (k1, s1, t1) and (k2, s2, t2) are disjoint 
if either t1 ≤ s2 or t2 ≤ s1, and adjacent if either t1 = s2 or t2 = s1. 

A booking schedule is an ordered tuple of room bookings where: every pair of room 
bookings from the schedule are disjoint, room bookings appear with increasing starting time in the
sequence, and every adjacent pair of room bookings reserves a different number of rooms. 

Given a set R of talk requests, there is a unique booking schedule B that satisfies the requests, i.e., 
the schedule books exactly enough rooms to host all the talks. For example, given a set of talk requests 

R = {(2, 3),(4, 10),(2, 8),(6, 9),(0, 1),(1, 12),(13, 14)}
pictured to the right, the satisfying room booking is: 

B = ((1, 0, 2),(3, 2, 3),(2, 3, 4),(3, 4, 6),(4, 6, 8),(3, 8, 9),(2, 9, 10),(1, 10, 12),(1, 13, 14))

(a) Given two booking schedules B1 and B2, where n = |B1| + |B2| and B1
and B2 are the respective booking schedules of two sets of talk requests R1 and R2, 
describe an O(n)-time algorithm to compute a booking schedule B for R = R1 U R2

ANS:  Say given a B1 = ((1,0,2),(3,2,3),(3,4,6),(2,9,10))
            and a B2 = ((2,0,3),(1,3,4),(2,5,6),(1,7,8))

    the bookings will look like:                          
            B1   1 1 3 0 3 3 0 0 0 2
            B2   2 2 2 1 0 2 0 1 0 0
   Total B1 U B2 3 3 5 1 3 5 0 1 0 2       ((3,0,2),(5,2,3),(1,3,4),(3,4,5),(5,5,6),(1,7,8),(2,9,10))
       Time T-> 0 1 2 3 4 5 6 7 8 9 10

       to do this lets create a current time pointer and look at the cases where the pointer might 
       stand
        let the the first and last booking time for B1 tuple be p1 q1 and the same for second tuple be 
        p2 q2.

        case 1:
        then curr may be less than both p1 and p2
        case 2:
        or curr may be less than either one of the p1 or p2 and greater than the other.
        case 3:
        or curr may be greater than both p1 and p2 and less than both q1 and q2
        case 4:
        or curr may be greater than both p1 and p2 and greater either one of the q1 or q2 and less than the other
        case 5:
        or curr may be greater than both q1 and q2

        we iterate over the tuples 
        for case 1: 
          curr is less than both p1 and p2 
          then curr should become min(p1 , p2)

        for case 2:
        
        ####  cases are wrong work on it again
        
'''


'''
(b) [5 points] Given a set R of n talk requests, describe an O(n log n)-time algorithm to 
return the booking schedule that satisfies R.

we take a set of n talk requests and divide them in 2 equal parts. than we keep on dividing by 
and then merge them with our merge booking code. This is exactly like mergesort.

'''
def mergebookings(B1, B2):
    #length of bookings
    n1 = len(B1)
    n2 = len(B2)
    i, j = 0,0
    curr = 0
    B = []

    while(i+j < n1+n2):
        #Tuple of room booking triples (r, p, q)
        if i<n1: r1, p1, q1  = B1[i]
        if j<n2: r2, p2, q2  = B2[j]

        if i == n1: #only bookings in B2 remain
            r, p, curr = r2, max(curr, p2), q2
            j += 1
        
        elif j == n2: #only bookings in B1 remain
            r,p, curr = r1, max(curr, p1), q1
            i+=1
        
        else: 
            if curr < min(p1, p2):   #if curr is less than both the starting time of slots
                curr = min(p1, p2)
            if q1 <= p2:  #only B1 is overlapping
                r, p, curr = r1,  p1, q1
                i += 1
            elif q2 <= p1: #if only B2 is overlaping
                r, p, curr = r2, p2, q2
                j += 1

            #since both q1 is not less than p2 and q2 is not less than p1:
            elif curr < p2:  #meaning current is at p1 and we need to go till p2
                r, p, curr = r1, curr, p2
            
            elif curr < p1:
                r, p, curr = r2, curr, p1
            
            else:  #overlaps B1 and B2 upto q1 or q2
                r , p , curr = r1+r2,curr, min(q1, q2)
                if q1 == curr: i +=1
                if q2 == curr: j +=1

        B.append((r, p, curr))

    #now we remove adjacent bookings with same no. of rooms and merging them

    B_  = [B[0]]
    n = len(B)
    for r, p, q in  B[1:] :
        r_,p_,q_ = B_[-1]
        if (r == r_) and (q_ == p):
            B_.pop()
            p = p_
        B_.append((r, p, q))
    return B_

        




def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    if len(R) == 1:
        p, q = R[0]
        return ((1, p ,q),)

    t = len(R)
    m = t//2
    left = R[:m]
    right = R[m:]

    left_bookings = satisfying_booking(left)
    right_bookings = satisfying_booking(right)
    B = mergebookings(left_bookings, right_bookings)


    ##################
    return tuple(B)