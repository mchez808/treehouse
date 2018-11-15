This file contains bash notes used for other lessons, such as installing program managers

# conda setup

setup conda to setup NumPy

(src: NumPy Treehouse video -- Getting Setup)

`conda --version`

### create an environment named 100days

`conda create -n 100days numpy jupyter`

(to update conda)

`conda update -n base conda`

to use it:

`conda activate 100days`

one-time configuration:

`echo ". /home/mark/anaconda/etc/profile.d/conda.sh" >> ~/.bashrc`

# open Jupyter server

`jupyter notebook`
