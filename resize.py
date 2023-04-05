import cv2
import os
shape = 512
path_org = 'ILP_orig'
path_dst = 'ILP'
dataset = os.listdir(path_org)
cnt = 1
for data in dataset:
    print(os.path.join(path_org, data))
    img = cv2.imread(os.path.join(path_org, data), cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img, (shape, shape), interpolation = cv2.INTER_AREA)
    filename =f'{cnt}.jpg'
    cv2.imwrite(os.path.join(path_dst, filename), img)
    cnt += 1