import pandas as pd
import numpy as np

#import the list of frequency changes and create frequency int
df = pd.read_csv('input.txt', header=None, sep='   ')

loc0 = np.sort(df[0].to_numpy())
loc1 = np.sort(df[1].to_numpy())
print(np.sum(abs(loc0 - loc1)))

