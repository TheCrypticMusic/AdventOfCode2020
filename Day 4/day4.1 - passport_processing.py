with open("Day 4/day4.txt") as f:
    file = f.read()


formatted_file = file.split("\n\n")

passports = []
for line in formatted_file:
    passports.append(line.replace("\n", " ").split())

count = 0
details_count = 0
for passport in passports:
    if len(passport) == 8:
        count += 1
    elif len(passport) == 7:
        for details in passport:
            details = details.split(":")
            if details[0] != "cid":
                details_count += 1
            if details[0] == "cid":
                details_count = 0
                break
            if details_count == 7:
                details_count = 0
                count += 1
        
print(count)
                
        

                
                