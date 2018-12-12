This file contains bash notes used for other lessons, such as installing program managers

Find out your OS architecture (32-bit or 64-bit)

`uname -m`

### Q&A about $PATH

Q: Why do we make sure ~/bin is in your $PATH?

A: To have the particular executable available everywhere on the command line.

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
