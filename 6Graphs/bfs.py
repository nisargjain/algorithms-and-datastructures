def bfs(Adj, s):                        # Adj: adjacency list, s: starting vertex
    parent = [None for v in Adj]        # O(V)  — use hash table if vertices are unlabeled
    parent[s] = s                       # O(1)  — root points to itself (marks s as visited)
    level = [[s]]                       # O(1)  — initialize levels with L0 = {s}

    while 0 < len(level[-1]):           # O(?)  — keep going while last level is non-empty
        level.append([])                # O(1) amortized — open a new empty level
        for u in level[-2]:             # O(?)  — loop over every vertex in previous level
            for v in Adj[u]:            # O(|Adj[u]|) — loop over neighbours of u
                if parent[v] is None:   # O(1)  — not yet visited?
                    parent[v] = u       # O(1)  — assign parent (marks v as visited)
                    level[-1].append(v) # O(1) amortized — add v to current frontier

    return parent


def unweighted_shortest_path(Adj, s, t):
    parent = bfs(Adj, s)          # O(V + E) — build BFS tree from source s
    if parent[t] is None:         # O(1)     — is t reachable from s?
        return None               # O(1)     — no path exists

    i = t                         # O(1)     — start at destination t
    path = [t]                    # O(1)     — initialize path with t
    while i != s:                 # O(V)     — walk parent pointers back to s
        i = parent[i]             # O(1)     — move to parent
        path.append(i)            # O(1) amortized — add to path
    return path[::-1]             # O(V)     — reverse: path is built t→s, return s→t