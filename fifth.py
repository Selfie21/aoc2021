import numpy as np

with open("inputs/5", "r") as file:
    lines = file.read().splitlines()

max_x = 0
max_y = 0
coords = []
for line in lines:
    x1, y1 = line.split(' -> ')[0].split(',')
    x2, y2 = line.split(' -> ')[1].split(',')
    coord_pair = [int(x1), int(y1), int(x2), int(y2)]
    if max_x < max(coord_pair[0], coord_pair[2]):
        max_x = max(coord_pair[0], coord_pair[2])
    if max_y < max(coord_pair[1], coord_pair[3]):
        max_y = max(coord_pair[1], coord_pair[3])
    coords.append(coord_pair)

c = np.full((max_x + 1, max_y + 1), 0)

for coord_pair in coords:
    if coord_pair[0] == coord_pair[2]:
        if coord_pair[1] < coord_pair[3]:
            np.add.at(c[:, coord_pair[0]], np.arange(coord_pair[1], coord_pair[3] + 1), 1)
        else:
            np.add.at(c[:, coord_pair[0]], np.arange(coord_pair[3], coord_pair[1] + 1), 1)
    elif coord_pair[1] == coord_pair[3]:
        if coord_pair[0] < coord_pair[2]:
            np.add.at(c[coord_pair[1], :], np.arange(coord_pair[0], coord_pair[2] + 1), 1)
        else:
            np.add.at(c[coord_pair[1], :], np.arange(coord_pair[2], coord_pair[0] + 1), 1)
    else:
        miny = min(coord_pair[0], coord_pair[2])
        maxy = max(coord_pair[0], coord_pair[2])
        direc_y = 1 if coord_pair[0] < coord_pair[2] else -1
        direc_x = 1 if coord_pair[1] < coord_pair[3] else -1
        starty = coord_pair[0]
        startx = coord_pair[1]
        for i in range(miny, maxy + 1):
            c[startx][starty] += 1
            startx += direc_x
            starty += direc_y

print(np.sum(c >= 2))
