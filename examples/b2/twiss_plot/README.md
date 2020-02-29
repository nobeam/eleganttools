1. Create symlink to your lattice, e.g.:

   ln -s /path/to/lattice.lte active.lte

2. Run elegant:

   elegant twiss.ele

3. Plot the twiss data:

   python plot_twiss.py twiss.twi --title "BESSY II Standard User Mode 2020/02/29"

