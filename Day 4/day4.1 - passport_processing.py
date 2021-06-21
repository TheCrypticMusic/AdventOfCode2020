with open("day4.txt") as f:
    file = f.read().split("\n\n")

file = [i.replace("\n", " ") for i in file]

required_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False}
formatted_file = [line.split() for line in file]
count = 0
for i in formatted_file:
    for j in i:
        key = j.split(":")[0]
        if key in required_fields:
            required_fields[key] = True

    if all(value == 1 for value in required_fields.values()):
        count += 1
        required_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}
    else:
        required_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}
print(count)



