# Kristin Schaefer
# CS325
# HW6, P2
# Sources: https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

import heapq


def minEffort(puzzle):
    if len(puzzle) == 0:
        return 0

    # convert 2d array puzzle[m][n] into graph for calculate_min_effort()
    starting_vertex = "r" + str(0) + "-" + "c" + str(0)
    end_vertex = "r" + str(len(puzzle)-1) + "-" + "c" + str(len(puzzle[0])-1)
    puzzle_graph = {}

    for m in range(len(puzzle)):
        for n in range(len(puzzle[0])):
            current_cell = "r" + str(m) + "-" + "c" + str(n)
            puzzle_graph[current_cell] = {}
            # if not top row
            if m != 0:
                neighbor_cell = "r" + str(m-1) + "-" + "c" + str(n)
                puzzle_graph[current_cell][neighbor_cell] = abs(puzzle[m][n] - puzzle[m-1][n])
            # if not left column
            if n != 0:
                neighbor_cell = "r" + str(m) + "-" + "c" + str(n-1)
                puzzle_graph[current_cell][neighbor_cell] = abs(puzzle[m][n] - puzzle[m][n-1])
            # if not bottom row
            if m != (len(puzzle)-1):
                neighbor_cell = "r" + str(m+1) + "-" + "c" + str(n)
                puzzle_graph[current_cell][neighbor_cell] = abs(puzzle[m][n] - puzzle[m+1][n])
            # if not rightmost column
            if n != (len(puzzle[0])-1):
                neighbor_cell = "r" + str(m) + "-" + "c" + str(n+1)
                puzzle_graph[current_cell][neighbor_cell] = abs(puzzle[m][n] - puzzle[m][n+1])

    return calculate_min_effort(puzzle_graph, starting_vertex, end_vertex)


def calculate_min_effort(graph, starting_vertex, end_vertex):
    efforts = {vertex: float('infinity') for vertex in graph}
    efforts[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_effort, current_vertex = heapq.heappop(pq)

        # Only process vertex first time we remove it from pq
        if current_effort > efforts[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            effort = weight

            # Only consider path if is better
            if effort < efforts[neighbor]:
                efforts[neighbor] = effort
                heapq.heappush(pq, (effort, neighbor))

    return efforts[end_vertex]


if __name__ == "__main__":
    puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
    print(minEffort(puzzle)) #1

    puzzle2 = [[1, 3, 1, 3], [1, 5, 7, 6], [1, 2, 3, 4], [5, 4, 2, 6]]
    print(minEffort(puzzle2))   #2