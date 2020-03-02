#!/usr/bin/env python2
import matplotlib
matplotlib.use('Agg')
from pylab import *
import matplotlib.patches as patches
import matplotlib.ticker as ticker

from sddshzb import SDDSad
import sys

# Initialize SDDS object and load sdds file from a centroid watchpoint
W = SDDSad(0)
W.load(sys.argv[1])
# Get convenient attribute dictionary
data = W.columnDataDict

# Print out contained data
print "\nDescription:",W.description
print "\n",len(W.parameterName),"Paramters:", W.parameterName
# print "\n",len(W.parameterDefinition),"ParametersDefinition:\n", W.parameterDefinition
# print "\n",len(W.parameterData),"ParametersData:\n", W.parameterData

print "\n",len(W.columnName),"Columns:", W.columnName
# print "\n",len(W.columnDefinition),"columnDefinition:\n", W.columnDefinition
# print "\n",len(W.columnData),"columnData:\n", W.columnData


fig = figure(figsize=(12,8))
plt.plot(data.Cx, data.Cxp, 'k.', lw=1, label="bla")
plt.ticklabel_format(axis='both', style='sci', scilimits=(-2,2), size=25)
plt.rc('font', size=25)
# plt.ylabel("$x' /mathrm{mrad}$", ha='center', va='bottom', size=25)
plt.ylabel("angle   $x' / \mathrm{rad}$", size=35)
plt.yticks(size=25)
plt.xlabel("offset   $x / \mathrm{m}$", size=35)
plt.xticks(size=10)
# For B2Standard
plt.xlim(-0.031, 0.018)
plt.ylim(-0.0014, 0.0014)
# For B2Tribs
# plt.xlim(-0.031, 0.018)
# plt.ylim(-0.0014, 0.0014)

ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2e-2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1e-2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2e-3))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1e-3))

gca().xaxis.grid(which='minor')
gca().yaxis.grid(which='minor')


# def eleplot(x,y, sel=None,label=None):
    # global data
    # print x,y
    # matplotlib.rcParams.update({'font.size': 8})
    # if sel is not None:
        # plot(data[x][sel], data[y][sel],'b,',label=label)
    # else:
        # plot(data[x], data[y],'b,',label=label)
    # xlabel(x)
    # ylabel(y)

# subplot(331)
# eleplot('Pass','dCt')
# subplot(334)
# eleplot('Pass','Cdelta')
# subplot(337)
# eleplot('dCt','Cdelta')

# subplot(332)
# eleplot('Pass','Cx')
# subplot(335)
# eleplot('Pass','Cxp')
# subplot(338)
# eleplot('Cx','Cxp')

# subplot(333)
# eleplot('Pass','Cy')
# subplot(336)
# eleplot('Pass','Cyp')
# subplot(339)
# eleplot('Cy','Cyp')


tight_layout()
savefig(sys.argv[1] + '_Tracking_XX_new.pdf')
savefig(sys.argv[1] + '_Tracking_XX_new.png')
#savefig(sys.argv[1] + '_Tracking_XX.jpg')

