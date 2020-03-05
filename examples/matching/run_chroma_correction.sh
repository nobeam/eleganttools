#!/bin/bash

# 1) chromaticity correction:

ln -s ../../lattices_B2/BII_2016-12-19_user_Split_noID_LOCOfitted_ActualUserMode.lte input.lte

elegant matchChromaticity.ele

elegant twissOutput.ele

egrep --color 'S1|S2' output_newChromaticity.lte

# calculate twiss

#ln -s output_newChromaticity.lte active.lte

#ln -s ../twissPlot/plotTwiss.py
#ln -s ../twissPlot/twissOutput.ele

#elegant twissOutput.ele

#python plotTwiss.py "general" "$(date)"
