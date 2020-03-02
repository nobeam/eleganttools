#!/bin/bash  

#for name in "B2GUser"
#do
#oldLattice=B2ControlUser_org
#oldLattice=B2User
#newLattice=$oldLattice
#newLattice=TEST
#newLattice=B2Qx17.65DDDD
#echo $oldLattice


#lattice=BII_2016-12-19_user_Split_noID_LOCOfitted_ActualUserMode.lte
#outfile=output_BII_2016-12-19_user_Split_noID_LOCOfitted_ActualUserMode.lte

#lattice=BII_2016-12-19_user_Split_noID_LOCOfitted_ActualUserMode_HarmSext0.lte
#outfile=output_BII_2016-12-19_user_Split_noID_LOCOfitted_ActualUserMode_HarmSext0.lte

lattice=BII_2016-09-25_TRIBsQx17.666_Split_noID_fixedQIpos_ObservationPoints.lte
outfile=output_BII_2016-09-25_TRIBsQx17.666_Split_noID_fixedQIpos_ObservationPoints.lte
 
# lattice=BII_2016-09-25_TRIBsQx17.666_Split_noID_fixedQIpos_ObservationPoints.lte
# outfile=output_BII_2016-09-25_TRIBsQx17.666_Split_noID_fixedQIpos_ObservationPoints_Q4D2OptTRIBs.lte
 
 
# lattice=BII_2016-09-25_Qx17.65.lte
# outfile=output_BII_2016-09-25_Qx17.65.lte
 
# lattice=BII_2016-09-25_Qx17.66.lte
# outfile=output_BII_2016-09-25_Qx17.66.lte
 
# lattice=BII_2016-09-25_Qx17.62.lte
# outfile=output_BII_2016-09-25_Qx17.62.lte
 
# lattice=BII_2016-09-25_Qx17.665.lte
# outfile=output_BII_2016-09-25_Qx17.665.lte
 
# lattice=BII_2016-09-25_Qx17.666.lte
# outfile=output_BII_2016-09-25_Qx17.666.lte
 
# lattice=BII_2016-09-25_Qx17.6665.lte
# outfile=output_BII_2016-09-25_Qx17.6665.lte

# lattice=BII_tribs_LOCO_FArmborst.lte
# outfile=output_BII_tribs_LOCO_FArmborst.lte

#lattice=max4_octupoles_symbreak_tribs_ele.lte
#outfile=output_max4_octupoles_symbreak_tribs_ele.lte

#lattice=BII_standard_user_FArmborst_Qx17.65.lte
#outfile=output_BII_standard_user_FArmborst_Qx17.65.lte

#energey=3000
energy=1700
#energy=629

echo $lattice
echo $outfile
echo $energy

	echo -e "\n##### Starting elegant #####\n"	
	# elegant ele_simpleTracking.ele -macro=rootname=$outfile,latticename=$lattice
	elegant ele_simpleTracking.ele -macro=rootname=$outfile,energy_mev=$energy,latticename=$lattice
	# elegant ele_simpleTracking.ele -macro=rootname=$outfile,energy_mev=$energy,latticename=$lattice > ele.log
		
	echo -e "\n##### Plot twiss with python #####\n"
	python pyplot_simpleTracking.py $outfile.w1
	python pyplot_Track_XX.py	$outfile.w1
#	python plotSimpleTracking.py $outfile.w2
	
	eog $outfile.w1_Tracking.png &
	
	echo -e "\n##### TwissParas of Lattice:" $newLattice " #####"
	sh sh_GlobalTwiss.sh $outfile.twi
	
	
	
	
	
: <<'COMMENT'

#	sleep 2
	echo -e "\n##### Converting elegant output to root files #####\n"	
#	sleep 1
	sddsBinary2ROOT.sh out_$newLattice.twi
	sddsBinary2ROOT.sh out_$newLattice.mag
	sddsBinary2ROOT.sh out_$newLattice.w1
	sddsBinary2ROOT.sh out_$newLattice.w2
##	sddsBinary2ROOT.sh out_$newLattice.wfft


#	sleep 2
	echo -e "\n##### TwissParas of Lattice:" $newLattice " #####"
	sh script_GlobalTwiss.sh out_$newLattice.twi
#	echo -e "\n##### TwissParas of Lattice:" $newLattice " #####"	>> Bla.txt
#	sh script_GlobalTwiss.sh out_$newLattice.twi >> Bla.txt
#	sleep 1


#	sleep 2
	echo -e "\n##### Plots with root #####\n"	
#	sleep 1
	root -l "plot.C(\"out_$newLattice\")"


#	sleep 2	
	rm out_$newLattice.ma* out_$newLattice.w* out_$newLattice.twi.root
	

COMMENT

#done



