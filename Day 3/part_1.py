import re


solution = 0

with open("input.txt") as comp_memory:
    for line in comp_memory:
        m = re.findall(r'mul\(\d+,\d+\)', line) #extract mul(#,#) strings

        for x in m:
            a = re.findall(r'\d+', x) #extract ints from mul(#,#) strings
            solution += int(a[0]) * int(a[1])
print(solution)
        