for var in {0..14}
do
    if [[ ${#var} < 2 ]]
    then
        var="0${var}"
    fi
    echo "$var"
    cd video_files
    gsutil -m cp -r \
    "gs://mediapipe-data/videos_for_coral/video_data_for_coral/$1/$var" \
    .
    cd ..
    echo "$PWD"
    python3 png_pose.py
    rm -r "video_files/$var"

    for file in /home/mendel/posebucket-project-posenet/pose_data/*.csv
    do
        echo "sending $file to google cloud server !!"

        runname="$file/tuned_goose"
        direc="gs://mediapipe-data/videos_for_coral/coral_results/$1/"

        /home/mendel/google-cloud-sdk/bin/gsutil cp $file $direc
        echo "file: $file"
	rm $file
   done

done
