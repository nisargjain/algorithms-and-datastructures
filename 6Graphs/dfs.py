def dfs(Adj, s, parent=None, order=None):
    # Initialize on the first call
    if parent is None:
        parent = [None for v in Adj] 
        parent[s] = s 
        order = [] 
        
    # Traverse neighbors
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
            
    # Append to order after all descendants are visited (post-order)
    order.append(s)
    
    return parent, order


def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []

    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    
    return parent, order

