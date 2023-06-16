# Opens images from a specified folder and saves their pose info
# in a csv file.

from pose_engine import PoseEngine
from PIL import Image
from PIL import ImageDraw

import numpy as np
import os
import csv

# os.system('wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/'
#           'Hindu_marriage_ceremony_offering.jpg/'
#           '640px-Hindu_marriage_ceremony_offering.jpg -O /tmp/couple.jpg')
# pil_image = Image.open('/tmp/couple.jpg').convert('RGB')

def save_dict(p_dict, filename):
    data_dir = 'pose_data'
    # date_str = date.today()
    # filenum = len(os.listdir(data_dir))+1
    
    csv_file = data_dir + f'/{filename}.csv'
    print("saving csv file name: ", csv_file)
    with open(csv_file, 'w') as f:
        writer = csv.DictWriter(f, p_dict.keys())
        writer.writeheader()
        writer.writerow(p_dict)

n = 0
pose_dict = {}

poses_list = ['NOSE', 'LEFT_EYE', 'RIGHT_EYE', 'LEFT_EAR', 'RIGHT_EAR', 'LEFT_SHOULDER', 'RIGHT_SHOULDER', 'LEFT_ELBOW', 'RIGHT_ELBOW', 'LEFT_WRIST', 'RIGHT_WRIST', 'LEFT_HIP', 'RIGHT_HIP', 'LEFT_KNEE', 'RIGHT_KNEE', 'LEFT_ANKLE', 'RIGHT_ANKLE']

for img_folder in os.listdir('video_files'):
    for image_file in os.listdir(f'video_files/{img_folder}/'):
        pil_image = Image.open(f'video_files/{img_folder}/' + image_file).convert('RGB')
    # pil_image = Image.open('video_files/images_00/image_0.png').convert('RGB')
        engine = PoseEngine(
            'models/mobilenet/posenet_mobilenet_v1_075_481_641_quant_decoder_edgetpu.tflite')
        poses, inference_time = engine.DetectPosesInImage(pil_image)
        print('Inference time: %.f ms' % (inference_time * 1000))

        # for pose in poses:
        #     if pose.score < 0.4: continue
        #     print('\nPose Score: ', pose.score)
        #     for label, keypoint in pose.keypoints.items():
        #         print('  %-20s x=%-4d y=%-4d score=%.1f' %
        #               (label.name, keypoint.point[0], keypoint.point[1], keypoint.score))

        for pose in poses:
            for key in pose.keypoints.keys():
                point = pose.keypoints[key].point
                score = pose.keypoints[key].score
                
                if n==0:
                    pose_dict[poses_list[key]] = [[point.x, point.y, score, n]]
                else:
                    pose_dict[poses_list[key]].append([point.x, point.y, score, n])

        n += 1

    save_dict(pose_dict, image_file[:-4])
