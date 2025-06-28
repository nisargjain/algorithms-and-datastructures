def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #

    a = list(A)
    maxlength = 1
    length = 1
    for i in range(1,len(a)):
        # print("loop at number: ", a[i])
        if a[i-1] < a[i]:
            length += 1
            # print("length when increasing: ", length)

            if length > maxlength:
                maxlength = length
                count = 0
            # print("maxlength when increasing: ", maxlength)

        else:
            # print("length when decreased: ", length)
            # print("maxlength when decreased: ", maxlength)
            if length == maxlength:
                count += 1
            length = 1
            # print("current max count", count)
    if length == maxlength:
        count += 1
    ##################
    return count
