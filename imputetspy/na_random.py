import numpy as np
import pandas as pd
from imputetspy.check_data import check_data, consecutive
from imputetspy.data import ts_airgap, ts_heating, ts_nh4
#from

def na_random(data, lower_bound = None, upper_bound = None, maxgap = None) :
    """ Missing Value Imputation by Random Sample
    
    Replaces each missing value by drawing a random sample between two given bounds based on uniform distribution.
    
    Parameters:
        data (float): numpy.array, list or pandas.Series data to impute.
        lower_bound (float): minimum number of the random data (lower bound of uniform distribution), if empty the parameter will be the minimum of the data.
        upper_bound (float): maximum number of the random data (upper bound of uniform distribution), if empty the parameter will be the maximum of the data.
        maxgap (int): Maximum number of successive NAs to still perform imputation on. 
                Default setting is to replace all NAs without limitation. 
                With this option set, consecutive NAs runs, that are longer than 'maxgap' will be left NA. 
                This option mostly makes sense if you want to treat long runs of NA afterwards separately.
    Returns:
        numpy.array Imputed data.
    
    Examples:

        >>> import imputeTSpy
        
        >>> data = imputeTSpy.ts_nh4()
        
        >>> data_fill_random = imputeTSpy.na_random(data)

    
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
    
    if lower_bound == None :
        lower_bound = np.nanmin(x)
    
    
    if upper_bound == None :
        upper_bound = np.nanmax(x)
        
    inp = []
    for i in range(len(nan_idx)) : 
        inp.append(np.random.uniform(lower_bound, upper_bound))
        
    
    x[nan_idx] = inp
    
    return x
