import cv2
img  = cv2.imread('download.jpg',1)
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_ITALIC
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(255,0,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_ITALIC
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img,strBGR,(x,y),font,0.5,(255,255,0),2)
        cv2.imshow('image',img)
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

