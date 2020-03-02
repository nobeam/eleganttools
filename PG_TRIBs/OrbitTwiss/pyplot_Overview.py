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
sdds.load('output_3IBx.clo')
# Get convenient attribute dictionary
clo3IB = sdds.columnDataDict
print('\n type of clo3IB = ' , type(clo3IB))

sdds.load('output_Core3x.clo')
cloCore = sdds.columnDataDict

sdds.load('output_3IBx.twi')
twi3IB = sdds.columnDataDict

sdds.load('output_Core3x.twi')
twiCore = sdds.columnDataDict

# Length of ring
C = np.max(np.array(twi3IB.s,dtype=np.float64))
print('\n clo3IB...', len(clo3IB), clo3IB.keys(), len(clo3IB.s), C)
print('\n cloCore...', len(cloCore), cloCore.keys(),len(clo3IB.s), C)
print('\n twi3IB...', len(twi3IB), twi3IB.keys(), C)
# print len(clo3IB.s), len(cen.s)


# Create figure in golden ratio (A paper sizes)
#figsizeinch = 28
#fig = figure(figsize=(figsizeinch,figsizeinch * 0.5**.5))

plot(twi3IB.s, twi3IB.betax,  'r-', lw=2, label='3IB betax')
xlim(0,30.0)


"""

subplot(311)
plot(clo3IB.s, clo3IB.x,  'r-', lw=2, label='x 3IB orbit')
plot(clo3IB.s, clo3IB.xp,  'b-', lw=2, label='xp 3IB angle')
plot(clo3IB.s, clo3IB.y,  'g-', lw=20, label='y 3IB orbit')
plot(clo3IB.s, clo3IB.yp,  'y-', lw=8, label='yp 3IB orbit')

# plot(cloCore.s, cloCore.x,  'r-', lw=2, label='x Core orbit')
# plot(cloCore.s, cloCore.xp,  'b-', lw=2, label='xp Core angle')
# plot(cloCore.s, cloCore.y,  'g-', lw=10, label='y Core orbit')
# plot(cloCore.s, cloCore.yp,  'k-', lw=2, label='yp Core orbit')

xlim(0,C)
xlabel('Position s / m', size=18)
ylabel('x,xp, y,yp / m,rad ', size=18)

legend(ncol = 4, loc=3, frameon=True)


lypos = gca().get_ylim()[1]
tp = Twissplot(lypos = lypos, lysize = lypos*0.15)
tp.paintlattice(clo3IB,0,C, ec=False, labels=False, fscale=20)
# tp.plotstraightnames()

subplot(312)
plot(twi3IB.s, twi3IB.betax,  'r-', lw=2, label='3IB betax')
plot(twiCore.s, twiCore.betax,  'b-', lw=2, label='Core betax')
plot(twi3IB.s, twi3IB.betay,  'g-', lw=2, label='3IB betay')
plot(twiCore.s, twiCore.betay,  'y-', lw=2, label='Core betay')

xlim(0,C)
xlabel('Position s / m', size=18)
ylabel('betax, betay / m ', size=18)

legend(ncol = 4, loc=1, frameon=True)


subplot(313)
plot(twi3IB.s, twi3IB.etax,  'r-', lw=2, label='3IB etax')
plot(twiCore.s, twiCore.etax,  'g-', lw=2, label='Core etax')
# plot(twi3IB.s, twi3IB.betay,  'g-', lw=2, label='3IB betay')
# plot(twiCore.s, twiCore.betay,  'y-', lw=2, label='Core betay')

xlim(0,C)
xlabel('Position s / m', size=18)
ylabel('Dispersion etax / m ', size=18)

legend(ncol = 4, loc=1, frameon=True)


tight_layout()
"""
savefig('res_OverviewX.pdf')


