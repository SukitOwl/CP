import json

def printPath(path, v, u):
    if path[v][u] == v:
        return ""

    return printPath(path, v, path[v][u]) + " " + str(path[v][u])

def printSolution(cost ,path, n):
    for v in range(n):
        for u in range(n):
            if (u != v) and path[v][u] != -1:
                print(f"Shortest path from vertex {v} to vertex {u} is ( {v}{printPath(path, v, u)} {u} )")

def FloydWarshell(adjMatrix, n):
    cost = [
        [None] * n,
        [None] * n,
        [None] * n,
        [None] * n
    ]
    path = [
        [None] * n,
        [None] * n,
        [None] * n,
        [None] * n
    ]
    for i in range(n):
        for j in range(n):
            cost[i][j] =  adjMatrix[i][j]
            if i == j:
                path[i][j] = 0
            elif cost[i][j] != 999:
                path[i][j] = i
            else:
                path[i][j] = -1

    print('====================')
    for i in cost:
        print(i)
    print('====================')
    for i in path:
        print(i)
    print("\n")

    for k in range(n):
        for v in range(n):
            for u in range(n):
                if cost[v][k] != 999 and cost[k][u] != 999 and cost[v][k] + cost[k][u] < cost[v][u]:
                    cost[v][u] =  cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
                    print(f"k: {k}, v: {v}, u: {u}")
                    print('====================')
                    for i in cost:
                        print(i)
                    print('====================')
                    for i in path:
                        print(i)

            if cost[v][v] < 0:
                print("Negative weight cycle found")
                return
    printSolution(cost, path, n)

    print('====================')
    for i in cost:
        print(i)
    print('====================')
    for i in path:
        print(i)

adjMatrix = [
    [0,     999,    -2,     999],
    [4,     0,      3,      999],
    [999,   999,    0,      2],
    [999,   -1,     999,    0]
]
FloydWarshell(adjMatrix, 4)
