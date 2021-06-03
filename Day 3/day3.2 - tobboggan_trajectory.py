with open("Day 3/day3.txt", "r") as f:
    file = f.read().splitlines()


trajectory = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
number_of_lines = len(file)
line_length = len(file[0])
steps = 0
line_number = 0
trees = 0
slope_number = 0
trees_num = []
while slope_number != len(trajectory):
    steps += trajectory[slope_number][0]
    line_number += trajectory[slope_number][1]
     
    if steps >= line_length:
        steps = steps % line_length
    
    if file[line_number][steps] == '#':
        trees += 1
    if line_number == number_of_lines - 1:
        slope_number += 1
        steps = 0
        line_number = 0
        trees_num.append(trees)
        trees = 0
               
print(trees_num[0] * trees_num[1] * trees_num[2] * trees_num[3] * trees_num[4])