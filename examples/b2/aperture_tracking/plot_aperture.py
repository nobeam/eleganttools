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
# python plotTwiss.py 'BESSY II std. user 15.06.2016' BII_2016-06-10_user_PartialSplit_noID_CurrentUserMode.lte

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load("output.twi")
# Get convenient attribute dictionary
twi = twis.columnDataDict

# Print out contained data
# print "\nDescription:",twis.description
# print "\n",len(twis.parameterName),"Paramters:\n", twis.parameterName
# print "\n",len(twis.columnName),"Columns:\n", twis.columnName

# Length of ring
C = np.max(np.array(twi.s, dtype=np.float64))
print(len(twi), twi.keys(), C)

# Create figure in golden ratio (A paper sizes)
figsizeinch = 14
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

# Plot whole ring
subplot(311)
plot(twi.s, twi.xAperture, "g-")
plot(twi.s, twi.yAperture, "b-")
ylabel("x,y Effective horizontal aperture / m")
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
# tp.axislabels(yscale=0.5)
tp.paintlattice(twi, 0, C, ec=False, fscale=2)
xlim(0, C)


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


# open file directly
aps = SDDSad(0)
aps.load("aperture.sdds")
ap = aps.columnDataDict

subplot(312)

plot(ap.s, ap.xHalfAperture, "g")
plot(ap.s, ap.yHalfAperture, "b")
ylabel("x,yHalfAperture / m")
gca().set_xticks(linspace(0, 240, 17, endpoint=True))
gca().set_xticks(linspace(7.5, 232.5, 16, endpoint=True), minor=True)
gca().xaxis.grid(which="minor")
gca().yaxis.grid(alpha=0.3, zorder=0)

xlim(0, C)

subplot(313)

plot(ap.s, ap.xCenter, "g")
plot(ap.s, ap.yCenter, "b")
ylabel("x,yCenter / m")
gca().set_xticks(linspace(0, 240, 17, endpoint=True))
gca().set_xticks(linspace(7.5, 232.5, 16, endpoint=True), minor=True)
gca().xaxis.grid(which="minor")
gca().yaxis.grid(alpha=0.3, zorder=0)


xlim(0, C)


# Efficient Plot Adjustment
# subplots_adjust(top=0.9, left=0.05, right=0.98, bottom=0.05, hspace=0.3)
tight_layout()
savefig("aperture.pdf")
