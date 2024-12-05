import pandas as pd
import numpy as np

#import the list of frequency changes and create frequency int
df = pd.read_csv('input.txt', header=None, sep='   ')

loc0 = df[0].to_numpy()
loc1 = df[1].to_numpy()

solution = 0

for x in loc0:
    for y in loc1:
        if x == y:
            solution += x
print(solution)
