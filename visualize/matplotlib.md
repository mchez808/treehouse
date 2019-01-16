```Python
import matplotlib.pyplot as plt
import numpy as np
np.__version__
```

Matplotlib vs Bokeh & Seaborn
----
libraries such as Bokeh or Seaborn are better suited to generate interactive, web-based charts (than matplotlib).

* https://matplotlib.org/gallery/index.html

* [bokeh: interactive visualization library for modern web browsers ](https://bokeh.pydata.org/en/latest/)

* [seaborn: statistical data visualization](seaborn.pydata.org)

Matplotlib Resources
----
* [Matplotlib color options](https://matplotlib.org/api/colors_api.html)

* [Matplotlib linestyles](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html?highlight=line%20style%20reference)

Chart Toppers: Plotting
----
* [groupby in Python itertools](https://docs.python.org/3/library/itertools.html#itertools.groupby)
* [pyplot.title() method](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.title.html?highlight=matplotlib%20pyplot%20title#matplotlib.pyplot.title)
* [Matplotlib Legends](https://matplotlib.org/users/legend_guide.html)
* [Matplotlib Markers](https://matplotlib.org/api/markers_api.html)

```Py
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
