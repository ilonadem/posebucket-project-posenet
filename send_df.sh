
for file in /home/mendel/posebucket-project-posenet/pose_data/*.csv
do
	echo "sending $file to google cloud server !!"
	# ../../google-cloud-sdk/bin/gsutil cp $file gs://mediapipe-data/homerun_test1/

	year=${file[*]:50:4}
	month=${file[*]:55:2}
	day=${file[*]:58:2}
	time=${file[*]:61:2}

	echo $1
	# echo "file: $file"
	# echo "file: ${file[*]}"
	# echo "year $year"
	# echo "month $month"
	# echo "day $day"
	# echo "time $time"

	runname="deft_shrimp_data/$1"
	direc="gs://mediapipe-data/$runname/$year/$month/$day/$time/"

	/home/mendel/google-cloud-sdk/bin/gsutil cp $file $direc
	rm $file

done
