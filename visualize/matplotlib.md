```Python
import matplotlib.pyplot as plt
import numpy as np
np.__version__

students_gpas.mean(axis=1)
plt.boxplot(students_gpas)
plt.plot()
# this will plot along the undesired array shape
# a transpose is necessary

plt.boxplot(students_gpas.T)
plt.plot()

# Pass in a 1D array, of all non-negative minutes.
plt.hist(study_minutes[study_minutes > 0])

```
