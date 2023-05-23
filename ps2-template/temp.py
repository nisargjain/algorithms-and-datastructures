

'''

[15 points] Given two booking schedules B1 and B2, where n = |B1| + |B2| and B1
and B2 are the respective booking schedules of two sets of talk requests R1 and R2, 
describe an O(n)-time algorithm to compute a booking schedule B for R = R1∪ R2

ANS:  Say given a B1 = ((1,0,2),(3,2,3),(3,4,6),(2,9,10))
            and a B2 = ((2,0,3),(1,3,4),(2,5,6),(1,7,8))

    the bookings will look like:                          
            B1   1 1 3 0 3 3 0 0 0 2
            B2   2 2 2 1 0 2 0 1 0 0
   Total B1 U B2 3 3 5 1 3 5 0 1 0 2       ((3,0,2),(5,2,3),(1,3,4),(3,4,5),(5,5,6),(1,7,8),(2,9,10))
       Time T-> 0 1 2 3 4 5 6 7 8 9 10


'''


def mitsol(B1, B2):
    currenttime=0          ## B1 = ((1,0,2),(3,2,3),(3,4,6),(2,9,10))
                           ## B2 = ((2,0,3),(1,3,4),(2,5,6),(1,7,8))
    B = []
    n1 = len(B1)
    n2 = len(B2)
    i=0
    j=0
    while(i!=n1 and j!=n2):

        #case1: first booking schedule is depleted or second booking schedule is depleted
        #                    |--------------------|
        #        ^         or        ^
        #      currenttime        currenttime
        if(i==n1):
            B.append((B2[j][0], max(B2[j][1], currenttime), B2[j][2]))
            currenttime = B2[j][2]
            j+=1
        
        elif(j==n2):
            B.append((B1[i][0], max(B1[i][1], currenttime), B1[i][2]))
            currenttime = B1[i][2]
            i+=1

        else:
        # case                  B1     |--------------------------------|
        #                       B2              |-----------------|         
        #               ^
        #            currentime    
        # case                  B1         |-------------------|
        #                       B2     |-----------------|            
        #                                ^
        #            currentime
            if (currenttime < min(B1[i][1], B2[j][1])):
                if min



B1 = ((1,0,2),(3,2,3),(3,4,6),(2,9,10))
B2 = ((2,0,3),(1,3,4),(2,5,6),(1,7,8))
        




#----------------My solution--------------------------

# B1 = ((1,0,2),(3,2,3),(3,4,6),(2,9,10))
# timer = 0
# arr = []
# for tup in B1:
#     while(timer<=tup[1]):
#         arr.append(0)
#         timer+=1
#     while(timer<=tup[2]):
#         arr.append(tup[0])
#         timer+=1
# B2 = ((2,0,3),(1,3,4),(2,5,6),(1,7,8))
# timer = 0
# arr2 = []
# for tup in B2:
#     while(timer<=tup[1]):
#         arr2.append(0)
#         timer+=1
#     while(timer<=tup[2]):
#         arr2.append(tup[0])
#         timer+=1  
# print(arr)
# print(arr2) 

# #reconcialation

# p1 = 0
# p2 = 0
# n1 = len(arr)
# n2 = len(arr2)
# maxlength = max(n1,n2)
# arr3= [0]*maxlength
# if(n1<=n2):
#     for i in range(n1):
#         arr3[i] = arr[i]+arr2[i]
#     for i in range(n1,n2):
#         arr3[i] = arr2[i]
# else:
#     for i in range(n2):
#         arr3[i] = arr[i]+arr2[i]
#     for i in range(n2,n1):
#         arr3[i] = arr[i]

# print(arr3)
# B3 = []
# #arr3 to tuple
# prev = 0
# for i in range(1,len(arr3)-1):
#     if arr3[i] == arr3[i+1]:
#         continue
#     if arr3[i]>0:
#         tup = (arr3[i], prev, i)
#         B3.append(tup)
#     prev=i
# if arr3[prev] != arr3[prev+1]:
#     B3.append((arr3[prev+1], prev, prev+1))
# print(B3)


#-----------------My solution ends---------------------


#-----------------My friends solution----------------

# B1 = ((1,0,2),(3,2,3),(3,4,6),(2,9,10))
# B2 = ((2,0,3),(1,3,4),(2,5,6),(1,7,8))
# maxtuplekey = max(B1[len(B1)-1][2], B2[len(B2)-1][2])
# indexarray = []

# #creating index array
# p1=0
# p2=0
# i=0
# j=0
# while((p1+p2)<=(len(B1)+len(B2)-2)):
#     if(B1[p1][i%2 + 1]<=B2[p2][j%2 + 1]):



# timer = 0
# arr = []
# for tup in B1:
#     while(timer<=tup[1]):
#         arr.append(0)
#         timer+=1
#     while(timer<=tup[2]):
#         arr.append(tup[0])
#         timer+=1

# timer = 0
# arr2 = []
# for tup in B2:
#     while(timer<=tup[1]):
#         arr2.append(0)
#         timer+=1
#     while(timer<=tup[2]):
#         arr2.append(tup[0])
#         timer+=1  
# print(arr)
# print(arr2) 

# #reconcialation

# p1 = 0
# p2 = 0
# n1 = len(arr)
# n2 = len(arr2)
# maxlength = max(n1,n2)
# arr3= [0]*maxlength
# if(n1<=n2):
#     for i in range(n1):
#         arr3[i] = arr[i]+arr2[i]
#     for i in range(n1,n2):
#         arr3[i] = arr2[i]
# else:
#     for i in range(n2):
#         arr3[i] = arr[i]+arr2[i]
#     for i in range(n2,n1):
#         arr3[i] = arr[i]

# print(arr3)
# B3 = []
# #arr3 to tuple
# prev = 0
# for i in range(1,len(arr3)-1):
#     if arr3[i] == arr3[i+1]:
#         continue
#     if arr3[i]>0:
#         tup = (arr3[i], prev, i)
#         B3.append(tup)
#     prev=i
# if arr3[prev] != arr3[prev+1]:
#     B3.append((arr3[prev+1], prev, prev+1))
# print(B3)



#-------------friends solution -----------------