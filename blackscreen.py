import time
import cv2 
import numpy as np 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file =cv2.VideoWriter('output.avi',fourcc, 20.0 (640,480))
cap = cv2.Videowriter(0)

time.sleep(0)
bg = 0

frame = cv2.resize(frame, (640,480))
image = cv2.resize(image, (640,480))
for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg, axis=1)

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img,axis=1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
u_black = np.array([104, 153, 70])
i_black = np.array([30, 30, 0])
mask = csv2.inRange(frame, i_black, u_black)
res = cv2.bitwise_and(frame, frame, mask = mask)

f = frame  - res 
f = np.where(f == 0, image, f)
