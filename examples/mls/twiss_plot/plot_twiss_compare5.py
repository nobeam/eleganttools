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
twis.load(sys.argv[3])
twi3 = twis.columnDataDict
twis.load(sys.argv[4])
twi4 = twis.columnDataDict
twis.load(sys.argv[5])
twi5 = twis.columnDataDict

# Length of ring
C1 = np.max(np.array(twi1.s, dtype=np.float64))
print len(twi1), twi1.keys(), C1
# C2 = np.max(np.array(twi2.s,dtype=np.float64))
# print len(twi2), twi2.keys(), C2

# Create figure in golden ratio (A paper sizes)
figsizeinch = 10
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

plt.subplot(311)
plt.plot(twi1.s, twi1.betax, "-", color="#8A0808", lw=8, label="FromTT")
plt.plot(twi2.s, twi2.betax, "-", color="#DF0101", lw=6, label="FitFamily")
plt.plot(twi3.s, twi3.betax, "-", color="#FE2E2E", lw=4, label="FitMagnet")
plt.plot(twi4.s, twi4.betax, "-", color="#F78181", lw=2, label="FitPS")
plt.plot(twi5.s, twi5.betax, "-", color="k", lw=1, label="FitNoPara")

# plt.ylim(-1.0,14.0)
plt.xlim(0.0, C1)
plt.ylabel("betaX $\\beta_x / \mathrm{m}$", ha="center", va="bottom", size=12)
plt.tick_params(
    axis="x",  # changes apply to the x-axis
    which="both",  # both major and minor ticks are affected
    bottom="on",  # ticks along the bottom edge are off
    top="on",  # ticks along the top edge are off
    labelbottom="on",
)  # labels along the bottom edge are off
plt.grid()
plt.legend(fontsize=8)


plt.subplot(312)
plt.plot(twi1.s, twi1.betay, "-", color="#08298A", lw=8, label="FromTT")
plt.plot(twi2.s, twi2.betay, "-", color="#013ADF", lw=6, label="FitFamily")
plt.plot(twi3.s, twi3.betay, "-", color="#2E64FE", lw=4, label="FitMagnet")
plt.plot(twi4.s, twi4.betay, "-", color="#819FF7", lw=2, label="FitPS")
plt.plot(twi5.s, twi5.betay, "-", color="k", lw=1, label="FitNoPara")
plt.xlim(0.0, C1)
plt.ylabel("betaY $\\beta_y / \mathrm{m}$", ha="center", va="bottom", size=12)
plt.grid()
plt.legend(fontsize=8)


plt.subplot(313)
plt.plot(twi1.s, twi1.etax, "-", color="#21610B", lw=8, label="FromTT")
plt.plot(twi2.s, twi2.etax, "-", color="#31B404", lw=6, label="FitFamily")
plt.plot(twi3.s, twi3.etax, "-", color="#40FF00", lw=4, label="FitMagnet")
plt.plot(twi4.s, twi4.etax, "-", color="#9FF781", lw=2, label="FitPS")
plt.plot(twi5.s, twi5.etax, "-", color="k", lw=1, label="FitNoPara")
xlim(0, C1)
ylim(-0.4, 1.8)
plt.ylabel("dispersion  $\\eta_x / \mathrm{m}$", ha="center", va="bottom", size=12)
plt.xlabel("position $s / \mathrm{m}$", size=12)
plt.legend(fontsize=8)
plt.grid()


# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.15)
# tp.axislabels(yscale=0.8)
tp.paintlattice(twi1, 0, C1, ec=True, fscale=0.0)
# plt.subplots_adjust(wspace=0, hspace=0)
plt.tight_layout()
# plt.tight_layout(pad=0.1, w_pad=1.0, h_pad=1.0)


# outputfile = 'twiss_'+
# savefig(sys.argv[1]+'__and__'+sys.argv[2]+'ssCompare.pdf')
figname = sys.argv[1]
figname = figname.replace("FromTT.twi", "CompareAllLocoFits.pdf")
savefig(figname)
