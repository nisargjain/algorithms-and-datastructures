
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

def hashset(A):

    D = [[] for _ in range(9)]
    
    for num in A:
        hashingindex = hashfunction(num)
        D[hashingindex].append(num)

    for chain in D:
        print('->', end='')
        for num in chain:
            print(num , end='->')
        print()


if __name__ == '__main__':
    A = [67, 13, 49, 24, 40, 33, 58]
    hashset(A)