file = open("inputs/2", "r")
lines = file.read().splitlines()
lines = [str(line) for line in lines]

hori = 0
depth = 0
for line in lines:
    if line[:8] == 'forward ':
        hori += int(line[8])
    elif line[:5] == 'down ':
        depth += int(line[5])
    elif line[:3] == 'up ':
        depth -= int(line[3])


hori = 0
depth = 0
aim = 0
for line in lines:
    if line[:8] == 'forward ':
        hori += int(line[8])
        depth += (aim * int(line[8]))
    elif line[:5] == 'down ':
        aim += int(line[5])
    elif line[:3] == 'up ':
        aim -= int(line[3])

print(hori * depth)
