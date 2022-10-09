
for file in /home/mendel/coral/posebucket-project-posenet/pose_data/*.csv
do
	echo "sending $file to google cloud server !!"
	# ../../google-cloud-sdk/bin/gsutil cp $file gs://mediapipe-data/homerun_test1/

	year=${file[*]:56:4}
	month=${file[*]:61:2}
	day=${file[*]:64:2}
	time=${file[*]:67:2}

	# echo "file: $file"
	# echo "file: ${file[*]}"
	# echo "year $year"
	# echo "month $month"
	# echo "day $day"
	# echo "time $time"

	runname="homerun_test1"
	direc="gs://mediapipe-data/$runname/$year/$month/$day/$time/"

	/home/mendel/google-cloud-sdk/bin/gsutil cp $file $direc
	rm $file

done
