### Simple Tracking

1. Add these elements to your lattice:

       RC: RECIRC
       M1: MALIGN, on_pass=1
       W1: WATCH, filename="%s.w1", mode="CENTROID"

2. Run elegant:

       elegant simple_tracking.ele -macro=lattice=/path/to/lattice.lte,energy=1700

3. Plot tracking data:

       python plot_simple_tracking.py

