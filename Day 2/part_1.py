import numpy as np

solution = 0

with open("input.txt") as file:
    for line in file:
        str_arr = line.split()
        arr = np.array([int(x) for x in str_arr])


        diff = np.diff(arr)
        
        dir = np.sign(diff[0])


        skip = False
        for x in diff:
            if 0==dir or np.sign(x) != dir:
                skip = True
                break
            elif 3 < abs(x) or 0 == x:
                skip = True
                break
        if False == skip:
            solution+=1
print(solution)
