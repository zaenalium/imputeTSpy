import numpy as np
import pandas as pd
from check_data import check_data, consecutive, power_exp
from tsAirgap import ts_airgap, ts_heating, ts_nh4
#from

def na_ma(data, k = 4, func=np.mean, 
        weighting = None, maxgap = None) :
  """ Missing Value Imputation by Random Sample
  
  Missing value replacement by weighted moving average. Uses semi-adaptive window size to ensure all NAs are replaced  
  
  Parameters
  ----------
  data: numpy.array, list or pandas.Series
      Data to impute.
      
  k: integer width of the moving average window. Expands to both sides of the center element e.g. k=2 means 4 observations (2 left, 2 right) are taken into account. If all observations in the current window are NA, the window size is automatically increased until there are at least 2 non-NA values present.

  weighting:	Weighting to be used. Accepts the following input:
  
              * "simple" - Simple Moving Average (SMA)
              
              * "linear" - Linear Weighted Moving Average (LWMA)
              
              * "exponential" - Exponential Weighted Moving Average (EWMA)
              
  maxgap: Maximum number of successive NAs to still perform imputation on. Default setting is to replace all NAs without restrictions. With this option set, consecutive NAs runs, that are longer than 'maxgap' will be left NA. This option mostly makes sense if you want to treat long runs of NA afterwards separately.
  Returns
  -------
  numpy.array
      Imputed data.
  
  Examples
  ------
  
  k = 4; func=np.mean weighting = None; maxgap = None

  data = ts_nh4()
  import imputetspy
  
  data = imputetspy.ts_nh4()
  
  data_fill_ma = imputetspy.na_ma(data, 4)

  
  """
  
  if (func != np.mean) & (weighting != None) :
    raise("weighting only can be used only if func = np.mean!!!!")
  
  x = check_data(data)
  idx = np.arange(x.shape[0])
  nan_idx = idx[np.isnan(x)]
  non_nan_idx = idx[np.isnan(x) == False]
  if maxgap != None :
    z = consecutive(nan_idx)
    exc = []
    for i in range(len(z)) :
      if len(z[i]) > maxgap :
        exc.extend(z[i])
    nan_idx = nan_idx[np.isin(nan_idx, exc) == False]
  else :
    pass
  prev_k = k//2
  inp = []
  if weighting == None :
    for i in nan_idx :
      try :
        prv = non_nan_idx[(i - non_nan_idx) > 0][-prev_k:]
      except :
        prv = []
      try :
        nxt = non_nan_idx[(non_nan_idx - i) > 0][:prev_k]
      except :
        nxt = []
      to_mv = np.append(prv, nxt)
      inp.append(func(x[to_mv]))
  elif weighting == "linear" :
    for i in nan_idx :
      try :
        prv = non_nan_idx[(i - non_nan_idx) > 0][-prev_k:]
        prv = (1/(np.arange(len(prv)) + 2)) * x[prv]
      except :
        prv = []
      try :
        nxt = non_nan_idx[(non_nan_idx - i) > 0][:prev_k]
        nxt = (1/(np.arange(len(nxt)) + 2)) * x[nxt]
      except :
        nxt = []
      to_mv = np.append(prv, nxt)
      inp.append(np.mean(to_mv))  
  elif weighting == "exponential" :
    for i in nan_idx :
      try :
        prv = non_nan_idx[(i - non_nan_idx) > 0][-prev_k:]
        prv = power_exp(len(prv)) * x[prv]
      except :
        prv = []
      try :
        nxt = non_nan_idx[(non_nan_idx - i) > 0][:prev_k]
        nxt = power_exp(len(nxt)) * x[nxt]
      except :
        nxt = []
      to_mv = np.append(prv, nxt)
      inp.append(np.mean(to_mv))
  else :
    raise('please specify correct weighting!!!!')
  x[nan_idx] = inp
  return x

k = 4; func=np.mean
weighting = None; maxgap = None

    
data = ts_nh4()
