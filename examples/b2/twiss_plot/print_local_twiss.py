#!/usr/bin/env python2
import numpy as np
from sddshzb import SDDSad

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load("output.twi_full")
# Get convenient attribute dictionary
twi = twis.columnDataDict

# Prints the local twiss parameters at the next availible data point at or above the desired position s
# Note: High sampling density of elegant elements recommended
def printLocalTwiss(s):
    ipos = np.argmax(np.array(twi.s, dtype=np.float64) >= s)

    for i in range(len(twis.columnName)):
        key = twis.columnName[i]
        desc = twis.columnDefinition[i]
        unit = desc[1]
        text = desc[2]
        print "{0:<20} {1:>18} {2:<10} {3:20}".format(key, twi[key][ipos], unit, text)


# BII streak camera beam line BM2D2R at 4 deg: s = 35.0590
# Bending: 0.855 m / 11.25 degree : 0.076 m / degree
b = 0.076
# BII BM2D2R (D31) start: s =  34.75500 end: s = 35.610000 (arc length 0.855 m)
# BII BM2D5R (D91) start: s = 124.75500


# update 23.08.2016
# Abgangswinkel in 4 deg Dipolen Zusammenfassung:
#
#    Pinhole H03- DIP31 3.700 deg
#    Pinhole H09- DIP91 3.658 deg
#    Schnelle optische Strahldiagnose (alter Streakkameraport) - DIP31 4.100 deg
#    APD / Fillpattern DIP31 4.300 deg

for s in (34.75500 + b * 3.700, 34.75500 + b * 4.100, 124.75500 + b * 3.658):
    printLocalTwiss(s)
    print
    print
