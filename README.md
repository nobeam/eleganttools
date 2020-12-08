# Python tools for elegant

This repository contains Python tools for post processing of elegant simulation data. There are multiple examples in the `examples` folder, whereby each example includes a separate `Readme.md` file with further instructions.

## Installation

1. Install [elegant](https://aps.anl.gov/Accelerator-Operations-Physics/Software)

2. Install this package:

    - If you intend to make changes to this repository, clone and install it with:

          git clone git@github.com:nobeam/eleganttools.git
          pip install -Ue ./eleganttools

    - If you just want to use this package:

          pip install -U git+https://github.com/nobeam/eleganttools.git

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

### Matplotlib convenience functions

This package comes with some matplotlib convenience functions.

Draw the magnets of the lattice on top of a matplotlib axis:

``` python
from eleganttools import draw_elements

fig, ax = plt.subplots()
ax.plot(twiss["s"], twiss["betax"])
draw_elements(ax, twiss)
```
