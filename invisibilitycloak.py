import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
cap = cv2.VideoCapture(0)
time.sleep(0)
bg = 0
for i in range(60):
    ret,bg = cap.read()
bg = np.flip(bg,axis = 1)
while(cap.isOpened()):
    ret,img = cap.read()
    if not ret:
        break
    img = np.flip(img,axis = 1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    frame = cv2.resize(frame, (640,480))
    image = cv2.resize(image, (640,480))
    #lower_red = np.array([170,120,70])
    #upper_red = np.array([180,255,255])
    lower_black = np.array([104,153,70])
    upper_black = np.array ([30,30,0])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    #lower_red = np.array([0,120,50])
    #upper_red = np.array([10,55,55])
    #mask1 = cv2.inRange(hsv,lower_red,upper_red)
    #mask1 = mask1+mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    res_1 = cv2.bitwise_and(img,img,mask = mask2)
    res_2 = cv2.bitwise_and(bg,bg,mask = mask1)
    mask - cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame - res
    f = np.where(f==0, image, f)
    final_output = cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)
    cv2.imshow("magic",final_output)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()