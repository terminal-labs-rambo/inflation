[![Gitter](https://badges.gitter.im/terminal-labs/inflation.svg)](https://gitter.im/terminal-labs/inflation?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This project is very experimental

# Hardware Recommendations

This version assumes that the host os is RHEL or Ubuntu.

You need a reasonably fast cpu with 2 or more cores and VT-x (I used a Intel i7-3612QM 2.1GHz, 4 core chip)

8gb ram (or more)

16gb free drive space (or more)

# Installation

install anaconda
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -b

export PATH="~/miniconda3/bin:$PATH"

rm Miniconda3-latest-Linux-x86_64.sh
```

setup conda env
```
conda create -n inflation python=3.7

source activate inflation
```

activate inflation tools
```
. activate.sh
```
