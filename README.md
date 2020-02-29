# Python tools for elegant

## Installation

1. Install elegant from [here](https://aps.anl.gov/Accelerator-Operations-Physics/Software).

2. Installing this package:

    * If you intend to make changes to this repository, clone and install it with:

        ``` bash
        git clone git@github.com:nobeam/eleganttools.git
        pip install -Ue ./eleganttools
        ```

    * If you just want to use this package:

        ``` bash
        pip install -U git+https://github.com/nobeam/eleganttools.git@master
        ```

## Usage

### Dealing with Self Describing Data Sets (SDDS)

Load the twiss data from the `twiss.twi` SDDS file into a Python dictionary:

``` python
from eleganttools import SDDS

twiss = SDDS("/path/to/twiss.twi").as_dict()
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
df = SDDS("/path/to/twiss.twi").as_dataframe()
df.betax
```

### Run the examples

Make a sym

``` bash
ln -s /path/to/lattice.lte active.lte
```

