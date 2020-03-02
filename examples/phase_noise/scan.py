#!/usr/bin/python
from pylab import *

import os
import shlex
import subprocess

from sddshzb import SDDSad
from sddshzb import Twissplot


def run(**kw):
    if len(kw) < 1:
        return
    cmd = "elegant -macro="
    first = True
    for key in kw:
        # print key, kw[key]
        if not first:
            cmd += ","
        cmd += "{0}={1}".format(key, kw[key])
        first = False
    cmd += " track.ele"
    args = shlex.split(cmd)
    # print 'Cmd:',cmd

    words = subprocess.check_output(args, stderr=subprocess.STDOUT)
    # #.split()
    # #print "Words:",words
    # if words.find('unstable') != -1:
    #     return

    twis = SDDSad(0)
    twis.load("output.w1")
    par = twis.parameterData
    col = twis.columnDataDict
    St = np.mean(col.St)
    dCtpp = np.ptp(col.dCt)
    # if len(col.s) ==0:
    #     return (0,0,0,0)
    # else:
    #     return (col.s[0],col.x[0],col.xp[0],col.Pass[0])
    return (St, dCtpp)


Sta = []
dCta = []
freqs = logspace(1, 5, 50)
for f in freqs:
    (St, dCt) = run(freq=f)
    Sta.append(St)
    dCta.append(dCt)
    # sa.append(s)
    # sx.append(x)
    # sxp.append(xp)
    # spass.append(Pass)
    print f, St, dCt

savetxt("bl.txt", np.c_[freqs, Sta, dCta])

subplot(211)
plot(freqs, Sta, "o")
ylabel("St average")
xlabel("f / Hz")
grid()
xscale("log")

subplot(212)
plot(freqs, dCta, "o")
ylabel("dCt peak to peak")
xlabel("f / Hz")
grid()
xscale("log")

tight_layout()
savefig("noise.pdf")
