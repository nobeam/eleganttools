import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, VPacker

from .sddslib import SDDS


DOUBLET_NAMES = [
    "Injection",
    "U125",
    "UE56",
    "U49",
    "UE52",
    "UE56 + U139 (slicing)",
    "UE112",
    "UE49",
]
TRIPLET_NAMES = [
    "Landau + BAM WLS7",
    "MPW",
    "U41",
    "UE49",
    "UE46",
    "CPMU17 + UE48 (EMIL)",
    "PSF WLS7",
    "Cavities",
]
SECTION_NAMES = {
    "D": DOUBLET_NAMES,
    "T": TRIPLET_NAMES,
    "S": [d + " + " + t for d, t in zip(DOUBLET_NAMES, TRIPLET_NAMES)],
}


# Note:
# It seem elegant twiss-ouput always prints the length, type and name
# at the END of the element (!)
# Check element list
# print np.unique(twi.ElementType)
# ['CSBEND' 'DRIF' 'KQUAD' 'KSEXT' 'MALIGN' 'MARK' 'RECIRC' 'WATCH']
def draw_lattice(data, s_lim=None, labels=True, ax=None):
    s = np.array(data["s"], dtype=np.float64)
    et = data["ElementType"]
    en = data["ElementName"]
    s0, s1 = s_lim if s_lim is not None else (s[0], s[-1])

    if ax is None:
        ax = plt.gca()

    # get space for labels and rectangles
    y_min, y_max = ax.get_ylim()
    y_span = (y_max - y_min) * 1.1
    y_max = y_min + y_span
    ax.set_ylim(y_min, y_max)
    rect_height = y_span / 32

    i0 = np.argmax(s >= s0)
    i1 = np.argmax(s >= s1)
    start = s0
    for i in range(i0, i1 + 1):
        if i > i0:  # save start if previous element was something else
            if et[i] != et[i - 1]:
                start = s[i - 1]
        if i < i1:  # skip if next element of same type
            if et[i] == et[i + 1]:
                continue

        end = np.min((s[i], s1))
        length = end - start
        if et[i] == "CSBEND":
            face_color = "yellow"
        elif et[i] == "KQUAD":
            face_color = "red"
        elif et[i] == "KSEXT":
            face_color = "green"
        elif et[i] == "KOCT":
            face_color = "black"
        else:
            continue

        retangle = plt.Rectangle(
            (start, y_max - 0.5 * rect_height),
            length,
            rect_height,
            # ec="k",
            facecolor=face_color,
            clip_on=False,
            zorder=10,
        )
        ax.add_patch(retangle)
        if labels:
            fs = 80 / (s1 - s0)
            sign = 1 if et[i] == "KQUAD" else -1
            plt.annotate(
                en[i],
                xy=((end + start) / 2, y_max + sign * 1.5 * rect_height),
                fontsize=fs,
                va="center",
                ha="center",
                annotation_clip=False,
                zorder=100,
            )


def axis_labels(yscale=1, eta_x_scale=10, ax=None):
    if ax is None:
        ax = plt.gca()

    plt.xlabel("s / m")
    ybox1 = TextArea(
        "       $\\eta_x / {0}".format(int(100 / eta_x_scale)) + "\mathrm{cm}$",
        textprops=dict(color="g", rotation=90, ha="left", va="center"),
    )
    ybox2 = TextArea(
        "  $\\beta_y / \\mathrm{m}$",
        textprops=dict(color="b", rotation=90, ha="left", va="center"),
    )
    ybox3 = TextArea(
        "$\\beta_x / \\mathrm{m}$",
        textprops=dict(color="r", rotation=90, ha="left", va="center"),
    )
    ybox = VPacker(children=[ybox1, ybox2, ybox3], align="bottom", pad=0, sep=5)
    anchored_ybox = AnchoredOffsetbox(
        loc=8,
        child=ybox,
        pad=0.0,
        frameon=False,
        bbox_to_anchor=(-0.08 * yscale, 0.15),
        bbox_transform=plt.gca().transAxes,
        borderpad=0.0,
    )
    ax.add_artist(anchored_ybox)


def plot_bessy2_section(data, section_name, ax=None):
    """Section name must be 'T'/'D'/'S' plus a number, where 'S' indicates 'D' + 'T'."""
    s, beta_x, beta_y, eta_x = (data[key] for key in ("s", "betax", "betay", "etax"))
    section_type, section_number = section_name[0], int(section_name[1]) - 1
    s0 = section_number * 30.0 - 7.5
    if section_type == "T":
        s0 += 15.0
        s1 = s0 + 15.0
    elif section_type == "D":
        s1 = s0 + 15.0
    elif section_type == "S" or section_number:
        s1 = s0 + 30.0
    else:
        raise Exception(f"Unknown section name: {section_name}")

    if ax is None:
        ax = plt.gca()

    ax.plot(s, beta_x, "r-")
    ax.plot(s, beta_y, "b-")
    ax.plot(s, 10 * np.array(eta_x, dtype=np.float64), "g-")

    y0, y1 = ax.get_ylim()
    y_span = y1 - y0
    label = SECTION_NAMES[section_type][section_number]
    ax.annotate(label, ((s1 + s0) / 2.0, y1 - y_span * 0.1), fontsize=10, ha="center")
    ax.yaxis.grid(alpha=0.3, zorder=0)

    draw_lattice(data, (s0, s1))
    axis_labels()
    ax.set_xlim(s0, s1)
