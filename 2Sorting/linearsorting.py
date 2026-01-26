''' using counting sort for large u, where u<n^2  , stable tuple sort '''

import random
import math

def counting_sort(A):
	u = 1 + max([x[1] for x in A])
	D = [[] for i in range(u)]

	#this will create chain for the same key values
	for x in A:
		D[x.key].append(x)

	#then we sort it out by deconstructing the chain
	i = 0
	for chain in D:
		for x in chain:
			A[i] = x
			i+=1

def radix_sort(A):       # for u<n^c     will take O(6nc) time

	n = len(A)
	u = 1+max(A)
	c = math.ceil(math.log(u,n))
	
	#creating c length tuples for every number
	D = [()]*n                                 #whole thing will take O(nc)
	i=0
	for num in A:
		for tupi in range(c):
			divtup = divmod(num,n)
			D[i] = (divtup[1],) + D[i]
			num = num//n
		i+=1
	

	#loop c times from least significant to most significant to sort the tuples  
	# O(nc) time complexity
	# this is basically counting sort repeated c times
	for tupi in range(c-1, -1, -1):
		temp = [[] for _ in range(n)]
		for tup in D:
			temp[tup[tupi]].append(tup)
		i=0
		for chain in temp:
			for tup in chain:
				D[i] = tup
				i+=1


	#reversing the c length tuple to normal #O(nc)
	i=0
	for tup in D:
		A[i]=0
		for t in tup:
			A[i] = A[i]*n+t
		i+=1

	return A

def tuple_sort(A):         # for u<n^2 
	n = len(A)
	D = [None]*n			#takes O(n) time
	i=0
	for num in A:					#takes O(n) time
		D[i] = divmod(num, n)
		i += 1
	
	#counting sort for least important key tup[1]   takes O(n) time
	D2 = [[] for _ in range(n)]
	for tup in D:
		D2[tup[1]].append(tup)
	
	i=0
	for chain in D2:          #iterating for sorting takes O(n) time
		for tup in chain:
			D[i] = tup
			i+=1
	
	#counting sort for most important key tup[0]  takes O(n) time again
	D3 = [[] for _ in range(n)]
	for tup in D:
		D3[tup[0]].append(tup)
	
	i=0
	for chain in D3:          #iterating for sorting takes O(n) time
		for tup in chain:
			D[i] = tup
			i+=1

	#inversing divmod   O(n) time
	i=0
	for tup in D:
		A[i] = tup[0]*n+tup[1]
		i+=1

def test_radix_sort():
    input1 = [170, 45, 75, 90, 802, 24, 2, 66]
    expected_output1 = [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort(input1) == expected_output1

    input2 = [321, 543, 123, 432, 654, 987, 876]
    expected_output2 = [123, 321, 432, 543, 654, 876, 987]
    assert radix_sort(input2) == expected_output2

    input3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_output3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert radix_sort(input3) == expected_output3
    print("All test cases passes")

if __name__ == "__main__":
	A = [100000, 99999, 99998, 99997, 99996]
	radix_sort(A)
	flag = 0
	for i in range(len(A)-1):
		if A[i+1]<A[i]:
			flag = 1
			break
	if flag: print('Not Sorted')
	else: print('Sorted from Tuple')
	if not flag: print(A)
	test_radix_sort()
	


'''
MIT Solution for radix read afterwards

def radix_sort(A):
	"Sort A assuming items have non-negative keys"
	n = len(A)
	u = 1 + max([x.key for x in A]) # O(n) find maximum key
	c = 1 + (u.bit_length() // n.bit_length())
	class Obj: pass
	D = [Obj() for a in A]
	for i in range(n): # O(nc) make digit tuples
		D[i].digits = []
		D[i].item = A[i]
		high = A[i].key
		for j in range(c): # O(c) make digit tuple
			high, low = divmod(high, n)
			D[i].digits.append(low)
	
	for i in range(c): # O(nc) sort each digit
		for j in range(n): # O(n) assign key i to tuples
			D[j].key = D[j].digits[i]
		counting_sort(D) # O(n) sort on digit i
	for i in range(n): # O(n) output to A
		A[i] = D[i].item


'''