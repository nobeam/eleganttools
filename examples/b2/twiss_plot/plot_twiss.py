import numpy as np
import matplotlib.pyplot as plt

from eleganttools import SDDS, draw_lattice, axis_labels, plot_bessy2_section
import click


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--title", required=False, default="BESSY II", help="Title for figure")
def main(file, title):
    """Plot twiss data, where FILE is the path to the SDDS file."""
    # Load twiss data as Python dict
    twiss = SDDS(file).as_dict()

    # Length of ring
    lattice_length = twiss["s"][-1]

    # Create figure in golden ratio (A paper sizes)
    figsizeinch = 14
    fig = plt.figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))

    # Plot whole ring
    ax = plt.subplot(311)
    ax.plot(twiss["s"], twiss["betax"], "r-")
    ax.plot(twiss["s"], twiss["betay"], "b-")
    ax.plot(twiss["s"], 10 * np.array(twiss["etax"]), "g-")

    # Lattice graphics vertical position and size (axis coordinates!)
    axis_labels(yscale=0.5)
    draw_lattice(twiss, (0, lattice_length), labels=False)

    ax.set_xlim(0, lattice_length)
    ax.set_xticks(np.linspace(0, 240, 17, endpoint=True))
    ax.set_xticks(np.linspace(7.5, 232.5, 16, endpoint=True), minor=True)
    ax.xaxis.grid(which="minor")
    ax.yaxis.grid(alpha=0.3, zorder=0)

    # Print some headline information
    fig.suptitle(title, ha="left", fontsize=20, x=0.025)

    params = {"length": lattice_length, "E_GeV": twiss["pCentral"] / 3913.90152459 * 2}
    params.update(
        (k, twiss[k])
        for k in ["nux", "nuy", "alphac", "dnux/dp", "dnuy/dp", "U0", "Sdelta0", "ex0"]
    )

    for i, (key, value) in enumerate(params.items()):
        xpos = int(i / 4) * 0.18 + 0.5
        ypos = -int(i % 4) * 0.07 + 1.32
        plt.annotate(
            f"{key} = {value:12.6e}",
            xy=(xpos, ypos),
            va="center",
            xycoords="axes fraction",
        )

    # Plot 4 interesting sections
    plt.subplot(323)
    plot_bessy2_section(twiss, "D1")

    plt.subplot(324)
    plot_bessy2_section(twiss, "T6")

    plt.subplot(325)
    plot_bessy2_section(twiss, "D6")

    plt.subplot(326)
    plot_bessy2_section(twiss, "T8")

    # Efficient Plot Adjustment
    fig.subplots_adjust(top=0.9, left=0.05, right=0.98, bottom=0.05, hspace=0.3)
    plt.savefig("twiss.pdf")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
