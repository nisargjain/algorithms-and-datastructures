def indicator(F, i,j):
    if F[i-1][j-1] == 'm':
        return 1
    else: return 0

def count_paths(F): 
    # TODO: Implement your dynamic programming solution here.
    # Return the number of distinct optimal quick paths.
# =====================================================================
    n = len(F)
    if n<=0:
        return None
    
    # initializing DP matrix and base cases
    K = [[-float('inf')]*(n+1) for _ in range(n+1)]
    X = [[0]*(n+1) for _ in range(n+1)]
    # x(i,0) and x(0,j)  == 0 and x(1,1) = 1
    for i in range(n+1):
        X[i][0] = 0
        X[0][i] = 0
    X[1][1] = 1
    K[1][1] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if F[i-1][j-1] == 't':   ## F is zero indexed !!!
                continue
            if i == 1 and j == 1: ## stop from overwriting our base cases!
                K[1][1], X[1][1] = 0, 1 
                continue 
            K[i][j] = indicator(F,i,j) + max(K[i-1][j], K[i][j-1])
            if K[i-1][j] + indicator(F,i,j) == K[i][j]:
                X[i][j] += X[i-1][j]
            if K[i][j-1] + indicator(F,i,j) == K[i][j]:
                X[i][j] += X[i][j-1]
    return X[n][n]
# =====================================================================

def run_tests():
    tests_passed = 0

    # Test 1: Simple 2x2 empty grid
    # Expected: 2 paths (Right->Down, Down->Right)
    F1 = [
        ['.', '.'],
        ['.', '.']
    ]
    assert count_paths(F1) == 2, f"Test 1 Failed: Expected 2, got {count_paths(F1)}"
    print("✅ Test 1 Passed: Simple empty grid (2 paths)")

    # Test 2: Symmetric Mushrooms
    # Max mushrooms is 1. Both R->D and D->R collect exactly 1.
    # Expected: 2 paths
    F2 = [
        ['.', 'm'],
        ['m', '.']
    ]
    assert count_paths(F2) == 2, f"Test 2 Failed: Expected 2, got {count_paths(F2)}"
    print("✅ Test 2 Passed: Symmetric optimal paths (2 paths tied)")

    # Test 3: One strictly superior path
    # R->R->D->D collects 3 mushrooms. All other paths collect fewer.
    # Expected: 1 optimal path
    F3 = [
        ['.', 'm', 'm'],
        ['.', '.', 'm'],
        ['.', '.', '.']
    ]
    assert count_paths(F3) == 1, f"Test 3 Failed: Expected 1, got {count_paths(F3)}"
    print("✅ Test 3 Passed: Single superior path drops sub-optimal ones")

    # Test 4: All valid paths are optimal
    # 3x3 grid full of mushrooms. Every path takes 4 steps, collecting exactly 3 mushrooms.
    # Total paths in 3x3 without backtracking = 6. 
    # Expected: 6 paths
    F4 = [
        ['.', 'm', 'm'],
        ['m', 'm', 'm'],
        ['m', 'm', '.']
    ]
    assert count_paths(F4) == 6, f"Test 4 Failed: Expected 6, got {count_paths(F4)}"
    print("✅ Test 4 Passed: Grid of ties (6 paths)")

    # Test 5: Trees blocking the way
    # The middle is blocked. Only the outer edges work.
    # Going Right-Right-Down-Down collects 2. Down-Down-Right-Right collects 0.
    # Expected: 1 optimal path
    F5 = [
        ['.', '.', 'm'],
        ['.', 't', 'm'],
        ['.', 't', '.']
    ]
    assert count_paths(F5) == 1, f"Test 5 Failed: Expected 1, got {count_paths(F5)}"
    print("✅ Test 5 Passed: Obstacle avoidance with trees")

    # Test 6: Completely blocked grid
    # Impossible to reach home.
    # Expected: 0 paths
    F6 = [
        ['.', 't'],
        ['t', '.']
    ]
    assert count_paths(F6) == 0, f"Test 6 Failed: Expected 0, got {count_paths(F6)}"
    print("✅ Test 6 Passed: Unreachable home returns 0")

    # Test 7: Tiny 1x1 grid
    # Start is also the home.
    # Expected: 1 path
    F7 = [['.']]
    assert count_paths(F7) == 1, f"Test 7 Failed: Expected 1, got {count_paths(F7)}"
    print("✅ Test 7 Passed: 1x1 Base case")

    print("\n🎉 All 7 test cases passed successfully! The DP logic is solid.")

if __name__ == '__main__':
    run_tests()