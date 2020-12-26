def tsAirgap():
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
    df = imputeTSpy.tsAirgap()
    df
    # # data structure
    # dat.shape
    # dat.dtypes
    '''
    import pandas as pd
    
    #DATA_FILE = pkg_resources.resource_filename('imputeTSpy', 'data/tsAirgap.csv')
    
    df = pd.read_csv('./imputeTSpy/data/tsAirgap.csv')
 
    return df
