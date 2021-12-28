import copy
from collections import Counter

with open("inputs/12") as file:
    graph = file.read().splitlines()
    graph = [l.split('-') for l in graph]


def search_for_adjacent(graph, node):
    all_adjacent = []
    for line in graph:
        if node == line[0]:
            all_adjacent.append(line[1])
        elif node == line[1]:
            all_adjacent.append(line[0])
    return all_adjacent


def check_double(already_visited):
    tmp = ['start']
    found_two = False
    counts = Counter(already_visited)

    for cave in counts:
        if counts[cave] >= 2:
            found_two = True

    if found_two:
        for cave in counts:
            if cave not in ['start', 'end']:
                tmp.append(cave)
    return tmp




stack = []
current_path = []
all_paths = []
current_path.append('start')
stack.append(current_path)

while stack:
    current_path = stack.pop()
    current_elem = current_path[-1]

    if current_elem == 'end':
        all_paths.append(copy.deepcopy(current_path))
        current_path.pop()
        continue

    visited = check_double(list(filter(lambda x: x.islower(), current_path)))
    not_visited_neighbours = list(filter(lambda x: x not in visited, search_for_adjacent(graph, current_elem)))

    # no new neighbours found
    if not not_visited_neighbours:
        current_path.pop()
        continue

    for neighbour in not_visited_neighbours:
        if neighbour not in visited:
            tmp = copy.deepcopy(current_path)
            tmp.append(neighbour)
            stack.append(tmp)

tmp = set(tuple(x) for x in all_paths)
print(len(set(tuple(x) for x in all_paths)))

