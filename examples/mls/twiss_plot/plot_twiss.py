#!/usr/bin/env python2
import matplotlib

matplotlib.use("Agg")
from pylab import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt

from sddshzb import SDDSad
from sddshzb import Twissplot
import sys

print "Number of arguments:", len(sys.argv), "arguments."
print "Argument List:", str(sys.argv)
print "Input File:", sys.argv[1]
# ~ import sys
# ~ maintitle = subtitle  = ''
# ~ if len(sys.argv) > 1:
# ~ maintitle =  sys.argv[1]
# ~ if len(sys.argv) > 2:
# ~ subtitle =  sys.argv[2]

# Usage example:
# python plotTwiss.py 'BESSY II std. user 15.06.2016' BII_2016-06-10_user_PartialSplit_noID_CurrentUserMode.lte

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load(sys.argv[1])
# inputfile = sys.argv[1]
# print inputfile
# twis.load(inputfile)
# twis.load('output.twi_full')
# Get convenient attribute dictionary
twi = twis.columnDataDict

# Print out contained data
# print "\nDescription:",twis.description
# print "\n",len(twis.parameterName),"Paramters:\n", twis.parameterName
# print "\n",len(twis.columnName),"Columns:\n", twis.columnName

# Length of ring
C = np.max(np.array(twi.s, dtype=np.float64))
print len(twi), twi.keys(), C
# print len(twi),
# print twi.keys()
# print C


# Create figure in golden ratio (A paper sizes)
figsizeinch = 10
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))


plt.subplot(211)
plt.plot(twi.s, twi.betax, "r-", lw=2, label="$\\beta_x$")
plt.plot(twi.s, twi.betay, "b-", lw=2, label="$\\beta_y$")
plt.ylim(-1.0, 25.2)
plt.xlim(0.0, C)
plt.ylabel("beta functions  $\\beta / \mathrm{m}$", ha="center", va="bottom", size=15)
plt.tick_params(
    axis="x",  # changes apply to the x-axis
    which="both",  # both major and minor ticks are affected
    bottom="on",  # ticks along the bottom edge are off
    top="on",  # ticks along the top edge are off
    labelbottom="off",
)  # labels along the bottom edge are off
plt.grid()
plt.legend()


plt.subplot(212)
plt.plot(twi.s, twi.etax, "g-", lw=2)
xlim(0, C)
ylim(-0.4, 2.0)
plt.ylabel("dispersion  $\\eta_x / \mathrm{m}$", ha="center", va="bottom", size=15)
plt.xlabel("position $s / \mathrm{m}$", size=15)
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.08)
# tp.axislabels(yscale=0.8)
tp.paintlattice(twi, 0, C, ec=True, fscale=2)
# plt.subplots_adjust(wspace=0, hspace=0)
plt.grid()
plt.tight_layout()
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# outputfile = 'twiss_'+
savefig(sys.argv[1] + "ssPlot.pdf")
savefig(sys.argv[1] + "ssPlot.png")
