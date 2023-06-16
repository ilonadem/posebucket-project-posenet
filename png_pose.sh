for var in {1..10}
do
    if [[ ${#var} < 2 ]]
    then
        var="0${var}"
    fi
    echo "$var"
    
done

for file in /home/mendel/posebucket-project-posenet/pose_data/*.csv
do
	echo "sending $file to google cloud server !!"
	# ../../google-cloud-sdk/bin/gsutil cp $file gs://mediapipe-data/homerun_test1/

	# year=${file[*]:50:4}
	# month=${file[*]:55:2}
	# day=${file[*]:58:2}
	# time=${file[*]:61:2}

	# echo $1
	# echo "file: $file"
	# echo "file: ${file[*]}"
	# echo "year $year"
	# echo "month $month"
	# echo "day $day"
	# echo "time $time"

	runname="$file/tuned_goose"
	direc="gs://mediapipe-data/videos_for_coral/coral_results/tuned_goose/"

	/home/mendel/google-cloud-sdk/bin/gsutil cp $file $direc
	rm $file

done

# if [[ ${#input} < 2 ]] 
# then
#     inputNo="00${inputNo}"
#     inputNo="${inputNo: -2}"
# fi

# gsutil -m cp -r \
#   "gs://mediapipe-data/videos_for_coral/images_00" \
#   .