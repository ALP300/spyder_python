import pandas as pd
import numpy as np

df= pd.read_csv("DatosYT.csv")
print(df.dtypes)
print(df.sort_values(by=['xs'], ascending=[True]))
df1= pd.DataFrame(np.sort(df.values, axis=0), index= df.index, columns= 
                  df.columns)
print(df1)