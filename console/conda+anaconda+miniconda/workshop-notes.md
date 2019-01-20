# Anaconda

Anaconda is a large and
powerful platform that's heavily used by science and data-oriented Pythonistas.
And it provides a ton of the tools you'll use in those areas like Pandas,
Jupyter Notebook, and more.

It makes it faster and easier to set up and install the tools and
libraries that you need to do your science.

Another benefit of using a platform like Anaconda comes out when you're working
with a team or need to share your results with others in the community.
Using a standardized platform lets you all easily replicate an environment and
set up quickly and reliably.
That means less time spent setting things up and tweaking libraries and
more time for your science.

Beyond that though, Anaconda also brings with it easier manipulation and
use of data sources, a community of experts, and a lot more.

# Conda

Conda is a great tool to use for installing packages

Conda is Anaconda's pip-like tool.
  Conda does a bit more than pip;
  Conda does everything that the navigator can do.

## Managing Conda environments

`[conda env list](https://conda.io/docs/user-guide/tasks/manage-environments.html#viewing-a-list-of-your-environments)
`
## practice: creating a new project

* project name **humuhumu**
* install `numpy` into project environment

```
conda create --name humuhumu numpy
```

### refresh: pip

  (note: pip is a package management system)

```
pip install numpy --upgrade
pip install pandas --upgrade
```

```Py
import numpy
numpy.version.version
print(numpy.__path__)
```

# Miniconda
