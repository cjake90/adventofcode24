import numpy as np

solution = 0

def check_array(arr):
    dir = np.sign(arr[0])
    if 0==dir:
        return 1 # position of bad value
    for x in range(arr.size):
        if np.sign(arr[x]) != dir:
            return x+1
        elif 3 < abs(arr[x]) or 0 == arr[x]:
            return x+1
    return 0


with open("input.txt") as report:
    for line in report:
        str_arr = line.split()
        levels = np.array([int(x) for x in str_arr])

        for x in range(levels.size):
            temp = np.delete(levels, x)
            if(0==check_array(np.diff(temp))):
                solution+=1
                break

            
print(solution)
