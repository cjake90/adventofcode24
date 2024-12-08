import numpy as np
arr = []
solution = 0

with open("input.txt") as file:
    for line in file:
        arr.append(list(line.replace("\n","")))
    np_arr = np.array(arr)


    for x in range(1, np_arr.shape[0]-1):
        for y in range(1, np_arr.shape[1]-1):
            # searching array for "A", but skipping outer border since x cannot occur there 
            if "A" == np_arr[x][y]:
                #checking if the first diagonal has a MAS
                if ("M" == np_arr[x-1][y-1] and "S" == np_arr[x+1][y+1]) or ("S" == np_arr[x-1][y-1] and "M" == np_arr[x+1][y+1]):
                    #cehcking if second diagonal has a MAS
                    if ("M" == np_arr[x-1][y+1] and "S" == np_arr[x+1][y-1]) or ("S" == np_arr[x-1][y+1] and "M" == np_arr[x+1][y-1]):

                        solution+=1

    print(solution)