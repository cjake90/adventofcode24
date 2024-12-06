import re


solution = 0

with open("input.txt") as comp_memory:
    for line in comp_memory:
        temp = line
        m = re.findall('mul\(\d+,\d+\)', temp)

        for x in m:
            a = re.findall('\d+', x)
            solution += int(a[0]) * int(a[1])
print(solution)
        