from itertools import groupby

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, VPacker

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

red = "#EF4444"
yellow = "#FBBF24"
green = "#10B981"
blue = "#3B82F6"

COLOR_MAP = {
    "CSBEND": yellow,
    "KQUAD": red,
    "QUAD": red,
    "KSEXT": green,
    "KOCT": blue,
}


def draw_elements(ax, data, *, labels=True):
    """Draw lattice on matplotlib axes."""
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    rect_height = 0.05 * (y_max - y_min)
    y_max += rect_height
    ax.set_ylim(y_min, y_max)

    positions = data["s"]
    element_types = data["ElementType"]
    element_names = data["ElementName"]

    sign = -1
    i = -1
    start = end = 0
    for element_name, group in groupby(element_names):
        start = end
        i += len(list(group))
        end = positions[i]
        if end <= x_min:
            continue
        elif start >= x_max:
            break

        try:
            color = COLOR_MAP[element_types[i]]
        except KeyError:
            continue

        ax.add_patch(
            plt.Rectangle(
                (start, y_max - 0.5 * rect_height),
                min(end, x_max) - max(start, x_min),
                rect_height,
                facecolor=color,
                clip_on=False,
                zorder=10,
            )
        )
        if labels:
            sign = -sign
            plt.annotate(
                element_name,
                xy=((start + end) / 2, y_max + sign * rect_height),
                fontsize=5,
                va="center",
                ha="center",
                annotation_clip=False,
                zorder=11,
            )


def axis_labels(ax, *, eta_x_scale=10):
    plt.xlabel("s / m")
    text_areas = [
        TextArea(
            rf"{eta_x_scale} $\eta_x$ / m",
            textprops=dict(color=green, rotation=90),
        ),
        TextArea(
            r"$\beta_y$ / m",
            textprops=dict(color=blue, rotation=90),
        ),
        TextArea(
            r"$\beta_x$ / m",
            textprops=dict(color=red, rotation=90),
        ),
    ]
    ax.add_artist(
        AnchoredOffsetbox(
            child=VPacker(children=text_areas, align="bottom", pad=0, sep=20),
            loc="center left",
            bbox_to_anchor=(-0.125, 0, 1.125, 1),
            bbox_transform=ax.transAxes,
            frameon=False,
        )
    )


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

    axis_labels(ax)
    ax.set_xlim(s0, s1)
    draw_elements(ax, data)
