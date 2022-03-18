# Below application is used to demonstrates creation of Panel using Pandas
import pandas as pd
import numpy as np
import xarray as xr

df1 = {'one':pd.Series([1,2,3],index=['a','b','c']),
       'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}

df2 = {'one':pd.Series([1,2,3],index=['a','b','c']),
       'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}

data ={'item1':df1,'item2':df2}

# p = xr.DataArray(data)
p = np.array(data)
print(p)
