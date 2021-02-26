import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from check_data import check_data, consecutive
from tsAirgap import ts_airgap, ts_heating, ts_nh4
from stineman import slopes, stineman_interp
#from

def na_interpolate(data, option = "linear", maxgap = None) :
  """ Missing Value Imputation by Interpolation
  
  Uses linear, spline or stineman interpolation to replace missing values.

  
  Parameters
  ----------
  data: numpy.array, list or pandas.Series
      Data to impute.

  Returns
  -------
  numpy.array
      Imputed data.
  
  Examples
  ------
  import imputeTSpy
  
  data = imputeTSpy.ts_nh4()
  
  data_fill_locf = imputeTSpy.locf(data)
  data_fill_nocb = imputeTSpy.nocb(data)

  
  """

  x = check_data(data)
  idx = np.arange(x.shape[0])
  nan_idx = idx[np.isnan(x)]
  
    if maxgap != None :
      z = consecutive(nan_idx)
      exc = []
      for i in range(len(z)) :
          if len(z[i]) > maxgap :
              exc.extend(z[i])
      nan_idx = nan_idx[np.isin(nan_idx, exc) == False]
    else :
        pass
  
  
  if option == "linear" :
    f = interp1d(idx[np.isin(idx, nan_idx) == False],
                x[np.isin(idx, nan_idx) == False]   )
    intrep_val = f(idx)
  elif option == "spline" :
    f = interp1d(idx[np.isin(idx, nan_idx) == False],
                x[np.isin(idx, nan_idx) == False], kind= "cubic"   )
    intrep_val = f(idx)
  elif option == "stineman" :
    intrep_val = stineman_interp(idx , idx[np.isin(idx, nan_idx) == False], 
                            x[np.isin(idx, nan_idx) == False], yp = None)
  else :
    raise print("Please fill the valid option!!!")
    
  x[nan_idx] = intrep_val[nan_idx]
  
  return x
    
    
      
#C:/Users/Lenovo/AppData/Local/r-miniconda/envs/

