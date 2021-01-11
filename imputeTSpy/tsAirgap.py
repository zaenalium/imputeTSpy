import numpy as np
import pandas as pd

def ts_airgap():
    '''
    Time series of monthly airline passengers (with missing values)
    ------
    Monthly totals of international airline passengers, 1949 to 1960. This time series contains missing values.
    
    Params
    ------
    
    Returns
    ------
    DataFrame
    
    Examples
    ------
    import imputeTSpy
    
    # load data
    df = imputeTSpy.ts_airgap()
    df
    # # data structure
    # dat.shape
    # dat.dtypes
    '''
    
    
    #DATA_FILE = pkg_resources.resource_filename('imputeTSpy', 'data/tsAirgap.csv')
    
    df = pd.read_csv('data/tsAirgap.csv')
 
    return df
    
    
def ts_nh4():
    '''
    Time series of NH4 concentration in a wastewater system (with missing values)
    ------
    Time series of NH4 concentration in a wastewater system. Measured from 30.11.2010 - 16:10 to 01.01.2011 - 6:40 in 10 minute steps.
    
    Params
    ------
    
    Returns
    ------
    numpy array
    
    Examples
    ------
    import imputeTSpy
    
    # load data
    df = imputeTSpy.ts_nh4()
    df
    # # data structure
    # dat.shape
    # dat.dtypes
    '''
    
    #DATA_FILE = pkg_resources.resource_filename('imputeTSpy', 'data/tsAirgap.csv')
    
    df = np.loadtxt('data/tsNH4.txt', delimiter=",", unpack=False)
 
    return df


def ts_heating ():
    '''
    Time series of a heating systems supply temperature  (with missing values)
    ------
   ime series of a heating systems supply temperature. Measured from 18.11.2013 - 05:12:00 to 13.01.2015 - 15:08:00 in 1 minute steps.
    
    Params
    ------
    
    Returns
    ------
    numpy array
    
    Examples
    ------
    import imputeTSpy
    
    # load data
    df = imputeTSpy.ts_heating()
    df
    # # data structure
    # dat.shape
    # dat.dtypes
    '''
    
    #DATA_FILE = pkg_resources.resource_filename('imputeTSpy', 'data/tsAirgap.csv')
    
    df = np.loadtxt('data/tsHeating.txt', delimiter=",", unpack=False)
 
    return df


