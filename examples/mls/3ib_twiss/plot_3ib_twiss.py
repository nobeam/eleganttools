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
# python plotTwiss.py 'BESSY II std. user 15.06.2016' BII_2016-06-10_user_PartialSplit_noID_CurrentUserMode.lte

# Initialize SDDS object and load sdds file with twiss table
twisc = SDDSad(0)
twisc.load("output.twi_full_central")
# Get convenient attribute dictionary
twic = twisc.columnDataDict


twis = SDDSad(0)
twis.load("output.twi_full")
# Get convenient attribute dictionary
twi = twis.columnDataDict


# Print out contained data
# print "\nDescription:",twis.description
# print "\n",len(twis.parameterName),"Paramters:\n", twis.parameterName
# print "\n",len(twis.columnName),"Columns:\n", twis.columnName

# Length of ring
C = np.max(np.array(twi.s, dtype=np.float64))

# Create figure in golden ratio (A paper sizes)
figsizeinch = 14
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

# Plot whole ring
subplot(411)
plot(twic.s, twic.betax, "g-")
plot(twic.s, twic.betay, "b-")
plot(twic.s, 10 * np.array(twic.etax, dtype=np.float64), "r-")
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi, 0, C / 3, ec=True, fscale=3)
xlim(0, C)
ylim(-10)


# Print some headline information
par = twisc.parameterData
# print par
# for key in ('U0','alphac','nux','nuy','dnux/dp','dnuy/dp'):
#     print key, par[key][0]
annotate(
    maintitle, xy=(-0.02, 1.25), fontsize=30, va="center", xycoords="axes fraction"
)  # , annotation_clip=False)
annotate(subtitle, xy=(-0.02, 1.11), fontsize=8, va="center", xycoords="axes fraction")
ianno = 0
annotate(
    "center twiss stats",
    xy=(0.2, 1.45),
    fontsize=21,
    va="center",
    xycoords="axes fraction",
)


def annoTwiss(key, value=None):
    global ianno
    xpos = int(ianno / 4) * 0.18 + 0
    ypos = -int(ianno % 4) * 0.07 + 1.32
    ianno += 1
    # print ianno, xpos, ypos
    if value == None:
        value = par[key][0]
    if value < 1e-5:
        annotate(
            "{0:} = {1:12.6e}".format(key, value),
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )  # , annotation_clip=False)
    else:
        annotate(
            "{0:} = {1:12.10f}".format(key, value),
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )  # , annotation_clip=False)


annoTwiss("length", C)
annoTwiss("nux")
annoTwiss("nuy")
annoTwiss("alphac")
annoTwiss("dnux/dp")
annoTwiss("dnuy/dp")
annoTwiss("U0")
annoTwiss("Sdelta0")
annoTwiss("ex0")

################################################
# Print some headline information
par = twis.parameterData
# print par
# for key in ('U0','alphac','nux','nuy','dnux/dp','dnuy/dp'):
#     print key, par[key][0]
annotate(
    maintitle, xy=(-0.02, 1.25), fontsize=30, va="center", xycoords="axes fraction"
)  # , annotation_clip=False)
annotate(subtitle, xy=(-0.02, 1.11), fontsize=8, va="center", xycoords="axes fraction")
annotate(
    "islands twiss stats",
    xy=(0.7, 1.45),
    fontsize=21,
    va="center",
    xycoords="axes fraction",
)
ianno = 0


def annoTwiss(key, value=None):
    global ianno
    xpos = int(ianno / 4) * 0.18 + 0.55
    ypos = -int(ianno % 4) * 0.07 + 1.32
    ianno += 1
    # print ianno, xpos, ypos
    if value == None:
        value = par[key][0]
    if value < 1e-5:
        annotate(
            "{0:} = {1:12.6e}".format(key, value),
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )  # , annotation_clip=False)
    else:
        annotate(
            "{0:} = {1:12.10f}".format(key, value),
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )  # , annotation_clip=False)


annoTwiss("length", C)
annoTwiss("nux")
annoTwiss("nuy")
annoTwiss("alphac")
annoTwiss("dnux/dp")
annoTwiss("dnuy/dp")
annoTwiss("U0")
annoTwiss("Sdelta0")
annoTwiss("ex0")


gca().set_xticks(linspace(0, 48, 25, endpoint=True))
# gca().set_xticks(linspace(7.5,232.5,16,endpoint=True), minor=True)

gca().xaxis.grid(which="minor")
gca().yaxis.grid(alpha=0.3, zorder=0)


# subplot(411)

# plot(twic.s, twic.betax, 'g-')
# plot(twic.s, twic.betay, 'b-')
# grid()
# # Latteice graphics vertical position and size (axis coordinates!)
# lypos = gca().get_ylim()[1]
# tp = Twissplot(lypos = lypos, lysize = lypos*0.12)
# tp.axislabels(yscale=0.5)
# tp.paintlattice(twic,0,C, ec=True,fscale=7)

annotate("central orbit", xy=(10, 10), fontsize=30)

# twinx()
# ylabel('DISPERSION / m')
# plot(twic.s, np.array(twic.etax,dtype=np.float64) , 'm-')

xlim(0, 48)
ylim(-5)

#############

subplot(412)
annotate("island 1st turn", xy=(10, 10), fontsize=30)

plot(twi.s, twi.betax, "g-")
plot(twi.s, twi.betay, "b-")
plot(twi.s, 10 * np.array(twi.etax, dtype=np.float64), "r-")

grid()
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi, 0, C / 3, ec=True, fscale=3)

# twinx()
# ylabel('DISPERSION / m')
# plot(twi.s, np.array(twi.etax,dtype=np.float64) , 'm-')

xlim(0, 48)
ylim(-10)

subplot(413)
annotate("island 2nd turn", xy=(58, 10), fontsize=30)

plot(twi.s, twi.betax, "g-")
plot(twi.s, twi.betay, "b-")
plot(twi.s, 10 * np.array(twi.etax, dtype=np.float64), "r-")
grid()
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi, C / 3, 2 * C / 3, ec=True, fscale=3)

# twinx()
# ylabel('DISPERSION / m')
# plot(twi.s, np.array(twi.etax,dtype=np.float64) , 'm-')

xlim(48, 96)
ylim(-10)


subplot(414)
annotate("island 3rd turn", xy=(105, 10), fontsize=30)

plot(twi.s, twi.betax, "g-")
plot(twi.s, twi.betay, "b-")
plot(twi.s, 10 * np.array(twi.etax, dtype=np.float64), "r-")
grid()
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi, 2 * C / 3, C, ec=True, fscale=3)

# twinx()
# ylabel('DISPERSION / m')
# plot(twi.s, np.array(twi.etax,dtype=np.float64) , 'm-')

xlim(96, C)
ylim(-10)


# Efficient Plot Adjustment
subplots_adjust(top=0.9, left=0.05, right=0.94, bottom=0.05, hspace=0.3)

savefig("twiss.pdf")


# floor coordinate plots

dataf = SDDSad(0)
dataf.load("output.flr")
data = dataf.columnDataDict

clof = SDDSad(0)
clof.load("output.clo")
clo = clof.columnDataDict


from matplotlib.colors import LinearSegmentedColormap
from matplotlib.collections import LineCollection

# CONVERSION FACTOR
#


def plotFloor(s, a, col=None):
    x = []
    y = []
    # s,a: some value vs. s coordinate
    # x,y: horizontal floor coordintaes
    s = np.array(data.s, dtype=np.float64)
    for (sp, ap) in zip(s, a):
        if sp > 48:
            sp = sp % 48.0
        # ignore 0 position
        if sp == 0 or sp == 48.0:
            continue
        # 1) find x,y for s
        i = argmax(s >= sp)
        # 2) move perpendicular to the ring by value of a
        Z = float(data.Z[i])
        X = float(data.X[i])
        th = float(data.theta[i])
        xc = Z - ap * sin(th)
        yc = X + ap * cos(th)
        x.append(xc)
        y.append(yc)
        # print i,sp,ap, th

    if col == None:
        # --- Custom colormaps ---
        colors = [
            (0.9, 0, 0),
            (0, 0.8, 0),
            (0, 0.8, 0),
            (0, 0, 0.8),
            (0, 0, 0.8),
            (0.9, 0, 0),
        ]
        colors = [
            (0.9, 0, 0),
            (0.9, 0.7, 0.0),
            (0.5, 0.9, 0.0),
            (0.5, 0.9, 0.0),
            (0.9, 0, 0),
        ]

        cm = LinearSegmentedColormap.from_list("alist", colors, N=100)

        # https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/MulticoloredLine.html
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        # plt.get_cmap('copper')
        lc = LineCollection(segments, cmap=cm, norm=plt.Normalize(0, 10))
        t = np.linspace(0, 10, len(x))
        lc.set_array(t)
        # lc.set_linewidth(3)

        plt.gca().add_collection(lc)
    else:
        plot(x, y, "-", color=col)


figure(figsize=(9, 11))

C = np.max(np.array(data.s, dtype=np.float64))
tp = Twissplot(lysize=0.5, zorderoffset=-10)  # ,lypos, lysize = lypos*0.12)
tp.paintlattice(data, 0, C, ec=True, fscale=6, floorCoordinates=True)


plot(data.Z, data.X, "k-", label="central orbit")
plot(0, 0, "r-", label="island orbit (100 x enhanced, colored line)")

legend()

s = np.array(twi.s, dtype=np.float64)
# a = np.array(twi.betax,dtype=np.float64) * 0.2
a = np.array(clo.x, dtype=np.float64) * 1e2
# a = np.ones_like(a)
lc = plotFloor(s, a)

xlim(-9, 9)
ylim(-18, 4)
subplots_adjust(top=0.96, left=0.04, right=0.96, bottom=0.04)
grid()
annotate("MLS 3IB", xy=(0, -5), fontsize=40, ha="center")
annotate("(outdated optics)", xy=(0, -6), fontsize=20, ha="center")


savefig("orbitFloor.pdf")

############

figure(figsize=(9, 12.5))

tp.paintlattice(data, 0, C, ec=True, fscale=6, floorCoordinates=True)

plot(data.Z, data.X, "k-", label="central orbit")

plot(0, 0, "k-", label="central betax $\\times 0.3$ (black line)")

plot(0, 0, "r-", label="island betax $\\times 0.3$ (colored line)")

legend()

s = np.array(twi.s, dtype=np.float64)

a = np.array(twic.betax, dtype=np.float64) * 0.3
plotFloor(s, a, col="black")

a = np.array(twi.betax, dtype=np.float64) * 0.3
plotFloor(s, a)

print a[0:10]
xlim(-9, 9)
ylim(-20, 5)
subplots_adjust(top=0.96, left=0.04, right=0.96, bottom=0.04)
grid()
annotate("MLS 3IB", xy=(0, -5), fontsize=40, ha="center")
annotate("(outdated optics)", xy=(0, -6), fontsize=20, ha="center")


savefig("twissFloor.pdf")

############
figure(figsize=(9, 12.5))

tp.paintlattice(data, 0, C, ec=True, fscale=6, floorCoordinates=True)

plot(data.Z, data.X, "k-", label="central orbit")
plot(0, 0, "k-", label="central etax $\\times 1$ (black line)")
plot(0, 0, "r-", label="island etax $\\times 1$ (colored line)")

legend()

s = np.array(twi.s, dtype=np.float64)

a = np.array(twic.etax, dtype=np.float64) * 1
plotFloor(s, a, col="black")

a = np.array(twi.etax, dtype=np.float64) * 1
plotFloor(s, a)

print a[0:10]
xlim(-9, 9)
ylim(-20, 5)
subplots_adjust(top=0.96, left=0.04, right=0.96, bottom=0.04)
grid()
annotate("MLS 3IB", xy=(0, -5), fontsize=40, ha="center")
annotate("(outdated optics)", xy=(0, -6), fontsize=20, ha="center")


savefig("twissFloorDisp.pdf")
