import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def canny(img, low_threshold, high_threshold):
        return cv2.Canny(img, low_threshold, high_threshold)
    
blur_kernel_size = (15, 15)
canny_low_threshold = 100
canny_high_threshold = 250

cap = cv2.VideoCapture('roadvid.mp4')
frame_counter = 0
#reaing viedeo frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    r, f = cap.read()
    #preaparing image to draw lines
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray_image, blur_kernel_size, 0)

    canny_low_threshold = 100
    canny_high_threshold = 250
    blur_canny = canny(gray_image,    canny_low_threshold, canny_high_threshold)
    img = blur_canny
    height, width = img.shape[:2]
    h = 1500
    w = 600
    x = 600
    y = 900
    img1 = img[x:x+h, y:y+w]
    img2 =  np.zeros_like(img)
    img2 [x:x+h, y:y+w] = img1
    src = img2
    dst = cv2.Canny(src, 50, 200, None, 3)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    #drawing lines
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines [i][0][0]
            theta = lines [i][0][1]
            a = math.cos( theta )
            b = math.sin( theta )
            x0 = a * rho
            y0 = b * rho
            pt1 = (int (x0 + 1000 *(-b)), int (y0 + 1000 *(a)))
            pt2 = (int (x0 - 1000 *(-b)), int (y0 - 1000 *(a)))
            cv2.line( cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    linesP = cv2.HoughLinesP (dst, 1, np.pi / 180, 50, None, 50, 10)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP [i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)

    #adding raw frame and red lines
    img2 = cv2.addWeighted(f, 0.8, cdstP, 1, 0)
    #napis
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img2, "LUKASZ RUZICKI", (1250,750), font, 1,(255,255,0), 1, cv2.LINE_AA)
    cv2.imshow('sum', img2)
    frame_counter = frame_counter + 1

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() # destroy all opened windows
print(count)