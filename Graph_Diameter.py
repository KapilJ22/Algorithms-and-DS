from collections import defaultdict, deque
import enum


Not_Visited = 0
Visiting = 1
Visited = 2


graph = {
    'a': ['b', 'd', 'e'],
    'b': ['c', 'f'],
    'c': [],
    'd': ['e'],
    'e': ['i'],
    'f': ['h', 'g'],
    'g': [],
    'i': [],
    'h': ['i']
}
status = defaultdict(int)

max_path_nodes = defaultdict(int)


def dfs_path(v1, v2):
    global max_path_nodes
    if v1 == v2:
        return 0
#     if max_path_nodes[(v1, v2)] == 0:
        # max_path_nodes[(v1, v2)] = 1 + max([dfs_path(nbr, v2)
        #     for nbr in graph[v1]])
    for nbr in graph[v1]:
        max_path_nodes[(v1, v2)] = max(
            max_path_nodes[(v1, v2)], 1 + dfs_path(nbr, v2))

    return max_path_nodes[(v1, v2)]


def max_path(graph):
    max_path = 0
    for v1 in graph.keys():
        for v2 in graph.keys():
            max_path = max(max_path, dfs_path(v1, v2))

    return max_path


# print(dfs_path('a', 'i'))
print(max_path(graph))
