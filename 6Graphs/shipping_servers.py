def dijkstra_normal(Adj,w,s):
    d = [float('inf') for v in Adj]
    d[s] = 0
    Q = [i for i in range(len(Adj))]  #we will return min by finding it every time

    while len(Q) > 0:
        u = Q[0] #finding min key vertex
        for v in Q:
            if d[v] < d[u]:
                u = v
        Q.remove[u]
        for v in Adj[u]:
            if d[v] > d[u]+w(u,v):
                d[v] = d[u] + w(u,v)
    return d

def dijkstra_bottleneck(Adj,w,s):
    d = [0 for v in Adj]
    d[s] = float('inf')
    Q = [i for i in range(len(Adj))]  #we will return max by finding it every time
    while len(Q) > 0:
        u = Q[0]                    # find max capacity in Q 
        for v in Q:
            if d[v] > d[u]:
                u = v
        Q.remove[u]
        for v in Adj[u]:
            d[v] = max(d[v], min(d[u], w(u,v)))
    return d

def ship_server_stats(R, s, t): 
    n = 0 
    city_idx = {} # label cities with integers 
    
    for (_s, _t, _w, _c) in R: 
        for city in (_s, _t): 
            if city not in city_idx: 
                city_idx[city] = n 
                n += 1 
                
    Adj = [[] for i in range(n)] # construct graph 
    w_w, w_c = {}, {} 
    
    for (_s, _t, _w, _c) in R: 
        si, ti = city_idx[_s], city_idx[_t] 
        Adj[si].append(ti) 
        w_w[(si, ti)], w_c[(si, ti)] = _w, _c 
        
    si, ti = city_idx[s], city_idx[t] # find max bottleneck weight 
    w = dijkstra_bottleneck(Adj, lambda u, v: w_w[(u, v)], si)[ti] 
    
    for i in range(n): # remove edges above bottleneck (below bottleneck weight)
        for j in Adj[i]: 
            if w_w[(i, j)] < w: 
                w_c[(i, j)] = float('inf') 
                
    c = dijkstra_normal( Adj, lambda u,v: w_c[(u,v)], si)[ti] # compute min length

    return w,c