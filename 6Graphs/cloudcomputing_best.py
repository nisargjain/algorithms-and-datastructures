def dfs(Adj, s, parent=None, order=None):
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order


def full_dfs(Adj):
    parent = [None for _ in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order


def topo_shortest_paths(Adj, w, s):
    _, order = full_dfs(Adj)
    order.reverse()                             # topological order

    # Cycle check via ranks
    rank = [None] * len(Adj)
    for i in range(len(Adj)):
        rank[order[i]] = i

    for v1 in range(len(Adj)):
        for v2 in Adj[v1]:
            if rank[v1] >= rank[v2]:            # back edge or self-loop = cycle
                return None, None

    # DAG relaxation (shortest path with negative weights = longest path)
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s

    for u in order:
        for v in Adj[u]:
            if d[v] > d[u] + w(u, v):
                d[v] = d[u] + w(u, v)
                parent[v] = u

    return d, parent


def min_time(C, D):
    """
    Calculates the minimum time to complete a set of cloud computing jobs.

    Args:
        C (list of tuples): [(file_name, time_needed), ...]
                            Example: [("A", 10), ("B", 20)]
        D (list of tuples): [(dependency_1, dependency_2), ...]
                            Example: [("A", "B")] means A must finish before B.

    Returns:
        int: The minimum number of microseconds needed to complete all jobs.
        None: If the job cannot be completed (cycle detected).
    """
    n = len(C)

    # Map file names to integer indices 1..n
    file_idx, file_time = {}, {}
    for i in range(n):
        f, t = C[i]
        file_idx[f] = i + 1
        file_time[i + 1] = t

    # Build adjacency list and weight dict (0 = supernode)
    Adj = [[] for _ in range(n + 1)]
    w = {}

    # Supernode 0 → every job (weight = -time of destination)
    Adj[0] = list(range(1, n + 1))
    for i in range(1, n + 1):
        w[(0, i)] = -file_time[i]

    # Dependency edges
    for f1, f2 in D:
        i1, i2 = file_idx[f1], file_idx[f2]
        Adj[i1].append(i2)
        w[(i1, i2)] = -file_time[i2]           # negative for longest-path trick

    # Run DAG shortest path (cycle check built in)
    dist, _ = topo_shortest_paths(Adj, lambda u, v: w[(u, v)], 0)

    if dist is None:
        return None

    return -min(dist)                           # negate to get longest path


# ==========================================
# Testing Framework
# ==========================================
def run_tests():
    test_cases = [
        {
            "name": "Test 1: Simple Linear Dependency",
            "C": [("A", 10), ("B", 20), ("C", 30)],
            "D": [("A", "B"), ("B", "C")],
            "expected": 60      # A(10) -> B(20) -> C(30)
        },
        {
            "name": "Test 2: Parallel Jobs (Critical Path)",
            "C": [("A", 10), ("B", 50), ("C", 10), ("D", 20)],
            "D": [("A", "C"), ("B", "D")],
            "expected": 70      # A->C=20, B->D=70, max=70
        },
        {
            "name": "Test 3: Complex DAG (Multiple paths to same node)",
            "C": [("A", 5), ("B", 10), ("C", 15), ("D", 5), ("E", 10)],
            "D": [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")],
            "expected": 35      # A(5)->C(15)->D(5)->E(10)=35
        },
        {
            "name": "Test 4: Disconnected Components",
            "C": [("A", 100), ("B", 10), ("C", 20)],
            "D": [("B", "C")],
            "expected": 100     # B->C=30, A alone=100, max=100
        },
        {
            "name": "Test 5: Cycle Detection (Impossible Job)",
            "C": [("A", 10), ("B", 20), ("C", 30)],
            "D": [("A", "B"), ("B", "C"), ("C", "A")],
            "expected": None    # Cycle exists
        },
        {
            "name": "Test 6: Single Job, No Dependencies",
            "C": [("A", 42)],
            "D": [],
            "expected": 42      # Just one job, no deps
        },
        {
            "name": "Test 7: Self-loop (Cycle on single node)",
            "C": [("A", 10)],
            "D": [("A", "A")],
            "expected": None    # A depends on itself
        },
        {
            "name": "Test 8: Diamond Dependency",
            #        A(5)
            #       /    \
            #     B(10)  C(20)
            #       \    /
            #        D(5)
            # Path via C is longer: A+C+D = 5+20+5 = 30
            "C": [("A", 5), ("B", 10), ("C", 20), ("D", 5)],
            "D": [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")],
            "expected": 30
        },
        {
            "name": "Test 9: Long Chain vs Fat Parallel Jobs",
            # Chain: A->B->C->D->E = 1+1+1+1+100 = 104
            # Fat single job: Z = 103
            # Critical path is the chain
            "C": [("A", 1), ("B", 1), ("C", 1), ("D", 1), ("E", 100), ("Z", 103)],
            "D": [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")],
            "expected": 104
        },
        {
            "name": "Test 10: Cycle hidden deep in graph",
            # A->B->C->D->E, but also E->C (hidden back edge)
            "C": [("A", 5), ("B", 5), ("C", 5), ("D", 5), ("E", 5)],
            "D": [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "C")],
            "expected": None    # E->C is a back edge, cycle
        },
        {
            "name": "Test 11: Multiple Disconnected Chains",
            # Chain 1: A->B = 10+20 = 30
            # Chain 2: C->D->E = 5+5+5 = 15
            # Chain 3: F = 50 (standalone)
            # Max = 50
            "C": [("A", 10), ("B", 20), ("C", 5), ("D", 5), ("E", 5), ("F", 50)],
            "D": [("A", "B"), ("C", "D"), ("D", "E")],
            "expected": 50
        },
        {
            "name": "Test 12: All Jobs Equally Fast, Wide DAG",
            # All jobs take 1ms, star topology: A -> B,C,D,E,F
            # Critical path = A + any leaf = 1+1 = 2
            "C": [("A", 1), ("B", 1), ("C", 1), ("D", 1), ("E", 1), ("F", 1)],
            "D": [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("A", "F")],
            "expected": 2
        },
    ]

    passed = 0
    for test in test_cases:
        print(f"Running {test['name']}...")
        try:
            result = min_time(test["C"], test["D"])
            if result == test["expected"]:
                print(f"  [PASS] Expected: {test['expected']}, Got: {result}\n")
                passed += 1
            else:
                print(f"  [FAIL] Expected: {test['expected']}, Got: {result}\n")
        except Exception as e:
            print(f"  [ERROR] An exception occurred: {e}\n")

    print(f"--- Test Summary: {passed}/{len(test_cases)} Passed ---")


if __name__ == "__main__":
    run_tests()