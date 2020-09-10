import cv2 as cv
import os
import numpy as np
import pdb

datapath = "/home/zhangh/Documents/mypython/unet_tf2/data/target_only"
gt_fns = [os.path.join(datapath, fn) for fn in os.listdir(datapath) if fn.endswith('_gt.png')]
window = "img"
cv.namedWindow(window, cv.WINDOW_NORMAL)
colors = np.array([[0,0,0], [0,255,0]])

bgrs = []
for fn in gt_fns:
    img = cv.imread(fn, -1)
    bgr = colors[img.reshape(-1)]
    bgr = bgr.reshape(*img.shape+(3,))
    bgrs.append(bgr)
    # cv.imwrite(os.path.basename(fn), bgr)

i = 0
while True:
    cv.imshow(window, bgrs[i])
    k = cv.waitKey(-1)
    if k == 27:
        break
    elif k == ord('j'):
        i -= 1
        if i < 0: i = 0
    elif k == ord('k'):
        i += 1
        if i > len(bgrs)-1: i = len(bgrs)-1

cv.destroyAllWindows()
