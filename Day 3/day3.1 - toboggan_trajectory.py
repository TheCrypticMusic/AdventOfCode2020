with open("Day 3/day3.txt", "r") as f:
    file = f.read().splitlines()

number_of_lines = len(file)
line_length = len(file[0])
three_steps_index = 0
line_index = 0
trees = 0
while line_index < number_of_lines - 1:
    three_steps_index += 3
    line_index += 1
    if three_steps_index >= line_length:
        three_steps_index = three_steps_index % line_length
    if file[line_index][three_steps_index] == '#':
        trees += 1

print(trees)
