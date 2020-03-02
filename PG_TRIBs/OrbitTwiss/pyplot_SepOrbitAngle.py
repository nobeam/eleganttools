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

# Length of ring
C = np.max(np.array(clo3IB.s,dtype=np.float64))
print '\n clo3IB...', len(clo3IB), clo3IB.keys(), C
# print len(clo3IB.s), len(cen.s)

print type(clo3IB.ElementName), len(clo3IB.ElementName)


### Observation points in straights
###
sMarksPoints = ["MD1","MD2","MD3","MD4","MD5","MD6A","MD6B","MD7","MD8",  "MT1","MT2","MT3","MT4","MT5","MT6A","MT6B","MT7","MT8"]
sIDs = ['Inj','U125','UE56','U49','UE52','U139','UE56','UE112','UE49', 		'BAM','MPW','U41','UE49','UE46','CPMU17','UE48','PSF','Cav']

# print "\n", sMarksPoints
xOneMarks = []
xMarksAll = []
xpOneMarks = []
xpMarksAll = []
for x in sMarksPoints:
	i=0
	# print x
	for elename in clo3IB.ElementName:
		# print i, clo3IB.s[i], clo3IB.ElementName[i]
		# if clo3IB.ElementName[i] == x: print i, "s = ", clo3IB.s[i], "eleName = ", clo3IB.ElementName[i], 1.0e3*np.array(clo3IB.x[i],dtype=np.float64), 1.0e3*np.array(clo3IB.xp[i],dtype=np.float64)
		if clo3IB.ElementName[i] == x: 
			xOneMarks.append(1.0e3*np.array(clo3IB.x[i],dtype=np.float64))
			xpOneMarks.append(1.0e3*np.array(clo3IB.xp[i],dtype=np.float64))
			# print x, xpOneMarks
		i += 1
	xMarksAll.append(xOneMarks)
	xpMarksAll.append(xpOneMarks)
	xOneMarks = []
	xpOneMarks = []
	
# print "\n xMarksAll =", xMarksAll, len(xMarksAll)
# print "\n xpMarksAll =", xpMarksAll, len(xpMarksAll)
# print "\n test1 =", xMarksAll[1][:], xpMarksAll[1][:]
# print len(sMarksPoints), len(xMarksAll), len(xpMarksAll)

# xMarksAll = np.asarray(xMarksAll)
# xpMarksAll = np.asarray(xpMarksAll)
# print type(sMarksPoints), type(xMarksAll), type(xpMarksAll)

# np.set_printoptions(precision=3, linewidth=60)
i=0
for x in sMarksPoints:
	# print x, xMarksAll[i], xpMarksAll[i]
	# print x, max(xMarksAll[i]), max(xpMarksAll[i])
	# print x, np.around(xMarksAll[i],decimals=3), xpMarksAll[i]
	# print x, ["%0.3f" % a for a in xMarksAll[i]]
	print '{0:4} {1:6} {2:6} {3:6}'.format(x[1:], sIDs[i], np.around(xMarksAll[i],decimals=3), np.around(xpMarksAll[i],decimals=3))
	i += 1

###
###

# i=2
# for x in clo3IB.ElementName[i:10]:
# i=8300
# for x in clo3IB.ElementName[i:-1]:
	# print i, x, clo3IB.s[i]
	# i += 1

### Summation over all orbit angle changes 
#a = clo3IB.xp[0].astype(np.float)
#xpsum = 0.0
#print '\n a = ', a
#for i,x in enumerate(np.array(clo3IB.xp,dtype=np.float64)):
##	print i, a,x, type(a), type(x)
#	if x!=a:	
#		w=abs(abs(x)-abs(a))
#		print i, a,x, type(a), type(x), w, xpsum
#		a = x
#		xpsum += w
###	
	
	
	
sturn = clo3IB.s[2:-1]
xturn = clo3IB.x[2:-1] 
xpturn = clo3IB.xp[2:-1] 
sturn = sturn.astype(np.float)						# in m
xturn = xturn.astype(np.float) *1.0e3 		# from m to mm
xpturn = xpturn.astype(np.float) *1.0e3		# from rad to mrad
# print '\n', len(sturn), type(sturn), type(sturn[0]), sturn
npoints = (len(sturn) - 1)/3
print '\n npoints', npoints
	
sturn1 = sturn[0*npoints : 1*npoints+1]
sturn2 = sturn[1*npoints : 2*npoints+1]
sturn3 = sturn[2*npoints : 3*npoints+1]

xturn1 = xturn[0*npoints : 1*npoints+1] 
xturn2 = xturn[1*npoints : 2*npoints+1] 
xturn3 = xturn[2*npoints : 3*npoints+1]

xpturn1 = xpturn[0*npoints : 1*npoints+1] 
xpturn2 = xpturn[1*npoints : 2*npoints+1] 
xpturn3 = xpturn[2*npoints : 3*npoints+1]

# sturn1 = clo3IB.s[0:2753]
# sturn2 = clo3IB.s[2752:5505]
# sturn3 = clo3IB.s[5504:8257]

# xturn1 = clo3IB.x[0:2753]
# xturn2 = clo3IB.x[2752:5505]
# xturn3 = clo3IB.x[5504:8257]

# print '\n', len(sturn1), len(xturn1), len(xturn2), len(xturn3), len(xpturn1), len(xpturn2), len(xpturn3)
# print type(sturn1), sturn1
# print type(sturn2), sturn2
# print type(sturn3), sturn3


# ## Create figure in golden ratio (A paper sizes)
# fig, (axOrbit, axAngle) = plt.subplots(2, 1, sharex=True, figsize=(15,8))
figsizeinch = 14
fig, (axOrbit, axAngle) = plt.subplots(2, 1, sharex=True, figsize=(figsizeinch,figsizeinch * 0.14**.5))
axOrbit.plot([0.0, C/3.0], [0.0, 0.0], 'k-', lw=1)
axOrbit.plot(sturn1, xturn1, 'r-', lw=2, label='1st turn')
axOrbit.plot(sturn1, xturn2, 'b-', lw=2, label='2nd turn')
axOrbit.plot(sturn1, xturn3, 'g-', lw=2, label='3rd turn')
axOrbit.set_ylim(-8.7,8.7)
# axOrbit.set_ylim(-2.0,2.0)
axOrbit.set_ylabel('Displacement x / mm ', size=14)
axOrbit.tick_params(axis='y', labelsize=12)

axOrbit.text(120.0, 10.2, "PRELIMINARY", fontsize=40,ha='center',va='top')
# axOrbit.annotate('PRELIMINARY', xy=(120.0,8.6), ha='center',va='top',fontsize=40)


axAngle.plot([0.0, C/3.0], [0.0, 0.0], 'k-', lw=1)
axAngle.plot(sturn1, xpturn1, 'r-', lw=2, label='1st turn')
axAngle.plot(sturn1, xpturn2, 'b-', lw=2, label='2nd turn')
axAngle.plot(sturn1, xpturn3, 'g-', lw=2, label='3rd turn')
axAngle.set_ylim(-6.8,6.8)
# axAngle.set_ylim(-4.2,4.2)
axAngle.set_ylabel('Angle xp / mrad ', size=14)
axAngle.tick_params(axis='y', labelsize=12)



xlim(0,C/3.0)
# xlim(30.0,40.0) #PinHole3
# xlim(120.0,130.0) #PinHole9
# xlim(45.0, 75.0) D3 UE56XMCD


## xlim(0,C/(4.0*3.0))
xlabel('Position s / m', size=16)
xticks(size=14)
#yticks(size=12)

legend(ncol = 4, loc=3, frameon=True)

lypos = gca().get_ylim()[1]
tp = Twissplot(lypos = lypos, lysize = lypos*0.15)
tp.paintlattice(clo3IB,0,C/3.0, ec=False, labels=False, fscale=20)
tp.plotstraightnames(12,8,0.8)


# ax = plt.axes()
axOrbit.xaxis.set_major_locator(ticker.MultipleLocator(15))
axOrbit.xaxis.set_minor_locator(ticker.MultipleLocator(5))
axOrbit.yaxis.set_major_locator(ticker.MultipleLocator(2))
axOrbit.yaxis.set_minor_locator(ticker.MultipleLocator(1))
axAngle.yaxis.set_major_locator(ticker.MultipleLocator(2))
axAngle.yaxis.set_minor_locator(ticker.MultipleLocator(1))

# axOrbit.xaxis.set_major_locator(ticker.MultipleLocator(1))
# axOrbit.xaxis.set_minor_locator(ticker.MultipleLocator(1))
# axOrbit.yaxis.set_major_locator(ticker.MultipleLocator(1))
# axOrbit.yaxis.set_minor_locator(ticker.MultipleLocator(1))
# axAngle.yaxis.set_major_locator(ticker.MultipleLocator(2))
# axAngle.yaxis.set_minor_locator(ticker.MultipleLocator(1))

axOrbit.xaxis.grid(which='minor')
axOrbit.yaxis.grid(which='minor')
axAngle.xaxis.grid(which='minor')
axAngle.yaxis.grid(which='minor')


tight_layout()
fig.subplots_adjust(hspace=0)

#savefig('res_SepOrbitAngle.png')
savefig('res_SepOrbitAngle_XXX.png')


