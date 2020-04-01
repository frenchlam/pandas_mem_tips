import pandas as pd 

def read_filtered( file, filter_cols ):
  return pd.read_csv(input_file,sep=',',header=0, na_values='NA',usecols=filter_cols )

input_file = "data/1988.csv.bz2"
cols=['Month','DayofMonth','DayOfWeek','CRSDepTime','UniqueCarrier','FlightNum','Origin','Dest','Cancelled']

#read data
df=read_filtered(input_file,cols)
df.info()
df.memory_usage(deep=True)
init_size = df.memory_usage(deep=True).sum()


#change categorical features
col_to_cat = ['UniqueCarrier','Origin','Dest','Cancelled']
df[col_to_cat] = df[col_to_cat].apply(pd.DataFrame.astype,dtype='category')

#change interger to unsigned
col_to_int = ['Month','DayofMonth','DayOfWeek','CRSDepTime','FlightNum','Cancelled']
df[col_to_int] = df[col_to_int].apply(pd.to_numeric, downcast='unsigned')

df.info()
df.memory_usage(deep=True)
final_size = df.memory_usage(deep=True).sum()

#calculate memory footprint dif

reduction = round((final_size/init_size)*100,2)
"final dataframe weighs {}% of the original".format(reduction)