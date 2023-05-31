def birthday_match(students):
	n = len(students)
	record = StaticArray(n)
	for k in range(n):
		(name1, bday1) = students[k]
		
		#Return pair if bday1 in record
		for i in range(k):
			(name2, bday2) = record.get_at(i)
			if bday1 == bday2:
				return (name1, name2)
		record.set_at(k, (name1, bday1))
	return None



def birthday_match(students):
    '''
    Find a pair of students with the same birthday
    Input: tuple of student (name, bday) tuples
    Output: tuple of student names or None
    '''
    n = len(students)                                  # O(1)
    record = StaticArray(n)                            # O(n)
    for k in range(n):                                 # n
    (name1, bday1) = students[k]                       # O(1)
    # Return pair if bday1 in record                                 
    for i in range(k):                                 # k
        (name2, bday2) = record.get_at(i)                  # O(1)
    if bday1 == bday2:                                 # O(1)
    return (name1, name2)                              # O(1)
    record.set_at(k, (name1, bday1))                   # O(1)
    return None                                        # O(1)