import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from sddshzb import SDDSad
from sddshzb import Twissplot

dataf = SDDSad(0)
dataf.load("output.flr")
data = dataf.columnDataDict

# Print out contained data
print("\nDescription:", dataf.description)
print("\n", len(dataf.parameterName), "Paramters:\n", dataf.parameterName)
print("\n", len(dataf.columnName), "Columns:\n", dataf.columnName)

# Plot whole ring

plt.figure(figsize=(36, 36))
plt.plot(data.Z, data.X, "-")

c = np.max(np.array(data.s, dtype=np.float64))

tp = Twissplot(lysize=0.5)  # ,lypos, lysize = lypos*0.12)
tp.paintlattice(data, 0, c, ec=True, fscale=12, floorCoordinates=True)


plt.xlim(-40, 40)
plt.ylim(-78, 2)

plt.grid()

plt.subplots_adjust(top=0.98, left=0.02, right=0.98, bottom=0.02)
plt.savefig("floor.pdf")
