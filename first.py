file = open("inputs/1", "r")
lines = file.read().splitlines()
lines = [int(line) for line in lines]

# a
bb = list(map((lambda x, y: x > y), lines[1:], lines))

# b
cc = list(map((lambda x, y, z: x+y+z), lines, lines[1:], lines[2:]))
dd = list(map((lambda x, y: x > y), cc[1:], cc))

print(sum(bb))
print(sum(dd))
