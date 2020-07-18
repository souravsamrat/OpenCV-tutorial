import cv2
import datetime
cap = cv2.VideoCapture('testvideo.mp4')
while (True):
    ret, frame = cap.read()
    if ret== True:
        font = cv2.FONT_ITALIC
        text= str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255),5,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
cv2.destroyAllWindows()
