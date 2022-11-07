import cv2
import numpy as np
import os
import time
from tqdm import tqdm

# set video file path of input video with name and extension
arr=sorted(list(os.listdir('./faceforensics++/manipulated_sequences/Deepfakes/c23/videos/')))



frame_skip=10
index = 0

for i in tqdm(arr[:40]):
    st='./faceforensics++/manipulated_sequences/Deepfakes/c23/videos/'+i
    vid = cv2.VideoCapture(st)
    if not os.path.exists('./frames/Deepfakes'):
        os.makedirs('./frames/Deepfakes')

    #for frame identity
    frame_count=0
    while(True):
        # Extract images
        ret, frame = vid.read()
        # end of frames
        if not ret: 
            break
        # Saves images

        if frame_count==frame_skip:
            break
        else:
            name = './frames/Deepfakes/' +  'df_' + str(index) + '.jpg'
            cv2.imwrite(name, frame)
            frame_count+=1

        # next frame
        index += 1

