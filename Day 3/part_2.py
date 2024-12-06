import re


solution = 0
do = True

with open("input.txt") as comp_memory:
    for line in comp_memory:
        s = re.split(r"(don?'?t?\(\))", line) #splitstring including "do()"/"don't()"
         
        for x in range(len(s)):
            if "don't()" == s[x]: #if "don't()" present, skip until "do()"
                do = False
            elif "do()" == s[x]: #if "do()" present, process until "don't()"
                do = True
            elif do:
                m = re.findall(r'mul\(\d+,\d+\)', s[x]) #extract mul(#,#) strings
                for y in m:
                    a = re.findall(r'\d+', y) #extract numbers from mul(#,#) strings
                    solution += int(a[0]) * int(a[1])

print(solution)
        