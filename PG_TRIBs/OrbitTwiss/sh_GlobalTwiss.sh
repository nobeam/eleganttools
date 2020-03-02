#!/bin/bash 
# execute with: ./script_GlobalTwiss.sh filename.twi

echo "GlobalTwiss for " $1
for parameter in nu? alpha* dnu*/dp* beta?Max beta?Min tau* ex0 Sdelta0 U0 
#dnu*/dA* dnu*/dJ* beta?Max h11001 h00111 h30000 tau* ex0 Sdelta0 U0 
#for parameter in nu? alpha* dnu*/dp* beta?Max tau* ex0 Sdelta0 U0 \
#nu?ChromUpper nu?ChromLower nu?TswaUpper nu?TswaLower
#for parameter in nu?
do
	sddsprintout $1 -noTitle -spreadsheet -par=$parameter,format=%.15f
done

: <<'END'
echo "----------------"
echo -e "/n RFSetting" 
for parameter in PhiSynch Voltage BucketHalfHeight nuSynch Sz0 St0
do 
	sddsprintout $2 -noTitle -spreadsheet -par=$parameter,format=%.15f
done
END


: <<'END'
for name in "BVUser" "BVLowA_D0"
do
	echo "###############################"
	echo "GlobalTwiss parameter for $name"
	echo "###############################"
	sddsprintout out_$name.twi -noTitle -spreadsheet -par=nu? -par=alpha*
	sddsprintout out_$name.twi -noTitle	-spreadsheet -par=dnu*/dp* 
	sddsprintout out_$name.twi -noTitle	-spreadsheet -par=dnu*/dA*
	sddsprintout out_$name.twi -noTitle	-spreadsheet -par=dnu*/dJ*
#	sddsprintout out_$name.twi -noTitle	-spreadsheet -par=nu?Tsqa* 
	sddsprintout out_$name.twi -noTitle -spreadsheet -par=tau*
	sddsprintout out_$name.twi -noTitle -spreadsheet -par=ex0	-par=Sdelta0 -par=U0
#	sddsprintout out_$name.twi -noTitle -spreadsheet -par=
#	sddsprintout out_$name.twi -noTitle -spreadsheet -par=	
done
END
