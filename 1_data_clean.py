from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/jennysu/Documents/Duke Spring 2015/PubPol590/data/"
git_dir = "/Users/jennysu/GitHub/Pubpol590/"
csv_file = "sample_data_unclean.csv"

df = pd.read_csv(os.path.join(main_dir,csv_file))

# converting lists to series and dataframe
list4 = range(100,105)
list5 = range(5)
list6 = range(10,15)

s1 = Series(list4)
s2 = Series(list5)

zip1 = zip(list4,list5) # makes pairwise joins
zip2 = zip(list4,list5,list6)
df1 = DataFrame(zip1)
df2 = DataFrame(zip1, columns = ['two', ':)'])
df3 = DataFrame(zip2, columns = [2, '2', ':)'])

df3[['2',':)']][3:4]

#make a dataframe using dict notation
df4 = DataFrame({':(':list4,9 : list6}) #lists must be same length
