#!/usr/bin/env python2
import matplotlib

matplotlib.use("Agg")
from pylab import *
import matplotlib.patches as patches

from sddshzb import SDDSad
from sddshzb import Twissplot
import sys

maintitle = subtitle = ""
if len(sys.argv) > 1:
    maintitle = sys.argv[1]
if len(sys.argv) > 2:
    subtitle = sys.argv[2]

# Usage example:

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load("output.twi_full1")
twi1 = twis.columnDataDict
twis.load("output.twi_full2")
twi2 = twis.columnDataDict

# Length of ring
C = np.max(np.array(twi1.s, dtype=np.float64))
print len(twi1), twi1.keys(), C

# Create figure in golden ratio (A paper sizes)
figsizeinch = 14
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

# Plot whole ring
subplot(311)
plot(twi1.s, twi1.betax, "g-")
plot(twi1.s, twi1.betay, "b-")
plot(twi2.s, twi2.betay, "b--")
plot(twi2.s, twi2.betax, "g--")
plot(twi1.s, 10 * np.array(twi1.etax, dtype=np.float64), "r-")
plot(twi2.s, 10 * np.array(twi2.etax, dtype=np.float64), "r--")

# Lattice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi1, 0, C, ec=False, fscale=2)
xlim(0, C)

annotate(
    maintitle, xy=(-0.02, 1.25), fontsize=30, va="center", xycoords="axes fraction"
)  # , annotation_clip=False)
annotate(subtitle, xy=(-0.02, 1.11), fontsize=8, va="center", xycoords="axes fraction")

for i in range(1, 10):
    ha = "center"
    if i == 1:
        ha = "left"
    if i == 9:
        ha = "right"
    x = i * 30 - 30
    annotate("D{0}".format(i), xy=(x, lypos * 0.9), ha=ha, va="top", zorder=105)
    annotate(
        tp.names["D"][(i - 1) % 8],
        xy=(x, lypos * 0.82),
        fontsize=4,
        ha=ha,
        va="top",
        zorder=105,
    )
    x = i * 30 - 15
    annotate("T{0}".format(i), xy=(x, lypos * 0.9), ha="center", va="top", zorder=105)
    annotate(
        tp.names["T"][(i - 1) % 8],
        xy=(x, lypos * 0.82),
        fontsize=4,
        ha="center",
        va="top",
        zorder=105,
    )

gca().set_xticks(linspace(0, 240, 17, endpoint=True))
gca().set_xticks(linspace(7.5, 232.5, 16, endpoint=True), minor=True)

gca().xaxis.grid(which="minor")
gca().yaxis.grid(alpha=0.3, zorder=0)

subplot(312)
x1 = np.array(twi1.betax, dtype=np.float64)
y1 = np.array(twi1.betay, dtype=np.float64)
x2 = np.array(twi2.betax, dtype=np.float64)
y2 = np.array(twi2.betay, dtype=np.float64)

# interpolate in case of different elemtents/slicing
# s1 = np.array(twi1.s,dtype=np.float64)
# s2 = np.array(twi2.s,dtype=np.float64)
# x2 = np.interp(s1,s2,x2)
# y2 = np.interp(s1,s2,y2)

bbx = (x2 - x1) / x1
bby = (y2 - y1) / y1
print bbx.std()
plot(twi1.s, bbx, "g-", label="beta beat std x = {:0.3f}".format(bbx.std()))
plot(twi1.s, bby, "b-", label="beta beat std y = {:0.3f}".format(bby.std()))

gca().set_xticks(linspace(0, 240, 17, endpoint=True))
gca().set_xticks(linspace(7.5, 232.5, 16, endpoint=True), minor=True)
gca().xaxis.grid(which="minor")
gca().yaxis.grid(alpha=0.3, zorder=0)

xlim(0, C)
ylabel("beta beat: $(\\beta_2 - \\beta_1) / \\beta_1$")
xlabel("s / m")
legend()

subplot(313)
d1 = np.array(twi1.etax, dtype=np.float64)
d2 = np.array(twi2.etax, dtype=np.float64)
plot(
    twi1.s,
    (d2 - d1) * 1e3,
    "r-",
    label="std = {:0.3f} mm".format(1e3 * (d2 - d1).std()),
)
gca().set_xticks(linspace(0, 240, 17, endpoint=True))
gca().set_xticks(linspace(7.5, 232.5, 16, endpoint=True), minor=True)
gca().xaxis.grid(which="minor")
gca().yaxis.grid(alpha=0.3, zorder=0)

xlim(0, C)
ylabel("x disp. diff.: $\\eta_2 - \\eta_1$ / mm")
xlabel("s / m")
legend()

# Efficient Plot Adjustment
subplots_adjust(top=0.9, left=0.08, right=0.98, bottom=0.05, hspace=0.3)

savefig("betabeat.pdf")
