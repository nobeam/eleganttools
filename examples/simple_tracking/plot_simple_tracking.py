import matplotlib.pyplot as plt
from eleganttools import SDDS

data = SDDS("output.w1").as_dict()

fig, axes = plt.subplots(3, 3, figsize=(12, 9))

for ax, (x, y) in zip(
    axes.flatten(),
    [
        ("Pass", "Cx"),
        ("Pass", "Cxp"),
        ("Cx", "Cxp"),
        ("Pass", "Cy"),
        ("Pass", "Cyp"),
        ("Cy", "Cyp"),
        ("Pass", "dCt"),
        ("Pass", "Cdelta"),
        ("dCt", "Cdelta"),
    ],
):
    ax.plot(data[x], data[y], ",")
    ax.set_xlabel(x)
    ax.set_ylabel(y)


plt.tight_layout()
plt.savefig("tracking.pdf")
