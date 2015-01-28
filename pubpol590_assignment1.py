#initialize python script by importing panda and numpy libraries
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#assign the main directory and files to a path
main_dir = "/Users/jennysu/GitHub/PUBPOL590/"
txt_file = "File1_small.txt"

#use the appropriate import function to import that data
df = pd.read_table(main_dir + txt_file, sep = "\s")

#Extract rows 60 to 99 of the DataFrame using row slicing.
df[60:100]

#Extract all the rows where electricity consumption (kwh) is greater than 30.
df[df.kwh > 30]