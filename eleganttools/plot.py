from sddshzb import SDDSad
import numpy as np
from matplotlib.pyplot import xlabel, ylabel, gca, xlim, ylim, annotate, plot

# from pylab import *
# from matplotlib.colors import LogNorm

import matplotlib.patches as patches
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker


class Twissplot:
    Dnames = [
        "Injection",
        "U125",
        "UE56",
        "U49",
        "UE52",
        "UE56 + U139 (slicing)",
        "UE112",
        "UE49",
    ]
    Tnames = [
        "Landau + BAM WLS7",
        "MPW",
        "U41",
        "UE49",
        "UE46",
        "CPMU17 + UE48 (EMIL)",
        "PSF WLS7",
        "Cavities",
    ]
    names = {
        "D": Dnames,
        "T": Tnames,
        "S": np.core.defchararray.add(Dnames, np.core.defchararray.add(" + ", Tnames)),
    }

    def __init__(self, lypos=25, lysize=3, zorderoffset=100):
        self.lypos = lypos
        self.lysize = lysize
        self.zorderoffset = zorderoffset

    def getrolled(self, s, y, fmt=None):  # access lattice from -120 to 120m
        x = np.array(s, dtype=np.float64)
        y = np.array(y, dtype=np.float64)
        x[x > 120] = x[x > 120] - 240.0
        ishift = np.argmax(x < 0)
        # print len(x),ishift
        x = np.roll(x, -ishift)
        y = np.roll(y, -ishift)
        if fmt:
            return x, y, fmt
        else:
            return x, y

    # Note:
    # It seem elegant twiss-ouput always prints the length, type and name
    # at the END of the element (!)
    #
    # Check element list
    # print np.unique(twi.ElementType)
    # ['CSBEND' 'DRIF' 'KQUAD' 'KSEXT' 'MALIGN' 'MARK' 'RECIRC' 'WATCH']
    #
    def paintlattice(
        self,
        d,
        s0,
        s1,
        ycenter=None,
        ysize=None,
        ec=True,
        labels=True,
        rolled=False,
        fscale=1.0,
        floorCoordinates=False,
    ):
        if ycenter is None:
            ycenter = self.lypos
        if ysize is None:
            ysize = self.lysize
        s = np.array(d.s, dtype=np.float64)
        et = d.ElementType
        en = d.ElementName
        angle = 0
        if floorCoordinates:
            Z = np.array(d.Z, dtype=np.float64)
            X = np.array(d.X, dtype=np.float64)
            theta = np.array(d.theta, dtype=np.float64)
        if rolled:
            s[s > 120] = s[s > 120] - 240.0
            ishift = np.argmax(s < 0)
            s = np.roll(s, -ishift)
            et = np.roll(et, -ishift)
            en = np.roll(en, -ishift)

        i0 = np.argmax(s >= s0)
        i1 = np.argmax(s >= s1)
        # print i0,i1
        start = s0
        for i in range(i0, i1 + 1):
            # save start if previous element was something else
            if i > i0:
                if et[i] != et[i - 1]:
                    start = s[i - 1]
            # skip if next element of same type
            if i < i1:
                if et[i] == et[i + 1]:
                    continue
            end = np.min((s[i], s1))
            l = end - start
            # print i, s[i], et[i], en[i], '    length of element:', l
            if floorCoordinates:
                istart = s == start
                angle = theta[istart][-1] / np.pi * 180
                start = Z[istart][-1] + np.sin(theta[i]) * 0.5 * ysize
                ycenter = X[istart][-1] + 0.5 * ysize - np.cos(theta[i]) * 0.5 * ysize
            col = "none"
            ecol = "k"
            if et[i] == "CSBEND":
                col = "yellow"
                ecol = "black"
                if floorCoordinates:
                    # HACK for BESSY II and MLS dipoles
                    if en[i] in ("B", "BB", "BEND"):
                        if abs(angle + 180.0) < 1e-9:
                            angle = angle + 360
                        angle = 0.5 * (angle + theta[i] / np.pi * 180)
                    if en[i] in ("B3ID", "B2ID", "B1ID"):
                        angle = theta[en == "B3ID"][-1] / np.pi * 180

            if et[i] == "KQUAD":
                col = "red"
            if et[i] == "KSEXT":
                col = "green"
            if et[i] == "KOCT":
                col = "black"
            if not ec:
                ecol = "none"

            if col != "none":
                gca().add_patch(
                    patches.Rectangle(
                        (start, ycenter - 0.5 * ysize),
                        l,
                        ysize,
                        ec=ecol,
                        facecolor=col,
                        clip_on=False,
                        zorder=self.zorderoffset + 1,
                        angle=angle,
                    )
                )
                if labels:
                    fs = 80 / (s1 - s0) * fscale
                    # TODO fixes for floorCoordinates:
                    if et[i] == "KSEXT":
                        annotate(
                            en[i],
                            xy=(start, ycenter),
                            xytext=(start + 0.5 * l, ycenter - 0.55 * ysize),
                            fontsize=fs,
                            va="top",
                            ha="center",
                            clip_on=False,
                            zorder=self.zorderoffset + 2,
                        )
                    else:
                        annotate(
                            en[i],
                            xy=(start, ycenter),
                            xytext=(start + 0.5 * l, ycenter + 0.5 * ysize),
                            fontsize=fs,
                            va="bottom",
                            ha="center",
                            clip_on=False,
                            zorder=self.zorderoffset + 2,
                        )
        # print d.ElementType

    def axislabels(self, yscale=1, Dfac=10):
        xlabel("s / m")
        # ylabel('beta function / m        dispertion / 0.1m')
        # ylabel('$\\beta / \mathrm{m}$        $\\eta_x / 10\mathrm{cm}$')

        ybox3 = TextArea(
            "       $\\eta_x / {0}".format(int(100 / Dfac)) + "\mathrm{cm}$",
            textprops=dict(color="r", rotation=90, ha="left", va="center"),
        )
        ybox1 = TextArea(
            "  $\\beta_y / \mathrm{m}$",
            textprops=dict(color="b", rotation=90, ha="left", va="center"),
        )
        ybox2 = TextArea(
            "$\\beta_x / \mathrm{m}$",
            textprops=dict(color="g", rotation=90, ha="left", va="center"),
        )
        ybox = VPacker(children=[ybox3, ybox1, ybox2], align="bottom", pad=0, sep=5)
        anchored_ybox = AnchoredOffsetbox(
            loc=8,
            child=ybox,
            pad=0.0,
            frameon=False,
            bbox_to_anchor=(-0.08 * yscale, 0.15),
            bbox_transform=gca().transAxes,
            borderpad=0.0,
        )
        gca().add_artist(anchored_ybox)
        # ylim(-1)

    def plotsection(self, d, stype, nr):
        s0 = (nr - 1) * 30.0 - 7.5
        if stype == "T":
            s0 += 15.0
        if stype == "S":
            s1 = s0 + 30.0
        else:
            s1 = s0 + 15.0

        if stype == "D" and nr == 1:
            plot(*self.getrolled(d.s, d.betax, "g-"))
            plot(*self.getrolled(d.s, d.betay, "b-"))
            x, y, = self.getrolled(d.s, d.etax)
            plot(x, 10 * y, "r-")
            rolled = True
        else:
            plot(d.s, d.betax, "g-")
            plot(d.s, d.betay, "b-")
            plot(d.s, 10 * np.array(d.etax, dtype=np.float64), "r-")
            rolled = False

        annotate(
            stype + "{0:0n}".format(nr),
            xy=((s1 + s0) / 2.0, 25 - 5),
            fontsize=20,
            ha="center",
            va="top",
            zorder=self.zorderoffset + 5,
        )
        gca().yaxis.grid(alpha=0.3, zorder=0)

        #    print stype, names[stype][nr-1], names[stype]
        annotate(
            "" + self.names[stype][nr - 1] + "",
            xy=((s1 + s0) / 2.0, 25 - 9),
            fontsize=8,
            ha="center",
            va="top",
            zorder=self.zorderoffset + 5,
        )

        self.paintlattice(d, s0, s1, self.lypos, self.lysize, ec=True, rolled=rolled)
        self.axislabels()
        xlim(s0, s1)
