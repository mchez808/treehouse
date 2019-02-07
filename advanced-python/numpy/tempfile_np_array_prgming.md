# note: add this to [Array Programming](https://github.com/mchez808/treehouse/blob/master/intermediate-python/numpy/Unit%203%20-%20Array%20Programming.ipynb) file when it works again

## Universal Functions
* [ufuncs](https://docs.scipy.org/doc/numpy/reference/ufuncs.html) are commonly needed vectorized functions
  * Vectorized functions allow you to operate element by element without using a loop
* The standard math and comparison operations have all been overloaded so that they can make use of vectorization
* Values can be [broadcasted](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html), or stretched to be applied to the ufuncs.

### Universal Functions: Reduce and Accumulate
* Universal Functions expose a function to `reduce` an array to a single value.
`np.add.reduce(study_minutes[0])`
`np.add.accumulate(study_minutes[0])`
* There is also a function named `accumulate` which will show the reduction and its accumulation as it happens.

## Common Routines
* Common [mathematical](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.math.html) [routines](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.html) are exposed so the formula can be abstracted away.
    * [`mean`](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html#numpy.mean) is a [statistics](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.statistics.html) routine used to calculate the average.
* Reduction functions take a dimension and collapse it into a single value.
    * These functions define an axis parameter, and you should remember that the function works across the dimension.

## Array Reductions in NumPy

```Python
quarterly_revenue_by_year = np.array([
    [22.72, 29.13, 25.36, 35.75],
    [29.13, 30.4, 32.71, 43.74],
    [35.71, 37.96, 43.74, 60.5]
])

Which of the following statements would allow for the quarterly average across the years?
quarterly_revenue_by_year.mean(axis=0)

Which of the following statements would allow for the yearly average of all quarters?
quarterly_revenue_by_year.mean(axis=1)

Which of the following statements would allow for the average of all of the quarters and years?
quarterly_revenue_by_year.mean()
```

