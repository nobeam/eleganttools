import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from eleganttools import SDDS, draw_elements

data = SDDS("data.flr").as_dict()

plt.figure(figsize=(8, 8))
plt.plot(data["Z"], data["X"], "-")  # TODO: draw magnets
plt.xlim(-40, 40)
plt.ylim(-78, 2)
plt.grid()
plt.savefig("floor.pdf")
