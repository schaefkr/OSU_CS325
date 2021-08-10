# Kristin Schaefer
# CS325
# HW7, P2
# Sources:
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# https://gist.github.com/hayderimran7/09960ca438a65a9bd10d0254b792f48f

import heapq


def Prims(G, starting_vertex):
    #mst to be returned will be list of tuples: (src-dest, weight)
    #mst = []
    mst = set()
    visited = set([starting_vertex])
    # get name and cost of edges connected to starting vertex and heapify
    edges = [(weight, starting_vertex, dest) for dest, weight in G[starting_vertex].items()]
    heapq.heapify(edges)

    while len(edges) > 0:
        # get the edge with the lowest weight in the heap
        edge = heapq.heappop(edges)
        weight, src, dest = edge
        # if the to vertex is not in the visited set, then add it to the set
        if dest not in visited:
            visited.add(dest)
            mst.add(edge)
            # add the edges that connect to the new vertex to the heap if not visited
            for dest_next, weight in G[dest].items():
                if dest_next not in visited:
                    heapq.heappush(edges, (weight, dest, dest_next))

    return sorted(mst)


def make_set(vertex, parent, rank):
    parent[vertex] = vertex
    rank[vertex] = 0


def find(vertex, parent):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex], parent)
    return parent[vertex]


def union(vertex_1, vertex_2, parent, rank):
    root_1 = find(vertex_1, parent)
    root_2 = find(vertex_2, parent)
    if root_1 != root_2:
        if rank[root_1] > rank[root_2]:
            parent[root_2] = root_1
        else:
            parent[root_1] = root_2
        if rank[root_1] == rank[root_2]:
            rank[root_2] += 1


def Kruskal(G):
    parent = dict()
    rank = dict()
    mst = set()

    # create a tree for each vertex in V
    for vertex in G['V']:
        make_set(vertex, parent, rank)

    # store list of edges and sort edges by increasing weight
    edges = sorted(list(G['E']))

    # process edges by smallest weight
    for edge in edges:
        weight, vertex_1, vertex_2 = edge
        # if vertex_1 and vertex_2 not in same tree then union and add to mst
        if find(vertex_1, parent) != find(vertex_2, parent):
            union(vertex_1, vertex_2, parent, rank)
            mst.add(edge)

    return sorted(mst)



if __name__ == "__main__":

    # Test Prims() with graph implemented as dict
    graph_test_Prims = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 3, 'E': 2},
        'C': {'A': 3, 'B': 1, 'E': 1},
        'D': {'B': 3, 'E': 5},
        'E': {'B': 2, 'C': 1, 'D': 5},
    }

    print(Prims(graph_test_Prims, 'A'))

    # Test Kruskal() with graph implemented as dict with list of vertices and edges
    graph_test_Kruskal = {
        'V': ['A', 'B', 'C', 'D', 'E'],
        'E': set([
            (2, 'A', 'B'),
            (3, 'A', 'C'),
            (2, 'B', 'A'),
            (1, 'B', 'C'),
            (3, 'B', 'D'),
            (2, 'B', 'E'),
            (3, 'C', 'A'),
            (1, 'C', 'B'),
            (1, 'C', 'E'),
            (3, 'D', 'B'),
            (5, 'D', 'E'),
            (2, 'E', 'B'),
            (1, 'E', 'C'),
            (5, 'E', 'D')
        ])
    }

    print(Kruskal(graph_test_Kruskal))
