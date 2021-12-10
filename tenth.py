points_dict = {')': 1, ']': 2, '}': 3, '>': 4}
opening_chars = ['(', '[', '{', '<']
complementary = {'(': ')', '[': ']', '{': '}', '<': '>'}


def incomplete_checker(syntax):
    openings = []
    for char in syntax:
        if char in opening_chars:
            openings.append(complementary[char])
        else:
            if char == openings[-1]:
                openings.pop()
            else:
                return 0
    if openings:
        score = 0
        for closing_bracket in reversed(openings):
            score *= 5
            score += points_dict[closing_bracket]
        return score
    return 0


with open("inputs/10", "r") as file:
    lines = file.read().splitlines()

scores = []
for line in lines:
    score = incomplete_checker(line)
    if score != 0:
        scores.append(incomplete_checker(line))
scores.sort()
print(scores[int(len(scores)/2)])
