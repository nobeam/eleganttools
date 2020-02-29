# Python tools for elegant

## Installation

1. Install elegant and SDDSPython from [here](https://aps.anl.gov/Accelerator-Operations-Physics/Software).

2. Clone this repository and install it with

``` bash
cd elegantools
pip install -Ue .
```

### Dealing with Self Describing Data Sets (SDDS)

Load the twiss data from the `twiss.twi` SDDS file into a Python dictionary:

``` python
from eleganttools import sdds

twiss = sdds.as_dict("/path/to/twiss.twi")
```

You can now access items of the twiss data via:

``` python
twiss["betax"]
```

Or, assign multiple items to individual Python variables:

``` python
s, beta_x, beta_y = (twiss[key] for key in ("s", "betax", "betay"))
```

It is also possible to load the data into a pandas dataframe and use the slightly more
convenient dot notation:

``` python
df = sdds.as_dataframe("/path/to/twiss.twi")
df.betax
```

### Run the examples

Make a sym

``` bash
ln -s /path/to/lattice.lte active.lte
```

