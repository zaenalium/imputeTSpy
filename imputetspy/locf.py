import numpy as np
import pandas as pd
from imputetspy.check_data import check_data, consecutive
from imputetspy.data import ts_airgap, ts_heating, ts_nh4
#from impyute.ops import error


def locf(data, na_remaining = "rev", maxgap = None):
    """ Last Observation Carried Forward
    
    For each set of missing indices, use the value of one row before(same
    column). In the case that the missing value is the first row, look one
    row ahead instead. If this next row is also NaN, look to the next row.
    Repeat until you find a row in this column that's not NaN. All the rows
    before will be filled with this value.
    
    Parameters:
        data: numpy.array, list or pandas.Series
            Data to impute.
        na_remaining : Method to be used for remaining nan (if missing number apear in the first observation) :
            "keep" - to return the series with NAs
            "mean" - to replace remaining NAs by overall mean
            "rev" - to perform nocb / locf from the reverse direction
        maxgap : Maximum number of successive NAs to still perform imputation on. Default setting is to replace all NAs without restrictions. With this option set, consecutive nan runs, that are longer than 'maxgap' will be left nan. This option mostly makes sense if you want to treat long runs of nan afterwards separately
    
    Returns:
        numpy.array imputed data.
        
    Examples:
        >>> import imputeTSpy
        
        >>> data = imputeTSpy.ts_nh4()
        
        >>> data_fill_locf = imputeTSpy.locf(data)
        >>> data_fill_nocb = imputeTSpy.nocb(data)
    
    """
    data = check_data(data)
    nan_xy = np.argwhere(np.isnan(data))
    nan_xy_idx = np.array([x[0] for x in nan_xy])
    
    if maxgap != None :
        z = consecutive(nan_xy_idx)
        exc = []
        for i in range(len(z)) :
            if len(z[i]) > maxgap :
                exc.extend(z[i])
        nan_xy_idx = nan_xy_idx[np.isin(nan_xy_idx, exc) == False]
    else :
        pass
    
    n = data.shape[0]
    n_int = np.arange(n)#[x for x in range(n)]
    
    data_cp = data.copy()
    
    for i in nan_xy_idx :
        try :
            cdd = n_int [n_int > i]
            idx_rep = np.min(cdd[np.isin(cdd, nan_xy_idx) == False])
            data_cp[i] = data_cp[idx_rep]
        except :
            if na_remaining == "rev" :
                cdd = n_int [n_int < i]
                idx_rep = np.max(cdd[np.isin(cdd, nan_xy_idx) == False])
                data_cp[i] = data_cp[idx_rep]
            elif na_remaining == "mean":
                idx_rep = np.mean(data[np.isnan(data) == False])
                data_cp[i] = idx_rep
            elif na_remaining == "keep":
                pass
            else :
                raise("the option is invalid, please fill valid option!!!!")
    return data_cp
        

def nocb(data, axis=0, na_remaining = "rev", maxgap = None):
    """ Next Observation Carried Backward

    For each set of missing indices, use the value of one row before(same
    column). In the case that the missing value is the first row, look one
    row ahead instead. If this next row is also NaN, look to the next row.
    Repeat until you find a row in this column that's not NaN. All the rows
    before will be filled with this value.

    Parameters:
        data: numpy.array, list or pandas.Series
            Data to impute.
        na_remaining : Method to be used for remaining nan (if missing number apear in the first observation) :
            "keep" - to return the series with NAs
            "mean" - to replace remaining NAs by overall mean
            "rev" - to perform nocb / locf from the reverse direction
        maxgap : Maximum number of successive NAs to still perform imputation on. Default setting is to replace all NAs without restrictions. With this option set, consecutive nan runs, that are longer than 'maxgap' will be left nan. This option mostly makes sense if you want to treat long runs of nan afterwards separately

    Returns:
        numpy.ndarray Imputed data.
    
    Examples:
        >>> import imputeTSpy
        
        >>> data = imputeTSpy.ts_nh4()
        
        >>> data_fill_locf = imputeTSpy.locf(data)
        >>> data_fill_nocb = imputeTSpy.nocb(data)
    """
    data = check_data(data)
    nan_xy = np.argwhere(np.isnan(data))
    nan_xy_idx = np.array([x[0] for x in nan_xy])
    
    if maxgap != None :
        z = consecutive(nan_xy_idx)
        exc = []
        for i in range(len(z)) :
            if len(z[i]) > maxgap :
                exc.extend(z[i])
        nan_xy_idx = nan_xy_idx[np.isin(nan_xy_idx, exc) == False]
    else :
        pass
    
    n = data.shape[0]
    n_int = np.arange(n)#[x for x in range(n)]
    
    data_cp = data.copy()
    
    for i in nan_xy_idx :
        try :
            cdd = n_int [n_int < i]
            idx_rep = np.min(cdd[np.isin(cdd, nan_xy_idx) == False])
            data_cp[i] = data_cp[idx_rep]
        except :
            if na_remaining == "rev" :
                cdd = n_int [n_int > i]
                idx_rep = np.max(cdd[np.isin(cdd, nan_xy_idx) == False])
                data_cp[i] = data_cp[idx_rep]
            elif na_remaining == "mean":
                idx_rep = np.mean(data[np.isnan(data) == False])
                data_cp[i] = idx_rep
            elif na_remaining == "keep":
                pass
            else :
                raise("the option is invalid, please fill valid option!!!!")
    return data_cp
    
    
#data = ts_nh4()
#data[-2:] =[np.nan, np.nan]
#nan_xy = np.argwhere(np.isnan(data))
#nan_xy_idx = np.array([x[0] for x in nan_xy])
#n = data.shape[0]
#n_int = np.arange(n)#[x for x in range(n)]
#
#np.diff(np.append(i, z)) != 1
#max_gap = 10
#
#    
##z = nan_xy_idx[nan_xy_idx > i]
##a = np.array([0, 47, 48, 49, 50, 97, 98, 99])
#if maxgap != None :
#    z = consecutive(nan_xy_idx)
#    exc = []
#    for i in range(len(z)) :
#        if len(z[i]) > max_gap :
#            exc.extend(z[i])
#    nan_xy_idx = nan_xy_idx[np.isin(nan_xy_idx, exc) == False]
#else :
#    pass
#
#data_cp = data.copy()
#na_remaining = "mean"
#for i in nan_xy_idx :
#    try :
#        cdd = n_int [n_int > i]
#        idx_rep = np.min(cdd[np.isin(cdd, nan_xy_idx) == False])
#        data_cp[i] = data_cp[idx_rep]
#    except :
#        if na_remaining == "rev" :
#            cdd = n_int [n_int < i]
#            idx_rep = np.max(cdd[np.isin(cdd, nan_xy_idx) == False])
#            data_cp[i] = data_cp[idx_rep]
#        elif na_remaining == "mean":
#            idx_rep = np.nanmean(data)
#            data_cp[i] = idx_rep
#        elif na_remaining == "keep":
#            pass
#        else :
#            raise("the option is invalid, please fill valid option!!!!")
#        
#            
#z = nan_xy_idx[nan_xy_idx > i]   
        
