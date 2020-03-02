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
sdds.load('output_3IB.twi')
# Get convenient attribute dictionary
twi3IB = sdds.columnDataDict
print '\n type of twi3IB = ' , type(twi3IB)

sdds.load('output_Core3x.twi')
twiCore = sdds.columnDataDict

# Length of ring
C = np.max(np.array(twi3IB.s,dtype=np.float64))
print '\n twi3IB...', len(twi3IB), len(twi3IB.s), twi3IB.keys(), C
# print '\n ', twi3IB.s, twi3IB.pCentral0, twi3IB.ElementName
# i=2
# for x in twi3IB.ElementName[i:10]:
# i=8300
# for x in twi3IB.ElementName[i:-1]:
	# print i, x, twi3IB.s[i]
	# i += 1

s = twi3IB.s[2:-1]
bx3IB = twi3IB.betax[2:-1]
by3IB = twi3IB.betay[2:-1]
etax3IB = twi3IB.etax[2:-1]

bxCore = twiCore.betax[2:-1]
byCore = twiCore.betay[2:-1]
etaxCore = twiCore.etax[2:-1]


s = s.astype(np.float)					# in m
bx3IB = bx3IB.astype(np.float)	# in m
by3IB = by3IB.astype(np.float)	# in m
etax3IB = etax3IB.astype(np.float)		# in m

bxCore = bxCore.astype(np.float)
byCore = byCore.astype(np.float)
etaxCore = etaxCore.astype(np.float)	


print '\n', len(s), type(s), type(s[0]), s
npoints = (len(s) - 1)/3
print '\n npoints', npoints

sturn1 = s[0*npoints : 1*npoints+1]
sturn2 = s[1*npoints : 2*npoints+1]
sturn3 = s[2*npoints : 3*npoints+1]

bx3IBturn1 = bx3IB[0*npoints : 1*npoints+1] 
bx3IBturn2 = bx3IB[1*npoints : 2*npoints+1] 
bx3IBturn3 = bx3IB[2*npoints : 3*npoints+1]

by3IBturn1 = by3IB[0*npoints : 1*npoints+1] 
by3IBturn2 = by3IB[1*npoints : 2*npoints+1] 
by3IBturn3 = by3IB[2*npoints : 3*npoints+1]

etax3IBturn1 = etax3IB[0*npoints : 1*npoints+1] 
etax3IBturn2 = etax3IB[1*npoints : 2*npoints+1] 
etax3IBturn3 = etax3IB[2*npoints : 3*npoints+1]

bxCoreturn1 = bxCore[0*npoints : 1*npoints+1] 
bxCoreturn2 = bxCore[1*npoints : 2*npoints+1] 
bxCoreturn3 = bxCore[2*npoints : 3*npoints+1]

byCoreturn1 = byCore[0*npoints : 1*npoints+1] 
byCoreturn2 = byCore[1*npoints : 2*npoints+1] 
byCoreturn3 = byCore[2*npoints : 3*npoints+1]

etaxCoreturn1 = etaxCore[0*npoints : 1*npoints+1] 
etaxCoreturn2 = etaxCore[1*npoints : 2*npoints+1] 
etaxCoreturn3 = etaxCore[2*npoints : 3*npoints+1]


# ## Create figure in golden ratio (A paper sizes)
# fig, (axOrbit, axAngle) = plt.subplots(2, 1, sharex=True, figsize=(15,8))
figsizeinch = 14
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(figsizeinch,figsizeinch * 0.3**.5))
# ax1.plot([0.0, C/3.0], [0.0, 0.0], 'k-', lw=1)
ax1.plot(sturn1, bxCoreturn1, 'k-', lw=6, label='Core')
# ax1.plot(sturn1, bxCoreturn2, 'y-', lw=4, label='Core2')
# ax1.plot(sturn1, bxCoreturn3, 'g-', lw=2, label='Core3')
ax1.plot(sturn1, bx3IBturn1, 'r-', lw=2, label='1st turn')
ax1.plot(sturn1, bx3IBturn2, 'b-', lw=2, label='2nd turn')
ax1.plot(sturn1, bx3IBturn3, 'g-', lw=2, label='3rd turn')
ax1.set_ylim(-0.0,38.0)
ax1.set_ylabel(r'$\beta_{x}$ / m ', size=14)
ax1.legend(ncol = 4, loc=1, frameon=True)


# axOrbit.text(120.0, 8.6, "PRELIMINARY", fontsize=40,ha='center',va='top')
# axOrbit.annotate('PRELIMINARY', xy=(120.0,8.6), ha='center',va='top',fontsize=40)
ax2.plot(sturn1, byCoreturn1, 'k-', lw=4, label='Core')
ax2.plot(sturn1, by3IBturn1, 'r-', lw=2, label='1st turn')
ax2.plot(sturn1, by3IBturn2, 'b-', lw=2, label='2nd turn')
ax2.plot(sturn1, by3IBturn3, 'g-', lw=2, label='3rd turn')
ax2.set_ylim(-0.0,38.0)
ax2.set_ylabel(r'$\beta_{y}$ / m ', size=14)

ax3.plot([0.0, C/3.0], [0.0, 0.0], 'k-', lw=1)
ax3.plot(sturn1, etaxCoreturn1, 'k-', lw=4, label='Core')
ax3.plot(sturn1, etax3IBturn1, 'r-', lw=2, label='1st turn')
ax3.plot(sturn1, etax3IBturn2, 'b-', lw=2, label='2nd turn')
ax3.plot(sturn1, etax3IBturn3, 'g-', lw=2, label='3rd turn')
ax3.set_ylim(-0.5,1.15)
ax3.set_ylabel(r'$D_{x}$ / m ', size=14)

xlim(0,C/3.0)
## xlim(0,C/(4.0*3.0))
xlabel('Position s / m', size=14)
# xticks(size=16)


lypos = gca().get_ylim()[1]
tp = Twissplot(lypos = lypos, lysize = lypos*0.15)
tp.paintlattice(twi3IB,0,C/3.0, ec=False, labels=False, fscale=20)
tp.plotstraightnames(12,8,0.8)


# ax = plt.axes()
ax1.xaxis.set_major_locator(ticker.MultipleLocator(15))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(5))

ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax3.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax1.xaxis.grid(which='minor')
ax1.yaxis.grid(which='major')
ax2.xaxis.grid(which='minor')
ax2.yaxis.grid(which='major')
ax3.xaxis.grid(which='minor')
ax3.yaxis.grid(which='major')


tight_layout()
fig.subplots_adjust(hspace=0)

#savefig('res_Twiss.png')
savefig('res_Twiss_XXX.png')


