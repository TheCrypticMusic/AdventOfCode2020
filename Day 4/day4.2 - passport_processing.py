with open("day4.txt") as f:
    file = f.read().split("\n\n")

file = [i.replace("\n", " ") for i in file]

ecl = {"amb": "", "blu": "", "brn": "", "gry": "", "grn": "", "hzl": "", "oth": ""}
required_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False}
formatted_file = [line.split() for line in file]
count = 0
for i in formatted_file:
    for j in i:
        key = j.split(":")[0]
        value = j.split(":")[1]
        if key in required_fields:
            if key == "byr" and 1920 <= int(value) <= 2002:
                print(key, value)
                required_fields[key] = True
            elif key == "iyr" and int(value) >= 2010 and int(value) <= 2020:
                print(key, value)
                required_fields[key] = True
            elif key == "eyr" and int(value) >= 2020 and int(value) <= 2030:
                print(key, value)
                required_fields[key] = True
            elif key == "hgt" and "cm" in value or "in" in value:
                if "cm" in value:

                    value = value.replace("cm", "")
                    if int(value) >= 150 and int(value) <= 193:
                        print(key, value)
                        required_fields[key] = True
                if "in" in value:
                    value = value.replace("in", "")
                    if int(value) >= 59 and int(value) <= 76:
                        print(key, value)
                        required_fields[key] = True
            elif key == "hcl" and len(value) == 7:
                print(key, len(value), value)
                required_fields[key] = True
            elif key == "ecl" and value in ecl:
                print(key, value)
                required_fields[key] = True
            elif key == "pid" and len(value) == 9:
                print(key, len(value), value)
                required_fields[key] = True
    if all(value == 1 for value in required_fields.values()):
        count += 1
        required_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}
    else:
        required_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}
print(count)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.