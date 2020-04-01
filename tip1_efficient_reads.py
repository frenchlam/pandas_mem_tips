import pandas as pd 
from memory_profiler import profile

input_file = "data/1988.csv.bz2"
cols=['Month','DayofMonth','DayOfWeek','CRSDepTime','UniqueCarrier','FlightNum','Origin','Dest','Cancelled']

#standard filter
@profile(precision=2)
def read_and_filter( file, filter_cols ): 
  return pd.read_csv(input_file,sep=',',header=0, na_values='NA')[filter_cols]

#better filter 
@profile(precision=2)
def read_filtered( file, filter_cols ):
  return pd.read_csv(input_file,sep=',',header=0, na_values='NA',usecols=filter_cols )

#read_and_filter(input_file,cols).info()

read_filtered(input_file,cols).info()

#launch from command line or python console using : 
#!python3 -m memory_profiler tip1_efficient_reads.py