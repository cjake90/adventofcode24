import re
import numpy as np

solution = 0
arr = []
diag = []

def diagelem(ll, a, b):
    try:
        if a < 0 or b < 0:
            raise IndexError
        return ll[a, b]
    except IndexError:
        return None

def get_diagonals(arr):
    dd = []
    for j in range(-arr.shape[0]+1, arr.shape[0]):
        dd.append([diagelem(arr, i, i+j) for i in range(arr.shape[1])])

    for j in range(0, 2*arr.shape[0]):
        dd.append([diagelem(arr, i, -i+j) for i in range(arr.shape[1])])
    diagonals = []
    for diag in dd:
        diagword = ''.join([letter for letter in diag if letter is not None])
        if len(diagword) > 0:
            diagonals.append(diagword)
    return diagonals


def find_xmas(text):
    m = re.findall('XMAS',text)
    m.extend(re.findall('SAMX',text))
    return len(m)

with open("input.txt") as file:
    for line in file:
        solution += find_xmas(line)
        arr.append(list(line.replace("\n","")))
    np_arr = np.array(arr)
    
    for col in np_arr.T:
        solution += find_xmas(''.join([letter for letter in col if letter is not None]))
    
    diag_array = get_diagonals(np_arr)
    for diag in diag_array:
        solution += find_xmas(diag)

print(solution)