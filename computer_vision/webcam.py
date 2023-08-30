# pip install opencv-contrin-python pillow mediapipe
import cv2  # library
import numpy as np
CAM_IDX = 0 # 0: default camera
cam = cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
  state, frame = cam.read()
  if not state:
    print('camera is not available')
    break
  # teen paanch yaha se shuru karna 
  frame = cv2.flip(frame,1) #mirror image
  # teen panch yaha pe khatam
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  outline = cv2.Canny(gray, 100,100) # img, min,max
  img = np.hstack([gray, outline])
  # drawing
  img = cv2.putText(img, "GRAY IMAGE",(300,40),
                    cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
  img2 = cv2.putText(img, "CANNY IMAGE",(1280-300,40),
                    cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
  cv2.imshow('gray',img)
  cv2.imshow('outline',img2)
  cv2.imshow('webcam',frame)
  if cv2.waitKey(1) == 27: # ESC key
    break
cam.release()
cv2.destroyAllWindows()