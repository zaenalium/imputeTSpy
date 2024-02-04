# imputeTSpy: Time series Imputation in Python

## What is it?

This package is a package for all imputation method in time series method. Most of this kind of package are available in R, however, when we use the package for interfacing python to R is somehow complicated, and need to install a lot of things as well as the performance is doesn't meet our expectation. Thefore, I decide to create this dedicated python package for time series imputation. Please visit this (link)[https://imputetspy.readthedocs.io/] for the detail of the package documentations. 


## Instalations

```
# manual installations from source
git clone https://github.com/zaenalium/imputeTSpy
cd imputeTSpy
python setup.py install
```

```

pip install imputetspy

```

## How to use this packages

### Moving Average imputation 

Fill the missing value by mean by *k* of both sides of the missing values. For example, if there is missing values in index 10, and we set k = 2, then we will calculate the mean from index 8, 9, 11, 12. This function also support weighted moving average function i.e. linear and exponential. Moreover, we can change the mean function to median or mode or any custom function.

```
import imputetspy

## load_sample dataset
df = imputetspy.datasets.ts_airgap()

## Moving average imputation
df['number_of_passengers'] = imputetspy.na_ma(df['number_of_passengers'], k = 2)

## Exponential moving average imputation
df['number_of_passengers'] = imputetspy.na_ma(df['number_of_passengers'], k = 2, weighting = 'exponential')


## moving median imputation
df['number_of_passengers'] = imputetspy.na_ma(df['number_of_passengers'], k = 2, func = 'median')


## moving custom functions imputation

def min_2(x):
    return min(x) * 2

df['number_of_passengers'] = imputetspy.na_ma(df['number_of_passengers'], k = 2, func = min_2)


```

### Interplotate imputation 



```


```

### Interplotate random 



```


```

### Overall Mean/median/mode imputation

In order to perform a mean imputation please take a look to this example.

```
import imputetspy

## load_sample dataset
df = imputetspy.datasets.ts_airgap()

## perform imputation by overall mean
df['number_of_passengers'] = imputetspy.na_mean(df['number_of_passengers'])

## perform imputation by overall mode
df['number_of_passengers'] = imputetspy.na_mean(df['number_of_passengers'], option = 'mode')

## perform imputation by overall median
df['number_of_passengers'] = imputetspy.na_mean(df['number_of_passengers'], option = 'median')


## perform imputation by overall harmonic mean
df['number_of_passengers'] = imputetspy.na_mean(df['number_of_passengers'], option = 'harmonic')

## perform imputation by overall geometric mean
df['number_of_passengers'] = imputetspy.na_mean(df['number_of_passengers'], option = 'geometric')


```


## Notes

Feel free if you have any comments or question, you can directly send me an email.


Warm regards,

Ahmad Zaenal