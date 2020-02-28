# Python tools for elegant

## Installation

1. Install elegant and SDDSPython from [here](https://aps.anl.gov/Accelerator-Operations-Physics/Software).

2. Clone this repository and install it with

``` bash
cd elegantools
pip install -Ue .
```

### Deal with Self Describing Data Sets (SDDS)

Load the twiss data from the `twiss.twi` SDDS file into a Python dictionary:

``` python
from eleganttools import sdds

data = sdds.as_dict("/path/to/twiss.twi")
parameters = data["parameters"]
columns = data["columns"]
s, beta_x, beta_y = (columns[key] for key in ("s", "betax", "betay"))
```

### Run the examples

Make a sym

``` bash
ln -s /path/to/lattice.lte active.lte
```

