import cv2
import numpy as np
from urllib import request

url = 'http://192.168.31.110/mjpeg/1'
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 图像处理代码

    cv2.imshow('ESP32-CAM Video Stream', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()