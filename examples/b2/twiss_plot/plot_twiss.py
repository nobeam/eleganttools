import numpy as np
import matplotlib.pyplot as plt

from eleganttools.sddshzb import SDDSad, Twissplot
import sys

maintitle = subtitle = ""
if len(sys.argv) > 1:
    maintitle = sys.argv[1]
if len(sys.argv) > 2:
    subtitle = sys.argv[2]

# Usage example:
# python plotTwiss.py 'BESSY II std. user 15.06.2016' BII_2016-06-10_user_PartialSplit_noID_CurrentUserMode.lte

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load("output.twi_full")

# Get convenient attribute dictionary
twi = twis.columnDataDict

# Length of ring
C = np.max(np.array(twi["s"], dtype=np.float64))
print(len(twi), twi.keys(), C)

# Create figure in golden ratio (A paper sizes)
figsizeinch = 14
fig = plt.figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

# Plot whole ring
plt.subplot(311)
plt.plot(twi["s"], twi["betax"], "g-")
plt.plot(twi["s"], twi["betay"], "b-")
plt.plot(twi["s"], 10 * np.array(twi["etax"], dtype=np.float64), "r-")

# Latteice graphics vertical position and size (axis coordinates!)
lypos = plt.gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi, 0, C, ec=False, fscale=2)
plt.xlim(0, C)

# Print some headline information
par = twis.parameterData
plt.annotate(
    maintitle, xy=(-0.02, 1.25), fontsize=30, va="center", xycoords="axes fraction"
)
plt.annotate(
    subtitle, xy=(-0.02, 1.11), fontsize=8, va="center", xycoords="axes fraction"
)
ianno = 0


def annotate_twiss(key, value=None):
    global ianno
    xpos = int(ianno / 4) * 0.18 + 0.5
    ypos = -int(ianno % 4) * 0.07 + 1.32
    ianno += 1
    # print ianno, xpos, ypos
    if value == None:
        value = par[key][0]
    if value < 1e-5:
        plt.annotate(
            "{0:} = {1:12.6e}".format(key, value),
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )  # , annotation_clip=False)
    else:
        plt.annotate(
            "{0:} = {1:12.10f}".format(key, value),
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )  # , annotation_clip=False)


annotate_twiss("length", C)
annotate_twiss("nux")
annotate_twiss("nuy")
annotate_twiss("alphac")
annotate_twiss("dnux/dp")
annotate_twiss("dnuy/dp")
annotate_twiss("U0")
annotate_twiss("Sdelta0")
annotate_twiss("ex0")
annotate_twiss("E_GeV", par["pCentral"][0] / 3913.90152459 * 2)

for i in range(1, 10):
    ha = "center"
    if i == 1:
        ha = "left"
    if i == 9:
        ha = "right"
    x = i * 30 - 30
    plt.annotate("D{0}".format(i), xy=(x, lypos * 0.9), ha=ha, va="top", zorder=105)
    plt.annotate(
        tp.names["D"][(i - 1) % 8],
        xy=(x, lypos * 0.82),
        fontsize=4,
        ha=ha,
        va="top",
        zorder=105,
    )
    x = i * 30 - 15
    plt.annotate(
        "T{0}".format(i), xy=(x, lypos * 0.9), ha="center", va="top", zorder=105
    )
    plt.annotate(
        tp.names["T"][(i - 1) % 8],
        xy=(x, lypos * 0.82),
        fontsize=4,
        ha="center",
        va="top",
        zorder=105,
    )

plt.gca().set_xticks(np.linspace(0, 240, 17, endpoint=True))
plt.gca().set_xticks(np.linspace(7.5, 232.5, 16, endpoint=True), minor=True)

plt.gca().xaxis.grid(which="minor")
plt.gca().yaxis.grid(alpha=0.3, zorder=0)

# Plot 4 interesting sections
plt.subplot(323)
tp.plotsection(twi, "D", 1)

plt.subplot(324)
tp.plotsection(twi, "T", 6)

plt.subplot(325)
tp.plotsection(twi, "D", 6)

plt.subplot(326)
tp.plotsection(twi, "T", 8)

# Efficient Plot Adjustment
plt.subplots_adjust(top=0.9, left=0.05, right=0.98, bottom=0.05, hspace=0.3)
plt.savefig("twiss.pdf")
