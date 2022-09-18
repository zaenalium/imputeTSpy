import numpy as np
import impyute
# pylint: disable=invalid-name, too-many-arguments, too-many-locals, too-many-branches, broad-except, len-as-condition

def moving_window(data, nindex=None, wsize=5, errors="coerce", func=np.mean,
        inplace=False):
    """ Interpolate the missing values based on nearby values.

    For example, with an array like this:

        array([[-1.24940, -1.38673, -0.03214945,  0.08255145, -0.007415],
               [ 2.14662,  0.32758 , -0.82601414,  1.78124027,  0.873998],
               [-0.41400, -0.977629,         nan, -1.39255344,  1.680435],
               [ 0.40975,  1.067599,  0.29152388, -1.70160145, -0.565226],
               [-0.54592, -1.126187,  2.04004377,  0.16664863, -0.010677]])

    Using a `k` or window size of 3. The one missing value would be set
    to -1.18509122. The window operates on the horizontal axis.

    Usage
    -----

    The parameters default the function to a moving mean. You may want to change
    the default window size:

        moving_window(data, wsize=10)

    To only look at past data (null value is at the rightmost index in the window):

        moving_window(data, nindex=-1)

    To use a custom function:

        moving_window(data, func=np.median)

    You can also do something like take 1.5x the max of previous values in the window:

        moving_window(data, func=lambda arr: max(arr) * 1.50, nindex=-1)

    Parameters
    ----------
    data: numpy.ndarray
        2D matrix to impute.
    nindex: int
        Null index. Index of the null value inside the moving average window.
        Use cases: Say you wanted to make value skewed toward the left or right
        side. 0 would only take the average of values from the right and -1
        would only take the average of values from the left
    wsize: int
        Window size. Size of the moving average window/area of values being used
        for each local imputation. This number includes the missing value.
    errors: {"raise", "coerce", "ignore"}
        Errors will occur with the indexing of the windows - for example if there
        is a nan at data[x][0] and `nindex` is set to -1 or there is a nan at
        data[x][-1] and `nindex` is set to 0. `"raise"` will raise an error,
        `"coerce"` will try again using an nindex set to the middle and `"ignore"`
        will just leave it as a nan.
    inplace: {True, False}
        Whether to return a copy or run on the passed-in array

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    data = moving_window(data, nindex=None, wsize=5, errors="coerce", func=np.mean,
        inplace=False)

    return data
