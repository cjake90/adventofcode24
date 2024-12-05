import numpy as np

solution = 0

def check_if_safe(arr):
    dir = np.sign(arr[0])
    for x in diff:
        if 0==dir or np.sign(x) != dir:
            return False
        elif 3 < abs(x) or 0 == x:
            return False
    return True


with open("input.txt") as file:
    for line in file:
        str_arr = line.split()
        arr = np.array([int(x) for x in str_arr])


        diff = np.diff(arr)
        
        if check_if_safe(diff):
            solution+=1
print(solution)
