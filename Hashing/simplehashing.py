
'''
1)
Insert integer keys A = [67, 13, 49, 24, 40, 33, 58] in order into a hash table of size 
9 using the hash function h(k) = (11k + 4) mod 9. Collisions should be resolved via chaining, 
where collisions are stored at the end of a chain. Draw a picture of the hash table after all keys 
have been inserted. 

2)
(a) [2 points] Insert integer keys A = [47, 61, 36, 52, 56, 33, 92] in order into 
a hash table of size 7 using the hash function h(k) = (10k + 4) mod 7. Each slot of 
the hash table stores a linked list of the keys hashing to that slot, with later insertions 
being appended to the end of the list. Draw a picture of the hash table after all keys 
have been inserted. 
(b) [3 points] Suppose the hash function were instead h(k) = ((10k + 4) mod c) mod 7
for some positive integer c. Find the smallest value of c such that no collisions occur 
when inserting the keys from A.

'''

def hashfunction(num):
    res = 11*num+4
    res = res%9
    return res

def psethash(num, c = 7):
    hk  =(((10*num)+4) % c)% 7
    return hk




def hashset(A,c):

    D = [[] for _ in range(7)]
    
    for num in A:
        hashingindex = psethash(num,c)
        D[hashingindex].append(num)

    for chain in D:
        print('->', end='')
        for num in chain:
            print(num , end='->')
        print()


if __name__ == '__main__':
    A=[47, 61, 36, 52, 56, 33, 92]
    # hashset(A)
    hashset(A,7)



    # 2 part b
    c = 1
    while(True):
        flag = 0
        D = [[] for _ in range(7)]
    
        for i in range(len(A)):
            hashingindex = psethash(A[i],c)
            if D[hashingindex]:
                break
            D[hashingindex].append(A[i])
            if i == len(A) -1 :
                flag = 1
        if flag == 1:
            break
        c += 1
    print(c)
    hashset(A,c)