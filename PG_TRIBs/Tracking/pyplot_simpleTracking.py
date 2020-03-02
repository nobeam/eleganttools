#!/usr/bin/env python2
import matplotlib
matplotlib.use('Agg')
from pylab import *
import matplotlib.patches as patches
import matplotlib as mpl

from sddshzb import SDDSad
import sys

# Initialize SDDS object and load sdds file from a centroid watchpoint
W = SDDSad(0)
W.load(sys.argv[1])
# Get convenient attribute dictionary
data = W.columnDataDict

# Print out contained data
print "\nDescription:",W.description
print "\n",len(W.parameterName),"Paramters:\n", W.parameterName
print "\n",len(W.columnName),"Columns:\n", W.columnName

fig = figure(figsize=(12,9))
cmap = mpl.cm.hsv 

def eleplot(x,y, sel=None,label=None):
    global data
    print x,y
    matplotlib.rcParams.update({'font.size': 8})
    if sel is not None:
        plot(data[x][sel], data[y][sel],'b,',label=label)
    else:
        plot(data[x], data[y],'b,',label=label)
    xlabel(x)
    ylabel(y)

subplot(331)
eleplot('Pass','dCt')
subplot(334)
eleplot('Pass','Cdelta')
subplot(337)
eleplot('dCt','Cdelta')

subplot(332)
eleplot('Pass','Cx')
subplot(335)
eleplot('Pass','Cxp')
subplot(338)
eleplot('Cx','Cxp')

subplot(333)
eleplot('Pass','Cy')
subplot(336)
eleplot('Pass','Cyp')
subplot(339)
eleplot('Cy','Cyp')


tight_layout()
savefig(sys.argv[1] + '_Tracking.png')
savefig(sys.argv[1] + '_Tracking.pdf')
