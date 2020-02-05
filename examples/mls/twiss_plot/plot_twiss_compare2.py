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

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load(sys.argv[1])
twi1 = twis.columnDataDict
twis.load(sys.argv[2])
twi2 = twis.columnDataDict

# Length of ring
C1 = np.max(np.array(twi1.s, dtype=np.float64))
print len(twi1), twi1.keys(), C1
# C2 = np.max(np.array(twi2.s,dtype=np.float64))
# print len(twi2), twi2.keys(), C2

# Create figure in golden ratio (A paper sizes)
figsizeinch = 10
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

plt.subplot(211)
plt.plot(twi1.s, twi1.betax, "r-", lw=4, label="$\\beta_x$ stduser")
plt.plot(twi2.s, twi2.betax, "#FA8258", lw=2, label="$\\beta_x$ 3IB")
plt.plot(twi1.s, twi1.betay, "b-", lw=4, label="$\\beta_y$ stduser")
plt.plot(twi2.s, twi2.betay, "#58D3F7", lw=2, label="$\\beta_y$ 3IB")
plt.ylim(-1.0, 18.2)
plt.xlim(0.0, C1)
plt.ylabel("beta functions  $\\beta / \mathrm{m}$", ha="center", va="bottom", size=15)
plt.tick_params(
    axis="x",  # changes apply to the x-axis
    which="both",  # both major and minor ticks are affected
    bottom="on",  # ticks along the bottom edge are off
    top="on",  # ticks along the top edge are off
    labelbottom="off",
)  # labels along the bottom edge are off
plt.grid()
plt.legend(fontsize=10)


plt.subplot(212)
plt.plot(twi1.s, twi1.etax, "g-", lw=4, label="$\\eta_x$ stduser")
plt.plot(twi2.s, twi2.etax, "#2EFE64", lw=2, label="$\\eta_x$ 3IB")
xlim(0, C1)
ylim(-0.4, 2.0)
plt.ylabel("dispersion  $\\eta_x / \mathrm{m}$", ha="center", va="bottom", size=15)
plt.xlabel("position $s / \mathrm{m}$", size=15)
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.08)
# tp.axislabels(yscale=0.8)
tp.paintlattice(twi1, 0, C1, ec=True, fscale=2)
# plt.subplots_adjust(wspace=0, hspace=0)
plt.grid()
plt.tight_layout()
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# outputfile = 'twiss_'+
savefig(sys.argv[1] + "__and__" + sys.argv[2] + "ssCompare.pdf")
