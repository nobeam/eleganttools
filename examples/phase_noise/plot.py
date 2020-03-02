#!/usr/bin/env python2
import matplotlib

matplotlib.use("Agg")
from pylab import *
import matplotlib.patches as patches

from sddshzb import SDDSad
import sys

# Initialize SDDS object and load sdds file from a centroid watchpoint
W = SDDSad(0)


fig = figure(figsize=(12, 9))


def eleplot(x, y, sel=None, label=None):
    global data
    print x, y
    plot(data[x], data[y], "-", label=label)
    xlabel(x)
    ylabel(y)


W.load("output.w1")
# Get convenient attribute dictionary
data = W.columnDataDict


clf()
# subplot(221)
# eleplot('Pass','Particles')
# plot(data.Pass, data.Particles,'-')
subplot(221)
eleplot("Pass", "St")

subplot(223)
eleplot("Pass", "dCt")
# plot(data.Pass, data.St,'-')
subplot(222)
eleplot("Pass", "Sdelta")
# plot(data.Pass, data.Sdelta,'-')
subplot(224)
eleplot("Pass", "Cdelta")
# plot(data.Pass, data.Ct,'-')

tight_layout()
savefig("tracking3.pdf")


bl = loadtxt("bl.txt")

clf()

fig = figure(figsize=(8, 8))

freqs = bl[:, 0]
Sta = bl[:, 1]
dCta = bl[:, 2]


subplot(211)
title("phase noise amplitude: 20 ps peak-to-peak")
plot(freqs, Sta * 1e12, "o")
ylabel("(bunch length) St average / ps")
xlabel("f / Hz")
grid()
xscale("log")
xlim(15)

subplot(212)
plot(freqs, dCta * 1e12, "o")
ylabel("dCt peak to peak / ps")
xlabel("phase noise f / Hz")
grid()
xscale("log")
yscale("log")
xlim(15)
tight_layout()
savefig("noise.pdf")


sys.exit()


# Print out contained data
print "\nDescription:", W.description
print "\n", len(W.parameterName), "Paramters:\n", W.parameterName
print "\n", len(W.columnName), "Columns:\n", W.columnName


subplot(331)
eleplot("Pass", "dCt")
subplot(334)
eleplot("Pass", "Cdelta")
subplot(337)
eleplot("dCt", "Cdelta")

subplot(332)
eleplot("Pass", "Cx")
subplot(335)
eleplot("Pass", "Cxp")
subplot(338)
eleplot("Cx", "Cxp")

subplot(333)
eleplot("Pass", "Cy")
subplot(336)
eleplot("Pass", "Cyp")
subplot(339)
eleplot("Cy", "Cyp")


tight_layout()
savefig("tracking.pdf")
