import cv2
import numpy as np
from pygame import mixer
cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')
mixer.init()
guitary=mixer.Sound("guitar.wav")
def guitar():
    guitary.play()
def drums():
    mixer.music.load("accoustic.wav")
    mixer.music.play()
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    contour = hands
    contour = np.array(contour)
    cv2.rectangle(frame,(10,100),(100,200),(0,255,0),5)
    cv2.putText(frame,"Guitar",(10,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.rectangle(frame,(10,350),(100,230),(0,255,220),5)
    cv2.putText(frame,"Accoustic",(30,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    if len(contour)<=2:
         for (x,y,w,h) in hands:
             print(x,y,w,h)
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
             if x in range(10,25) and y in range(230,250):
                 drums()
             if y in range(110,125):
                 guitar()
    cv2.imshow('Driver_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
