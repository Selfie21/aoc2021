# 0 lowest 9 highest
# risk level 1 plus its height
# sum of all risk level low points
from collections import deque

import numpy as np

with open("inputs/9", "r") as file:
    lines = file.read().splitlines()
    height_map = np.array([[int(char) for char in line] for line in lines])

LINE_LENGTH = len(height_map[0]) - 1
NO_LINES = len(height_map) - 1

def check_for_corner(i, j):
    if i == 0 and j == 0:
        return 1
    if i == 0 and j == LINE_LENGTH:
        return 2
    if i == NO_LINES and j == 0:
        return 3
    if i == NO_LINES and j == LINE_LENGTH:
        return 4
    else:
        return 0

def check_for_edge(i, j):
    if i == 0:
        return 1
    if j == LINE_LENGTH:
        return 2
    if j == 0:
        return 3
    if i == NO_LINES:
        return 4
    else:
        return 0

with open("inputs/9", "r") as file:
    lines = file.read().splitlines()
    height_map = np.array([[int(char) for char in line] for line in lines])

total = 0
for i, row in enumerate(height_map):
    # x, y
    corner_mapping = {1: [1, 1], 2: [-1, 1], 3: [1, -1], 4: [-1, -1]}
    edge_mapping = {1: [1, 1, -1], 2: [-1, 1, -1], 3: [1, -1, 1], 4: [1, -1, -1]}

    for j, height_level in enumerate(row):
        corner_check = check_for_corner(i, j)
        edge_check = check_for_edge(i, j)

        if corner_check != 0:
            if height_map[i + corner_mapping[corner_check][1], j] > height_level and height_map[i, j + corner_mapping[corner_check][0]] > height_level:
                total += height_level + 1
        elif (edge_check == 1) or (edge_check == 4):
            if height_map[i + edge_mapping[edge_check][1], j] > height_level and height_map[i, j + edge_mapping[edge_check][0]] > height_level and height_map[i, j + edge_mapping[edge_check][2]] > height_level:
                total += height_level + 1
        elif (edge_check == 2) or (edge_check == 3):
            if height_map[i + edge_mapping[edge_check][1], j] > height_level and height_map[i, j + edge_mapping[edge_check][0]] > height_level and height_map[i + edge_mapping[edge_check][2], j] > height_level:
                total += height_level + 1
        else:
            if height_map[i + 1, j] > height_level and height_map[i - 1, j] > height_level and height_map[i, j + 1] > height_level and height_map[i, j - 1] > height_level:
                total += height_level + 1
print(total)

