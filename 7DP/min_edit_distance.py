def edit_distance_with_path(A, B):
    """
    Computes the minimum edit distance between string A and string B,
    and returns both the distance and the sequence of operations.
    """
    m = len(A)
    n = len(B)
    
    # 1. Initialize the DP matrix with size (m + 1) x (n + 1)
    # x[i][j] represents the edit distance between A[:i] and B[:j]
    x = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 2. Base Cases (Empty String comparisons)
    for i in range(1, m + 1):
        x[i][0] = i  # Deleting all characters from A
    for j in range(1, n + 1):
        x[0][j] = j  # Inserting all characters to match B
        
    # 3. Fill the DP matrix (The Forward Pass)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                # Characters match, carry over the diagonal cost
                x[i][j] = x[i - 1][j - 1]
            else:
                # Characters don't match, take 1 + minimum of the three choices
                ed_del = 1 + x[i - 1][j]       # Look Up
                ed_ins = 1 + x[i][j - 1]       # Look Left
                ed_rep = 1 + x[i - 1][j - 1]   # Look Diagonal
                x[i][j] = min(ed_del, ed_ins, ed_rep)
                
    # The final edit distance is stored in the bottom right corner
    min_distance = x[m][n]
    
    # 4. Backtracking (The Reverse Pass)
    edits = []
    i = m
    j = n
    
    while i > 0 or j > 0:
        # Match (Diagonal step without cost)
        if i > 0 and j > 0 and A[i - 1] == B[j - 1]:
            # No operation recorded, just move indices backward
            i -= 1
            j -= 1
            
        # Replace (Diagonal step with cost)
        elif i > 0 and j > 0 and x[i][j] == 1 + x[i - 1][j - 1]:
            edits.append(f"Replace '{A[i-1]}' with '{B[j-1]}'")
            i -= 1
            j -= 1
            
        # Delete (Upward step)
        elif i > 0 and x[i][j] == 1 + x[i - 1][j]:
            edits.append(f"Delete '{A[i-1]}'")
            i -= 1
            
        # Insert (Leftward step)
        else:
            edits.append(f"Insert '{B[j-1]}'")
            j -= 1
            
    # Reverse the operations to show them from start to finish
    edits.reverse()
    
    return min_distance, edits

# ---------------------------------------------------------
# Test Runner
# ---------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ("cat", "bat"),           # 1 Replace
        ("apple", "pie"),         # The LCS counter-example
        ("kitten", "sitting"),    # The classic DP benchmark string
        ("algorithm", "altruistic")
    ]
    
    for A, B in test_cases:
        print(f"\n--- Transforming '{A}' to '{B}' ---")
        dist, ops = edit_distance_with_path(A, B)
        print(f"Total Edit Distance: {dist}")
        for step_num, op in enumerate(ops, 1):
            print(f"  Step {step_num}: {op}")