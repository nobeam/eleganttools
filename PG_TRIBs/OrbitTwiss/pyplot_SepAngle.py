#!/usr/bin/env python2
import matplotlib
matplotlib.use('Agg')
from pylab import *
# import matplotlib.patches as patches
import matplotlib.ticker as ticker
import numpy as np

from sddshzb import SDDSad
from sddshzb import Twissplot
import sys
maintitle = subtitle  = ''
if len(sys.argv) > 1:
    maintitle =  sys.argv[1]    
if len(sys.argv) > 2:
    subtitle =  sys.argv[2]

# Usage example:
# python plotTwiss.py 'BESSY II std. user 15.06.2016' BII_2016-06-10_user_PartialSplit_noID_CurrentUserMode.lte

# Initialize SDDS object and load sdds file with twiss table
sdds =SDDSad(0)
sdds.load('output_3IB.clo')
# Get convenient attribute dictionary
clo3IB = sdds.columnDataDict
print '\n type of clo3IB = ' , type(clo3IB)

sdds.load('output_Core3x.clo')
cloCore = sdds.columnDataDict


# Length of ring
C = np.max(np.array(clo3IB.s,dtype=np.float64))
print '\n clo3IB...', len(clo3IB), clo3IB.keys(), C
print '\n cloCore...', len(cloCore), cloCore.keys(), C
# print len(clo3IB.s), len(cen.s)

sturn = clo3IB.s[2:-1]
xturn = clo3IB.xp[2:-1] 
sturn = sturn.astype(np.float)						# in m
# xturn = xturn.astype(np.float) 					# in rad
xturn = xturn.astype(np.float) *1.0e3 		# from m to mm  or  rad to mrad
# print '\n', len(sturn), type(sturn), type(sturn[0]), sturn
npoints = (len(sturn) - 1)/3
print 'npoints', npoints
	
sturn1 = sturn[0*npoints : 1*npoints+1]
sturn2 = sturn[1*npoints : 2*npoints+1]
sturn3 = sturn[2*npoints : 3*npoints+1]

xturn1 = xturn[0*npoints : 1*npoints+1] 
xturn2 = xturn[1*npoints : 2*npoints+1] 
xturn3 = xturn[2*npoints : 3*npoints+1]

# sturn1 = clo3IB.s[0:2753]
# sturn2 = clo3IB.s[2752:5505]
# sturn3 = clo3IB.s[5504:8257]

# xturn1 = clo3IB.x[0:2753]
# xturn2 = clo3IB.x[2752:5505]
# xturn3 = clo3IB.x[5504:8257]

print '\n', len(sturn1), len(xturn1), len(sturn2), len(xturn2), len(sturn3), len(xturn3)
print type(sturn1), sturn1
print type(sturn2), sturn2
print type(sturn3), sturn3


score = cloCore.s[2:-1]
xcore = cloCore.xp[2:-1]
score = score.astype(np.float)
# xcore = xcore.astype(np.float)
xcore = xcore.astype(np.float) *1.0e3 		# from m to mm
# xcore = xcore.astype(np.float) *1.0e12 		# from m to pm

score = score[0*npoints : 1*npoints+1]
xcore = xcore[0*npoints : 1*npoints+1]


# Create figure in golden ratio (A paper sizes)
figsizeinch = 14
# fig = figure(figsize=(figsizeinch,figsizeinch * 0.5**.5))		# GoldenRatio
fig = figure(figsize=(figsizeinch,figsizeinch * 0.1**.5))

# plot(cen.s, cen.Cx,  'k-', lw=2, label='core orbit')
plot(score, xcore, 	 'k-', lw=1, label='core')
plot(sturn1, xturn1, 'r-', lw=2, label='1st turn')
plot(sturn1, xturn2, 'b-', lw=2, label='2nd turn')
plot(sturn1, xturn3, 'g-', lw=2, label='3rd turn')
xlim(0,C/3.0)
# xlim(0,C/(4.0*3.0))
xlabel('Position s / m', size=18)
xticks(size=16)
ylim(-7.5,7.5)
ylabel('Orbit Angle xp / mrad ', size=18)
yticks(size=16)

ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(15))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

gca().xaxis.grid(which='minor')
gca().yaxis.grid(which='major')
# gca().yaxis.grid(alpha=0.3, zorder=0)


legend(ncol = 4, loc=3, frameon=True)

lypos = gca().get_ylim()[1]
tp = Twissplot(lypos = lypos, lysize = lypos*0.15)
tp.paintlattice(clo3IB,0,C/3.0, ec=False, labels=False, fscale=20)
tp.plotstraightnames(12,8,0.8)

## tp.plotstraightnames() 
# straights = ['Injection','Landau + BAM','U125','MPW','UE56','U41','U49','UE49','UE52','UE46','U139 + UE56 \n (Slicing)','CPMU17 + UE48 \n (EMIL)','UE112','PSF','UE49','Cavities']
# for i in range(0,16):
	# ha='center'
	# x = i * 15
#	print i, x, i%2, i/2, straights[i]
	# if i == 0:
		# ha='left'
		# x = 0.5
	# if i%2 == 0:	annotate('D{0}'.format(i/2 +1), xy=(x,lypos*0.9), ha=ha,va='top',zorder=105)
	# if i%2 == 1:	annotate('T{0}'.format(i/2 +1), xy=(x,lypos*0.9), ha=ha,va='top',zorder=105)
	# annotate(straights[i], xy=(x,lypos*0.80), fontsize=6, ha=ha,va='top',zorder=105)

tight_layout()
# savefig('res_SepOrbit.png')
savefig('res_SepAngle.png')


