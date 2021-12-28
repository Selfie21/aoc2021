from collections import deque

graph = {'a': ['b', 'c'],
         'b': ['d'],
         'c': ['e'],
         'd': ['f', 'g'],
         'e': ['g', 'h'],
         'f': [],
         'g': [],
         'h': []}

visited = []
stack = []
stack.append('a')

while stack:
    current_elem = stack.pop()

    not_visited_neighbours = filter(lambda x: x not in visited, graph[current_elem])

    if not not_visited_neighbours:
        continue

    for neighbour in not_visited_neighbours:
        if neighbour not in visited:
            stack.append(neighbour)

    visited.append(current_elem)


def dfs(visited, current):
    if current in visited:
        return
    else:
        visited.append(current)
        for node in graph[current]:
            dfs(visited, node)


dfs([], 'a')
