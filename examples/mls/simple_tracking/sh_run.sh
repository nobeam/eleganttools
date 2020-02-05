#!/bin/bash  

#for name in "B2GUser"
#do
#oldLattice=B2ControlUser_org
#oldLattice=B2User
#newLattice=$oldLattice
#newLattice=TEST
#newLattice=B2Qx17.65DDDD
#echo $oldLattice


# lattice=../../lattices_MLS/MLS_2016-09-25_user_FromTT.lte
# outfile=output_MLS_2016-09-25_user_FromTT

# lattice=../../lattices_MLS/MLS_2016-09-25_user_locoFitByFamily.lte
# outfile=output_MLS_2016-09-25_user_locoFitByFamily

# lattice=../../lattices_MLS/MLS_2016-09-25_user_locoFitByMagnet.lte
# outfile=output_MLS_2016-09-25_user_locoFitByMagnet

# lattice=../../lattices_MLS/MLS_2016-09-25_user_locoFitByNoPara.lte
# outfile=output_MLS_2016-09-25_user_locoFitByNoPara

# lattice=../../lattices_MLS/MLS_2016-09-25_user_locoFitByPS.lte
# outfile=output_MLS_2016-09-25_user_locoFitByPS



lattice=../../lattices_MLS/MLS_2016-08-08_9h_3IB_locoFitByMagnet.lte
outfile=output_MLS_2016-08-08_9h_3IB_locoFitByMagnet


# energy=1700
energy=629

echo $lattice
echo $outfile
echo $energy

	echo -e "\n##### Starting elegant #####\n"	
	elegant ele_simpleTracking.ele -macro=rootname=$outfile,energy_mev=$energy,latticename=$lattice
	# elegant ele_simpleTracking.ele -macro=rootname=$outfile,energy_mev=$energy,latticename=$lattice > ele.log
	
	echo -e "\n##### Plot twiss with python #####\n"
	python plotSimpleTracking.py $outfile.w1
	
	evince $outfile.w1_Tracking.pdf &
	
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



