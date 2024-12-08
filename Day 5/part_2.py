import numpy as np
import re

rules_in = []
change_list = []
solution1 = 0
solution2 = 0

def check_validity(change, rules):
    #cycle through changes via index, j
    for j in range(len(change)):
            # find list of rules by index (r) that must come after current value (change[j])
        r = np.where(rules[:,0] == change[j])[0]
        # cycle through each matching rule
        for i in r:
            # check if value from the rules comes before the current value
            if rules[i,1] in change[:j]:
                return [j,change.index(rules[i,1])]
    return [0,0]


with open("input.txt") as file:
    for line in file:
        line = line.replace("\n","")
        if "|" in line:
            rules_in.append(re.split(r"\|",line))
        elif "," in line:
            change_list.append(re.split(r",",line))
    
    rules = np.array(rules_in)
    #change_list = np.array(change_in)
    
    for change in change_list:
        rule_break = check_validity(change, rules)
        if [0,0] == rule_break:
            solution1 += int(change[(len(change)-1)//2])
        else:
            print(f'bad change is {change}')
            while [0,0] != rule_break:
                new_change = change
                # move the value with a number that can't come before it to the beginning of the list
                new_change.insert(rule_break[1], new_change.pop(rule_break[0]))
                print(f'new change is {new_change}')
                rule_break = check_validity(new_change, rules)
            solution2 += int(change[(len(change)-1)//2])



    print(f'Solution to part 1 is {solution1}')
    print(f'Solution to part 2 is {solution2}')

