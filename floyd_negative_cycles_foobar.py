# returns costs of shortest paths in at most n steps
def floyd_warshall(graph):
    n = len(graph)
    # initialize dist
    dist = graph.copy()
    # compute shortest distances after at most n steps
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def are_there_negative_cycles(graph):
    B = floyd_warshall(test)
    answer=False
    for i in range(len(graph)):
        if B[i][i]<0:
            answer=True
    return answer

# shortest path that visists all vertices from s to t
def tsp(graph, s, t):
    n = len(graph)
    INF = float('inf')
    
    # Initialize DP table
    dp = [[INF] * n for _ in range(2**n)]
    dp[1 << s][s] = 0
    
    # Iterate over all subsets of vertices
    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + graph[u][v])
    
    # Find the shortest path from s to t
    min_cost = INF
    for v in range(n):
        if v == s or v == t:
            continue
        min_cost = min(min_cost, dp[(1 << n) - 1][v] + graph[v][t])
    
    return min_cost

# Example:
if __name__ == "__main__":
    # Example cost matrix A
    test = [[0, 3, 4, 6],
            [3, 0, 1, 7],
            [2, 3, 4, -2],
            [-2, 3, 4, 8]]
    
    N=len(test)
    
    # Calculate shortest paths after n steps
    dist=floyd_warshall(test)
    print(dist)

    # are there negative cycles:
    neg_cycles=are_there_negative_cycles(test)
    print('Negative cycles: ', neg_cycles)

    if not neg_cycles:
        print(f'cost of shortest path that visits all {N} vertices:',tsp(test, 0, N-1))
