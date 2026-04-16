def general_relax(Adj, w, s):  # Adj: adjacency list, w: weights, s: start 
    d = [float('inf') for _ in Adj] # shortest path estimates d(s, v) 
    parent = [None for _ in Adj] 
    d[s], parent[s] = 0, s 
    while True:     # repeat forever! 
        #relax some d[v] # ?? # relax a shortest path estimate d(s, v)
        return d, parent   
    # return weights, paths via parents