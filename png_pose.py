# Opens images from a specified folder and saves their pose info
# in a csv file.

from pose_engine import PoseEngine
from PIL import Image
from PIL import ImageDraw

import numpy as np
import os

# os.system('wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/'
#           'Hindu_marriage_ceremony_offering.jpg/'
#           '640px-Hindu_marriage_ceremony_offering.jpg -O /tmp/couple.jpg')
# pil_image = Image.open('/tmp/couple.jpg').convert('RGB')
pil_image = Image.open('video_files/images_00/image_0.png').convert('RGB')
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
        print(point, score)