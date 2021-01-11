def check_data(data) :  
  data_type = str(type(data))
  if ("list" in data_type) :
    x = np.asarray(data)
  elif ("series" in data_type) :
    x = data.values
  elif ("array" in data_type) :
    x = data.copy()
  else :
    print("this function are available for single columns data, please do not use pd.DataFrame")
  return x

def consecutive(data, stepsize=1):
  return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)
