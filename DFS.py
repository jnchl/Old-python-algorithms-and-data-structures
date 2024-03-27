from typing import List, Dict


def DFS(G: Dict[int, List[int]], s: int):
    acyclic = True
    visited: List[int] = []
    stack: List[int] = [s]

    while stack:
        s = stack.pop()

        if s not in visited:
            visited += [s]
            numberOfNeighboursVisited = 0
            for u in G[s]:
                stack.append(u)
                if u in visited:
                    numberOfNeighboursVisited += 1
                    if numberOfNeighboursVisited > 1:
                        acyclic = False

    oldKeys = list(G.keys())
    No = {}
    for i in range(len(visited)):
        No[visited[i]] = oldKeys[i]

    No = {key: No[key] for key in sorted(No.keys())}

    if len(visited) < len(G.keys()):
        cohesion = False
    else:
        cohesion = True

    return No, cohesion, acyclic

def printOutDFSResult(G, s):
    No, cohesion, acyclic = DFS(G, s)
    print("Vertex -> assigned number:")
    print(No)
    print("Graph is cohesive: {}".format(cohesion))
    print("Graph is acyclic: {}\n".format(acyclic))

saList = {1: [2, 6],
2: [1, 3, 8],
3: [2, 5, 7, 9, 10],
4: [6],
5: [3],
6: [1, 4],
7: [3],
8: [2],
9: [3],
10: [3]}

printOutDFSResult(saList, 2)
