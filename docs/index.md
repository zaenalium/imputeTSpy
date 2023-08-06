# ImputeTSpy: Missing Values Imputation for Time Series Data

Imputation method for time series data inspired by *imputeTS* package in R. Most of this kind of package are available in R, however, when we use the package for interfacing python to R is somehow complicated, and need to install a lot of things as well as the performance is doesn't meet our expectation. Thefore, I decide to create this dedicated python package for time series imputation.

## Installation

```
# manual installations from source
git clone https://github.com/zaenalium/imputeTSpy
cd imputeTSpy
python setup.py install
```

```

pip install imputetspy

```

## Getting Started

This packages contains the imputation method code, some graph to visualize the imputation values and the data sample. please take a look of this examples:

```
# get the sample data
data = ts_nh4()
import imputetspy

data = imputetspy.ts_nh4()

# impute the missing values using overall mean and median

data_fill_mean = imputetspy.na_mean(data, option = 'mean')

data_fill_med = imputetspy.na_mean(data, option = 'median')

```

