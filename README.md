# Python tools for elegant

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
from eleganttools import draw_lattice

plt.plot(twiss["s"], twiss["betax"])
draw_lattice(twiss)
```

## Examples

This repository also includes multiple examples in the `examples` folder. Additionally
each example contains a separate `Readme.md` file with further instructions.

### Lattice files

To avoid changing the elegant run files every time you want run your simulations for a
different lattice, most examples are configured to use the `active.lte` file.
The active lattice can be changed by setting a symbolic link to a lattice file:

``` bash
ln -s /path/to/lattice.lte active.lte
```

