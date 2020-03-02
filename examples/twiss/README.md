### Twiss plot

1. Copy or create symlink to your lattice file, e.g.:

       cp /path/to/lattice.lte active.lte
       ln -s /path/to/lattice.lte active.lte

2. Run elegant:

       elegant twiss.ele -macro=lattice=/path/to/lattice.lte

3. Plot the twiss data:

       python plot_twiss.py twiss.twi --title "BESSY II Standard User Mode 2020/02/29"

