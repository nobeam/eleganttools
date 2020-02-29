import numpy as np
import matplotlib.pyplot as plt

import matplotlib.patches as patches
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, VPacker

from . import sdds


class Twissplot:
    Dnames = (
        "Injection",
        "U125",
        "UE56",
        "U49",
        "UE52",
        "UE56 + U139 (slicing)",
        "UE112",
        "UE49",
    )
    Tnames = (
        "Landau + BAM WLS7",
        "MPW",
        "U41",
        "UE49",
        "UE46",
        "CPMU17 + UE48 (EMIL)",
        "PSF WLS7",
        "Cavities",
    )
    names = {
        "D": Dnames,
        "T": Tnames,
        "S": np.core.defchararray.add(Dnames, np.core.defchararray.add(" + ", Tnames)),
    }

    def __init__(self, lypos=25, lysize=3, zorderoffset=100):
        self.lypos = lypos
        self.lysize = lysize
        self.zorderoffset = zorderoffset

    def get_rolled(self, s, y, fmt=None):  # access lattice from -120 to 120m
        x = np.array(s, dtype=np.float64)
        y = np.array(y, dtype=np.float64)
        x[x > 120] = x[x > 120] - 240.0
        ishift = np.argmax(x < 0)
        x = np.roll(x, -ishift)
        y = np.roll(y, -ishift)
        if fmt:
            return x, y, fmt
        else:
            return x, y

    # Note:
    # It seem elegant twiss-ouput always prints the length, type and name
    # at the END of the element (!)
    # Check element list
    # print np.unique(twi.ElementType)
    # ['CSBEND' 'DRIF' 'KQUAD' 'KSEXT' 'MALIGN' 'MARK' 'RECIRC' 'WATCH']
    def paint_lattice(
        self,
        data,
        s0,
        s1,
        y_center=None,
        y_size=None,
        ec=True,
        labels=True,
        rolled=False,
        fscale=1.0,
        floorCoordinates=False,
    ):
        if y_center is None:
            y_center = self.lypos
        if y_size is None:
            y_size = self.lysize
        s = np.array(data["s"], dtype=np.float64)
        et = data["ElementType"]
        en = data["ElementName"]
        angle = 0
        if floorCoordinates:
            Z = np.array(data["Z"], dtype=np.float64)
            X = np.array(data["X"], dtype=np.float64)
            theta = np.array(data["theta"], dtype=np.float64)
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
                start = Z[istart][-1] + np.sin(theta[i]) * 0.5 * y_size
                y_center = (
                    X[istart][-1] + 0.5 * y_size - np.cos(theta[i]) * 0.5 * y_size
                )
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
                plt.gca().add_patch(
                    patches.Rectangle(
                        (start, y_center - 0.5 * y_size),
                        l,
                        y_size,
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
                        plt.annotate(
                            en[i],
                            xy=(start, y_center),
                            xytext=(start + 0.5 * l, y_center - 0.55 * y_size),
                            fontsize=fs,
                            va="top",
                            ha="center",
                            clip_on=False,
                            zorder=self.zorderoffset + 2,
                        )
                    else:
                        plt.annotate(
                            en[i],
                            xy=(start, y_center),
                            xytext=(start + 0.5 * l, y_center + 0.5 * y_size),
                            fontsize=fs,
                            va="bottom",
                            ha="center",
                            clip_on=False,
                            zorder=self.zorderoffset + 2,
                        )

    def axis_labels(self, yscale=1, Dfac=10):
        plt.xlabel("s / m")

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
            bbox_transform=plt.gca().transAxes,
            borderpad=0.0,
        )
        plt.gca().add_artist(anchored_ybox)

    def plot_section(self, data, s_lim, section_name=""):
        s, beta_x, beta_y, eta_x = (
            data[key] for key in ("s", "betax", "betay", "etax")
        )
        s0, s1 = s_lim
        plt.plot(s, beta_x, "g-")
        plt.plot(s, beta_y, "b-")
        plt.plot(s, 10 * np.array(eta_x, dtype=np.float64), "r-")
        rolled = False

        plt.annotate(
            section_name,
            xy=((s1 + s0) / 2.0, 25 - 5),
            fontsize=20,
            ha="center",
            va="top",
            zorder=self.zorderoffset + 5,
        )
        plt.gca().yaxis.grid(alpha=0.3, zorder=0)

        section_type, section_number = section_name
        plt.annotate(
            "" + self.names[section_type][int(section_number) - 1] + "",
            xy=((s1 + s0) / 2.0, 25 - 9),
            fontsize=8,
            ha="center",
            va="top",
            zorder=self.zorderoffset + 5,
        )

        self.paint_lattice(
            data, s0, s1, self.lypos, self.lysize, ec=True, rolled=rolled
        )
        self.axis_labels()
        plt.xlim(s0, s1)
