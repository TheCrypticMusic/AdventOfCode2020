with open("day6") as f:
    file = f.read().split("\n\n")

new_file = [x.replace("\n", "") for x in file]
count = 0

for line in new_file:
    count += len(set(line))

print(count)