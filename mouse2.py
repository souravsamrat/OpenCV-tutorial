import cv2
img = cv2.imread('download.jpg', 1)
points = []
def click_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(255,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,16),5)
            cv2.imshow('image',img)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
