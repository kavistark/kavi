import cv2

cap = cv2.VideoCapture("reso/y6uk.mp4")

while True:
    sucess , vid = cap.read()
    cv2.imshow("videos", vid)
    if cv2.waitKey(1) & 0xFF ==ord('m'):
        break
