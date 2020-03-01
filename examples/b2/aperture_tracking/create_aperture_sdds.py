import sdds
import numpy as np

tab = np.loadtxt("aperture_raw_table.txt")

output = "aperture.sdds"
x = sdds.SDDS(0)
x.setDescription("aperture file", "")

# # fill Parameters
# Pnames = ["pCentral", "Particles", "IDSlotsPerBunch"]
# Ptypes = [x.SDDS_DOUBLE, x.SDDS_LONG, x.SDDS_LONG]
# parameterData = [[pCentral], [Particles], [IDSlotsPerBunch]]
# for i in range(len(Pnames)):
#     x.defineSimpleParameter(Pnames[i], Ptypes[i])
#     x.setParameterValueList(Pnames[i], parameterData[i])

# fill Columns
Cnames = ["s", "xHalfAperture", "yHalfAperture", "xCenter", "yCenter"]
Ctypes = [x.SDDS_DOUBLE, x.SDDS_DOUBLE, x.SDDS_DOUBLE, x.SDDS_DOUBLE, x.SDDS_DOUBLE]
Cunits = ["m", "m", "m", "m", "m"]
Cdesc = [
    "Distance along the central trajectory",
    "Half aperture in the horizontal",
    "Half aperture in the vertical",
    "Center of the aperture in the horizontal",
    "Center of the aperture in the vertical",
]

for i in range(len(Cnames)):
    # x.defineSimpleColumn(Cnames[i], Ctypes[i])
    # def defineColumn(self, name, symbol, units, description, formatString, type, fieldLength):
    x.defineColumn(Cnames[i], "", Cunits[i], Cdesc[i], "", Ctypes[i], 0)


row = 0


def addpoint(s, data):
    global row
    row += 1
    # s = data[0] *1e-3
    s = s * 1e-3
    xHalfAperture = (data[2] - data[3]) / 2.0 * 1e-3
    yHalfAperture = (data[4] - data[5]) / 2.0 * 1e-3
    xCenter = (data[2] + data[3]) / 2.0 * 1e-3
    yCenter = (data[4] + data[5]) / 2.0 * 1e-3
    x.setColumnValue("s", s, 1, row)
    x.setColumnValue("xHalfAperture", xHalfAperture, 1, row)
    x.setColumnValue("yHalfAperture", yHalfAperture, 1, row)
    x.setColumnValue("xCenter", xCenter, 1, row)
    x.setColumnValue("yCenter", yCenter, 1, row)


olddata = tab[0]
addpoint(tab[0][0], tab[0])
for i in np.arange(len(tab)):
    data = tab[i]
    if np.any(olddata[2:] != data[2:]):
        addpoint(data[0], olddata)
        addpoint(data[0], data)
    olddata = data
addpoint(tab[-1][0], tab[-1])
addpoint(240000, tab[-1])

# needs to be binary for MPI !!
# x.mode = x.SDDS_BINARY
x.mode = x.SDDS_ASCII

x.save(output)
