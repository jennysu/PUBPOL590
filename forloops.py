from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/jennysu/Documents/Duke Spring 2015/PubPol590/data/"
git_dir = "/Users/jennysu/GitHub/Pubpol590/"
csv_file = "sample_data_unclean.csv"

# FOR LOOPS
list1 = [[i,v] for i, v in enumerate([5,6,7,8,9])] #enumerate gives index

# iterate through a series
# iteritems() gives index assigned in the data column
# [[i,float(v)] for i, v in df.iteritems()]

# Iterate through a dataframe
[v for v in df]
[df[v] for v in df]
[[i,v] for i, v in df.iteritems()]