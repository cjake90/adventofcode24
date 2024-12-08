import numpy as np
import re

rules_in = []
change_list = []
solution = 0

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
        valid = 1
        #cycle through changes via index, j
        for j in range(len(change)):
            # find list of rules by index (r) that must come after current value (change[j])
            r = np.where(rules[:,0] == change[j])[0]
            # cycle through each matching rule
            for i in r:
                # check if value from the rules comes before the current value
                if rules[i,1] in change[:j]:
                    valid = 0
        if 1 == valid:
            #if no rules were broken, add middle value
            solution+= int(change[(len(change)-1)//2])

    print(solution)

