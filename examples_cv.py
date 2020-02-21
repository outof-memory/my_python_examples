''' opencv python examples'''
import cv2 as cv
import numpy as np

class examples:
    def __init__(self):
        self.img = cv.imread("./test.jpg", -1)
        self.w, self.h = self.img.shape[:2]

    def undistort_points(self):
        #
        cameraMatrix = np.array([[2000, 0.0, 960],
                                [0.0, 2000, 540],
                                [0.0, 0.0, 1.0]])
        dist = np.array([[ 2.22446743e-01, -7.80478365e-01, -3.24776603e-04,
                        -2.88125977e-04,  0.00000000e+00]])
        points = np.array([[100, 500], [1000, 1000]], np.float32)
        points_undistort = cv.undistortPoints(points.reshape(1, -1, 2), cameraMatrix, 
                            dist, None, cameraMatrix)
        print("points: \n", points)
        print("points after undistort: \n", points_undistort.reshape(-1, 2))
    
    def mouse_callback(self):
        global px, py
        px, py = -1, -1
        def onMouse(event, x, y, flags, param):
            global px, py
            # not list other events
            if event == cv.EVENT_LBUTTONDOWN:
                print("Left button is pressed!")
                px, py = x, y

        windowname = "img"
        cv.namedWindow(windowname, cv.WINDOW_NORMAL)
        cv.setMouseCallback(windowname, onMouse)

        img_tmp = self.img.copy()
        while True:
            cv.imshow(windowname, img_tmp)
            if px>0: 
                cv.circle(img_tmp, (px, py), 40, [255, 0, 0], 2)
            key = cv.waitKey(1)
            if key == 27:
                break
            elif key == ord('c'):
                img_tmp = self.img.copy()
                px = -1
        cv.destroyAllWindows()

if __name__ == "__main__":
    ex = examples()
    ex.undistort_points()
    ex.mouse_callback()