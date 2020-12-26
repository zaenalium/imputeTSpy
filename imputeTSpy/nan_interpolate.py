import numpy as np
import pandas as pd
import scipy
import types

def na_interpolate(data, option = "linear", maxgap = np.inp) :
    data_type = str(type(data))
    if ("list" in data_type) :
      x = pd.Series(data)
    elif ("array" in data_type) :
      x = pd.Series(data)
    elif ("array" in data_type) :
      x = data.copy()
    else :
      print("this function are available for single columns data, please do not use pd.DataFrame")
     
      
#C:/Users/Lenovo/AppData/Local/r-miniconda/envs/

conda_install("impyute", envname = "r-reticulate", pip = TRUE)
