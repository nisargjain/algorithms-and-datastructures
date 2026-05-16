

def dfs(Adj, s, parent=None, order=None, ancestors = None):        
    # Traverse neighbors
    for v in Adj[s]:
        if v in ancestors[s]:
            return -1
        if parent[v] is None:
            parent[v] = s
            ancestors[v] = ancestors[s].copy()  # Copy parent's ancestors
            ancestors[v].add(s)
            flag = dfs(Adj, v, parent, order, ancestors)  
            if flag == -1:
                return -1
    # Append to order after all descendants are visited (post-order)
    order.append(s)
    return parent, order

def full_dfs(Adj,s):
    
    parent = [None for v in Adj]
    order = []
    ancestors = [set() for v in range(len(Adj))]

    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            ancestors[v].add(v)
            flag = dfs(Adj, v, parent, order, ancestors)
            if flag == -1:
                return None
    return parent, order

def dag(Adj, topo, w, s):  # Adj: adjacency list, w: weights, s: start 
    d = [float('inf') for _ in Adj] # shortest path estimates d(s, v) we only see from s hence single list variable and not a list of list
    parent = [None for _ in Adj] 
    d[s], parent[s] = 0, s 
    for u in topo:
        for v in Adj[u]:
            if d[v] > (d[u] + w[(u,v)]):
                parent[v] = u
                d[v] = d[u] + w[(u,v)]
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
        None: If the job cannot be completed (e.g., a cycle is detected). 
              (You can change this to return -1 if you prefer).
    """
    # ---------------------------------------------------------
    # TODO: Implement your O(|D|)-time algorithm here
    # ---------------------------------------------------------
    ### Create Adjacency List, Vertex List and the Graph and Weight Matrix to run DAG.
    #create integer map for filenames
    files = {}
    times = {}
    for i,t in enumerate(C):
        files[t[0]] = i+1
        times[i+1] = t[1]

    V = [i for i in range(len(C)+1)]  # vertice list
    W = {} # weight map
    for i in range(1, len(C)+1):
        W[(0,i)] = -times[i]
    Adj= [[] for i in range(len(C)+1)]
    Adj[0] = [i for i in range(1,len(C)+1)]
    for a, b in D:
        Adj[files[a]].append(files[b])
        W[(files[a], files[b])] = -times[files[b]]

    #check cycle or return order

    dfsresult = full_dfs(Adj, 0)
    if dfsresult is None:
        return None
    
    time,_ = dag(Adj, reversed(dfsresult[1]), W, 0) 
    return -min(time) # basically return max possible distance from s




# ==========================================
# Testing Framework
# ==========================================
def run_tests():
    test_cases = [
        {
            "name": "Test 1: Simple Linear Dependency",
            "C": [("A", 10), ("B", 20), ("C", 30)],
            "D": [("A", "B"), ("B", "C")],
            "expected": 60  # Path: A(10) -> B(20) -> C(30)
        },
        {
            "name": "Test 2: Parallel Jobs (Critical Path)",
            "C": [("A", 10), ("B", 50), ("C", 10), ("D", 20)],
            "D": [("A", "C"), ("B", "D")],
            "expected": 70  # A->C takes 20. B->D takes 70. Parallel max is 70.
        },
        {
            "name": "Test 3: Complex DAG (Multiple paths to same node)",
            "C": [("A", 5), ("B", 10), ("C", 15), ("D", 5), ("E", 10)],
            "D": [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")],
            "expected": 35  # Max path: A(5) -> C(15) -> D(5) -> E(10) = 35
        },
        {
            "name": "Test 4: Disconnected Components",
            "C": [("A", 100), ("B", 10), ("C", 20)],
            "D": [("B", "C")],
            "expected": 100 # B->C takes 30. A takes 100 on its own. Max is 100.
        },
        {
            "name": "Test 5: Cycle Detection (Impossible Job)",
            "C": [("A", 10), ("B", 20), ("C", 30)],
            "D": [("A", "B"), ("B", "C"), ("C", "A")],
            "expected": None # Cycle exists, cannot be completed.
        }
    ]

    passed = 0
    for i, test in enumerate(test_cases, 1):
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