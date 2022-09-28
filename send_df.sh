for file in ./pose_data/*.csv
do
	echo "sending $file to google cloud server !!"
	../../google-cloud-sdk/bin/gsutil cp $file gs://mediapipe-data/posenet_testing2/
	rm $file
done
