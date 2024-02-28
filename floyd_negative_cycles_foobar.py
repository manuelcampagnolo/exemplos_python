# returns costs of shortest paths in at most n steps
def floyd_warshall(graph):
    n = len(graph)
    # initialize dist
    dist = graph.copy()
    # compute shortest distances after n steps
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


# Example usage:
if __name__ == "__main__":
    # Example cost matrix A
    test = [[0, 3, 4, 6],
            [3, 0, 1, 7],
            [2, 3, 4, -2],
            [-3, 3, 4, 8]]
    
    # Calculate shortest paths after n steps
    print(floyd_warshall(test))

    # are there negative cycles:
    print('Negative cycles: ', are_there_negative_cycles(test))
