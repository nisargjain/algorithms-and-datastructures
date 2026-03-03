def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    ##################
    D = {}                              # hash table: freq table -> count of substrings with that freq
    k = len(S[0])

    # --- Build phase: slide a window of size k across T ---

    initial_substring = T[0:k]          # first length-k substring
    temp = [0]*26                       # freq table: 26 entries for each lowercase letter
    for c in initial_substring:
        temp[ord(c)-ord('a')] += 1      # build freq table for first substring
    D[tuple(temp)] = 1                  # store as hashable tuple key, count = 1

    j = k
    while j < len(T):                   # slide window one character at a time
        c_new = T[j]                    # character entering the window (right side)
        c_old = T[j-k]                  # character leaving the window (left side)
        temp[ord(c_new)-ord('a')] += 1  # add new character to freq table
        temp[ord(c_old)-ord('a')] -= 1  # remove old character from freq table
        temp_tuple = tuple(temp)
        if temp_tuple in D:
            D[temp_tuple] += 1          # seen this freq table before, increment count
        else: D[temp_tuple] = 1         # first time seeing this freq table
        j += 1

    # --- Query phase: look up each S_i in the hash table ---

    A = [0]*len(S)
    for i, s in enumerate(S):
        temp = [0]*26
        for c in s:
            temp[ord(c)-ord('a')] += 1  # build freq table for S_i in O(k)
        temp_tuple = tuple(temp)
        if temp_tuple in D:
            A[i] = D[temp_tuple]        # found: return stored count
        else: A[i] = 0                  # no anagram substrings of S_i in T
    ##################
    return tuple(A)