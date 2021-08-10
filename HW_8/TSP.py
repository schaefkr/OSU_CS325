# Kristin Schaefer
# CS325
# HW9, EXTRA CREDIT
# Sources:
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/

import heapq


def Prims(G, starting_vertex):
    # mst to be returned will be list of tuples: (src-dest, weight)
    # mst = []
    mst = set()
    visited = set([starting_vertex])
    # get name and cost of edges connected to starting vertex and heapify
    edges = [(weight, starting_vertex, dest) for dest, weight in
             G[starting_vertex].items()]
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


def approx_tsp_algo(G, starting_vertex):

    # compute MST from Prims
    MST = Prims(G, starting_vertex)

    # traverse MST pre-order to get the walk of MST
    visited = set()
    ham_cycle = []
    for edge in MST:
        w, vi, vj = edge
        if vi not in visited:
            ham_cycle.append(vi)
            visited.add(vi)
        if vj not in visited:
            ham_cycle.append(vj)
            visited.add(vj)

    ham_cycle.append(starting_vertex)
    return ham_cycle


if __name__ == "__main__":
    # Test Prims() with graph implemented as dict
    graph_test = {
        'A': {'B': 1, 'C': 3, 'D': 7},
        'B': {'A': 1, 'C': 2, 'D': 3},
        'C': {'A': 3, 'B': 2, 'D': 1},
        'D': {'A': 7, 'B': 3, 'C': 1},
    }
    print(approx_tsp_algo(graph_test, 'A'))
