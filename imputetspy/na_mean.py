import numpy as np
import pandas as pd
from imputetspy.check_data import check_data, consecutive
from imputetspy.data import ts_airgap, ts_heating, ts_nh4
from scipy.stats import gmean, hmean, mode

def na_mean(data, option = "mean", maxgap = None) :
    """ Missing Value Imputation by Average values (can use median & mode as well)
    
    Missing value replacement by overall mean (or other metric) values.    
    
    Parameters
    ----------
    data: numpy.array, list or pandas.Series
            Data to impute.
            
    option:Algorithm to be used. Accepts the following input:
        * "mean" - take the mean for imputation (default choice)
        * "median" - take the median for imputation
        * "mode" - take the mode for imputation
        * "harmonic" - take the harmonic mean
        * "geometric" - take the geometric mean
                            
    maxgap: Maximum number of successive NAs to still perform imputation on. Default setting is to replace all NAs without limitation. With this option set, consecutive NAs runs, that are longer than 'maxgap' will be left NA. This option mostly makes sense if you want to treat long runs of NA afterwards separately.
    Returns
    -------
    numpy.array
            Imputed data.
    
    Examples
    ------
    
    data = ts_nh4()
    import imputetspy
    
    data = imputetspy.ts_nh4()
    
    data_fill_mean = imputetspy.na_mean(data, option = 'mean')

    data_fill_med = imputetspy.na_mean(data, option = 'median')

    
    """
    

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
    
    if option == "mean" :
        val = np.nanmean(x)
    elif option == "median" :
        val = np.nanmedian(x)
    elif option == "harmonic" :
        val = hmean(x[np.isnan(x)])
    elif option == "geometric" :
        val = gmean(x[np.isnan(x)])
    elif option == "mode" :
        val = mode(x[np.isnan(x)])
    
    x[nan_idx] = val
    
    return x
