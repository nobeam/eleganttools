#!/bin/bash

ln -sf MLS_3IB_3foldring_outdated.lte active.lte

# Some tracking to see where islands are
elegant tracking.ele
python plotTracking.py 

# Calculate twiss functions+orbits on central and island orbit
# Note: approximate position of island needs to be known for misalignment
elegant twissOutput3IB.ele
# floor coordinates
elegant floorCoordinates.ele

# plot something
python plot3IBTwiss.py

