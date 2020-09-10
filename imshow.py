import sys
import cv2 as cv

args = sys.argv

fn = args[1]
img = cv.imread(fn, -1)
window = 'img'
cv.namedWindow('img', cv.WINDOW_NORMAL)
while True:
    cv.imshow(window, img)
    key = cv.waitKey(-1)
    if key == 27:
        break
cv.destroyAllWindows()
