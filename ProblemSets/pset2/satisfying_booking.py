"""
R = {(2, 3), (4, 10), (2, 8), (6, 9), (0, 1), (1, 12), (13, 14)}
pictured to the right, the satisfying room booking is: 
B = ((1, 0, 2), (3, 2, 3), (2, 3, 4), (3, 4, 6), 
(4, 6, 8), (3, 8, 9), (2, 9, 10), (1, 10, 12), (1, 13, 14)).

"""


def merge_bookings(B1, B2):
    x = 0
    i = 0
    j = 0
    l1 = len(B1)
    l2 = len(B2)
    B = []
    while (i+j) < (l1+l2):

        if (i<l1) : r1, s1, s2 = B1[i]
        if (j<l2) : r2, t1, t2 = B2[j]

        if (j == l2):
            B.append((r1, max(s1, x), s2))
            x= s2
            i+=1 

        elif (i == l1):
            B.append((r2, max(t1, x), t2))
            x = t2
            j+=1

        else:
            if (x < s1) and (x < t1) :
                x = min(s1,t1)
            elif s2<=t1:
                B.append((r1,x,s2))
                i+=1
                x=s2
            elif t2<=s1:
                B.append((r2, x, t2))
                j+=1
                x = t2
            elif x < t1:
                B.append((r1, x, t1))
                x = t1
            elif x < s1:
                B.append((r2, x, s1))
                x = s1
            else:
                B.append((r1+r2, x, min(s2,t2)))
                x = min(s2,t2)
                if x == s2:
                    i+=1
                if x == t2:
                    j+=1
    B_ = [B[0]]
    for r,s,t in B[1:]:
        r_,s_,t_ = B_[-1]
        if (r == r_) and (t_ == s):
            B_.pop()
            s= s_
        B_.append((r,s,t))
    return B_

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    if len(R) == 1:
        return ((1, R[0][0], R[0][1]),)
    m = len(R) //2
    B1 = satisfying_booking(R[:m])
    B2 = satisfying_booking(R[m:])
    B = merge_bookings(B1, B2)
    return tuple(B)
