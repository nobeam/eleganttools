#!/usr/bin/env python2
import matplotlib

matplotlib.use("Agg")
from pylab import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# import matplotlib.gridspec as gridspec
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker


from sddshzb import SDDSad
from sddshzb import Twissplot
import sys

maintitle = subtitle = ""
if len(sys.argv) > 1:
    maintitle = sys.argv[1]
if len(sys.argv) > 2:
    subtitle = sys.argv[2]

# Usage example:
# python plotTwiss.py 'BESSY II std. user 15.06.2016' BII_2016-06-10_user_PartialSplit_noID_CurrentUserMode.lte

# Initialize SDDS object and load sdds file with twiss table
twis = SDDSad(0)
twis.load("output.twi_full")
# Get convenient attribute dictionary
twi = twis.columnDataDict

# Print out contained data
# print "\nDescription:",twis.description
# print "\n",len(twis.parameterName),"Paramters:\n", twis.parameterName
# print "\n",len(twis.columnName),"Columns:\n", twis.columnName


# Length of ring
C = np.max(np.array(twi.s, dtype=np.float64))
print len(twi), twi.keys(), C
# print len(twi),
# print twi.keys()
# print C


# Create figure in golden ratio (A paper sizes)
figsizeinch = 10
fig = figure(figsize=(figsizeinch, figsizeinch * 0.5 ** 0.5))


ax = plt.subplot(211)
plt.plot(twi.s, twi.betax, "g-")
plt.plot(twi.s, twi.betay, "b-")
# plt.plot(twi.s, 10* np.array(twi.etax,dtype=np.float64) , 'r-')
plt.ylim(-1.0, 18.2)
plt.xlim(0.0, C)
plt.tick_params(
    axis="x",  # changes apply to the x-axis
    which="both",  # both major and minor ticks are affected
    bottom="on",  # ticks along the bottom edge are off
    top="on",  # ticks along the top edge are off
    labelbottom="off",
)  # labels along the bottom edge are off
# axes = gca()
# axes.set_ylim([10,20.0])
# plt.ylabel("  $\\beta_y / \mathrm{m}$")

ylab1 = TextArea(
    "$\\beta_y / \mathrm{m}$ ", textprops=dict(color="g", size=15, rotation="vertical")
)
ylab2 = TextArea(
    "$\\beta_x / \mathrm{m}$ ", textprops=dict(color="b", size=15, rotation="vertical")
)
# ylab1 = TextArea("beta x ", textprops=dict(color="g", size=15,rotation='vertical'))
# ylab2 = TextArea("beta y ", textprops=dict(color="b", size=15,rotation='vertical'))
ylab = VPacker(children=[ylab1, ylab2], align="center", pad=0, sep=5)
anchored_ylab = AnchoredOffsetbox(
    loc=8,
    child=ylab,
    pad=0.0,
    frameon=False,
    bbox_to_anchor=(-0.05, 0.4),
    bbox_transform=ax.transAxes,
    borderpad=0.0,
)
ax.add_artist(anchored_ylab)
plt.grid()


plt.subplot(212)
plt.plot(twi.s, 10 * np.array(twi.etax, dtype=np.float64), "r-")
xlim(0, C)
ylim(-4.2, 18)

plt.ylabel("$\\eta_x / \mathrm{m}$", color="r", size=15)
plt.xlabel("s / m")

# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos=lypos, lysize=lypos * 0.08)
# tp.axislabels(yscale=0.8)
tp.paintlattice(twi, 0, C, ec=True, fscale=2)

plt.subplots_adjust(wspace=0, hspace=0)
plt.grid()
plt.tight_layout()
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
savefig("twiss_PG.pdf")


"""

# Plot whole ring
#subplot(111)
plot(twi.s, twi.betax, 'g-')
plot(twi.s, twi.betay, 'b-')
plot(twi.s, 10* np.array(twi.etax,dtype=np.float64) , 'r-')
    
# Latteice graphics vertical position and size (axis coordinates!)
lypos = gca().get_ylim()[1]
tp = Twissplot(lypos = lypos, lysize = lypos*0.12)
tp.axislabels(yscale=0.5)
tp.paintlattice(twi,0,C, ec=False,fscale=2)
xlim(0,C)

# Print some headline information
par = twis.parameterData
#print par
# for key in ('U0','alphac','nux','nuy','dnux/dp','dnuy/dp'):
#     print key, par[key][0]
annotate(maintitle, xy=(-.02, 1.25), fontsize=30, va='center', xycoords='axes fraction')#, annotation_clip=False)
annotate(subtitle, xy=(-.02, 1.11), fontsize=8, va='center', xycoords='axes fraction')
ianno = 0
def annoTwiss(key,value=None):
    global ianno
    xpos = int(ianno / 4) *0.18 + 0.5
    ypos = -int(ianno % 4)*0.07 + 1.32
    ianno += 1
    #print ianno, xpos, ypos
    if value==None:
        value = par[key][0]
    if value < 1e-5:
        annotate('{0:} = {1:12.6e}'.format(key,value), xy=(xpos, ypos), va='center', xycoords='axes fraction')#, annotation_clip=False)
    else:
        annotate('{0:} = {1:12.10f}'.format(key,value), xy=(xpos, ypos), va='center', xycoords='axes fraction')#, annotation_clip=False)
annoTwiss('length',C)
annoTwiss('nux')
annoTwiss('nuy')
annoTwiss('alphac')
annoTwiss('dnux/dp')
annoTwiss('dnuy/dp')
annoTwiss('U0')
annoTwiss('Sdelta0')
annoTwiss('ex0')

for i in range(1,10):
    ha='center'
    if i == 1:
        ha = 'left'
    if i == 9:
        ha = 'right'
    x = i * 30 - 30
    annotate('D{0}'.format(i), xy=(x,lypos*0.9), ha=ha,va='top',zorder=105)
    annotate(tp.names['D'][(i-1)%8],xy=(x,lypos*0.82), fontsize=4,ha=ha,va='top',zorder=105)
    x = i * 30 - 15
    annotate('T{0}'.format(i), xy=(x,lypos*0.9), ha='center',va='top',zorder=105)
    annotate(tp.names['T'][(i-1)%8],xy=(x,lypos*0.82), fontsize=4,ha='center',va='top',zorder=105)
             
gca().set_xticks(linspace(0,240,17,endpoint=True))
gca().set_xticks(linspace(7.5,232.5,16,endpoint=True), minor=True)

gca().xaxis.grid(which='minor')
gca().yaxis.grid(alpha=0.3, zorder=0)


# Plot 4 interesting sections
#subplot(323)
#tp.plotsection(twi,'D',1)

#subplot(324)
#tp.plotsection(twi,'T',6)

#subplot(325)
#tp.plotsection(twi,'D',6)

#subplot(326)
#tp.plotsection(twi,'T',8)

# Efficient Plot Adjustment
subplots_adjust(top=0.5, left=0.08, right=0.88, bottom=0.08, hspace=0.3)

savefig('twiss_pure.pdf')

"""
